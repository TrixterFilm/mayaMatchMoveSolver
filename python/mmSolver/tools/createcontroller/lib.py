# Copyright (C) 2019, 2020, 2021 David Cattermole.
#
# This file is part of mmSolver.
#
# mmSolver is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# mmSolver is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with mmSolver.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Create a controller transform node.
"""

import collections

import maya.cmds

import mmSolver.logger

import mmSolver.utils.node as node_utils
import mmSolver.utils.time as time_utils
import mmSolver.utils.animcurve as anim_utils
import mmSolver.utils.transform as tfm_utils
import mmSolver.tools.reparent.keytimeutils as keytime_utils
import mmSolver.tools.createcontroller.constant as const

import mmSolver.api as mmapi

LOG = mmSolver.logger.get_logger()


def _bake_attributes(nodes, attrs, start_frame, end_frame, smart_bake=False):
    """
    Bake the attributes on nodes.

    .. note::
        If 'attrs' is empty, all keyable attributes are baked on the nodes.

    :param nodes: Nodes to bake.
    :param attrs: Attributes to bake. If empty, bake all keyable attributes.
    :param start_frame: Start frame to bake.
    :param end_frame: End frame to bake.
    :param smart_bake: Perform a "smart" bake - do not bake per-frame.
    """
    assert isinstance(nodes, list)
    assert isinstance(start_frame, (int, long))
    assert isinstance(end_frame, (int, long))
    assert isinstance(smart_bake, bool)
    assert isinstance(attrs, list)
    if smart_bake is True:
        maya.cmds.bakeResults(
            nodes,
            time=(start_frame, end_frame),
            attribute=attrs,
            smart=int(smart_bake),
            simulation=True,
            sparseAnimCurveBake=False,
            minimizeRotation=True)
    else:
        maya.cmds.bakeResults(
            nodes,
            time=(start_frame, end_frame),
            attribute=attrs,
            simulation=True,
            sparseAnimCurveBake=False,
            minimizeRotation=True)
    return


def _get_keyable_attrs(node, attrs):
    keyable_attrs = set()
    for attr in attrs:
        plug = node + '.' + attr
        keyable = maya.cmds.getAttr(plug, keyable=True)
        settable = maya.cmds.getAttr(plug, settable=True)
        if settable is True and keyable is True:
            keyable_attrs.add(plug)
    return keyable_attrs


def _get_skip_attrs(node, attrs):
    assert len(attrs) == 3
    axis_list = ['x', 'y', 'z']
    skip_attrs = set(axis_list)
    for axis, attr in zip(axis_list, attrs):
        plug = node + '.' + attr
        keyable = maya.cmds.getAttr(plug, keyable=True)
        settable = maya.cmds.getAttr(plug, settable=True)
        if settable is True and keyable is True:
            skip_attrs.remove(axis)
    return skip_attrs


def _get_constraints_from_ctrls(input_node):
    """
    Get Constraints 'input_node' is connected to.
    """
    constraints = maya.cmds.listConnections(
        input_node,
        type='constraint',
        source=False,
        destination=True) or []
    constraints = [n for n in constraints
                   if node_utils.node_is_referenced(n) is False]
    constraints = set(constraints)
    if len(constraints) == 0:
        LOG.warn('Node is not controlling anything: %r', input_node)
        return set()
    assert input_node not in constraints
    return constraints


def _get_destination_nodes_from_ctrls(constraints):
    """
    Get nodes connected to constraints.
    """
    dest_nodes = set()
    attr = 'constraintParentInverseMatrix'
    for constraint in constraints:
        plug = constraint + '.' + attr
        temp = maya.cmds.listConnections(
            plug,
            type='transform',
            source=True,
            destination=False,
        ) or []
        dest_nodes |= set(temp)
    if len(dest_nodes) != 1:
        return []
    return list(dest_nodes)


def _remove_constraint_blend_attr_from_nodes(nodes):
    for node in nodes:
        attr_list = maya.cmds.listAttr(node)
        for attr in attr_list:
            if ("blendPoint" in attr
                    or "blendOrient" in attr
                    or "blendParent" in attr):
                maya.cmds.deleteAttr(str(node) + "." + str(attr))
    return


def _delete_keyframes_on_transforms(tfm_nodes):
    """
    Delete all keyframes on given TransformNode objects.
    """
    keyable_attrs = set()
    for tfm_node in tfm_nodes:
        node = tfm_node.get_node()
        keyable_attrs |= _get_keyable_attrs(node, const.TFM_ATTRS)
    anim_curves = anim_utils.get_anim_curves_from_nodes(
        list(keyable_attrs))
    anim_curves = [n for n in anim_curves
                   if node_utils.node_is_referenced(n) is False]
    if len(anim_curves) > 0:
        maya.cmds.delete(anim_curves)
    return


def _create_constraint(src_node, dst_node):
    """
    Create constraint from source node to destination node.

    :param src_node: Constrain from this node.
    :type src_node: stc

    :param dst_node: Control this node with constraint nodes.
    :type dst_node: str

    :rtype: [str, ..]
    """
    constraints = []
    skip = _get_skip_attrs(src_node, const.TRANSLATE_ATTRS)
    if len(skip) != 3:
        constraints += maya.cmds.pointConstraint(
            dst_node,
            src_node,
            skip=tuple(skip)
        ) or []
    skip = _get_skip_attrs(src_node, const.ROTATE_ATTRS)
    if len(skip) != 3:
        constraints += maya.cmds.orientConstraint(
            dst_node,
            src_node,
            skip=tuple(skip)
        ) or []
    skip = _get_skip_attrs(src_node, const.SCALE_ATTRS)
    if len(skip) != 3:
        constraints += maya.cmds.scaleConstraint(
            dst_node,
            src_node,
            skip=tuple(skip)
        ) or []
    return constraints


def _sort_by_hierarchy(nodes, children_first=False):
    """
    Sort the nodes by hierarchy depth; level 0 first, 1 second,
    until 'n'.
    """
    assert isinstance(nodes, (list, set, tuple))
    depth_to_node_map = collections.defaultdict(list)
    for node in nodes:
        assert isinstance(node, basestring)
        depth = node.count('|')
        depth_to_node_map[depth].append(node)
    nodes = []
    depths = sorted(depth_to_node_map.keys())
    if children_first is True:
        depths = reversed(depths)
    for depth in depths:
        node_list = depth_to_node_map.get(depth)
        assert len(node_list) > 0
        nodes += sorted(node_list)
    return nodes


def _sort_hierarchy_depth_to_nodes(nodes):
    depth_to_node_map = collections.defaultdict(set)
    for node in nodes:
        depth = node.count('|')
        depth_to_node_map[depth].add(node)
    return depth_to_node_map


def _sort_hierarchy_depth_to_tfm_nodes(tfm_nodes):
    depth_to_tfm_node_map = collections.defaultdict(list)
    for tfm_node in tfm_nodes:
        depth = tfm_node.get_node().count('|')
        depth_to_tfm_node_map[depth].append(tfm_node)
    return depth_to_tfm_node_map


def _guess_frame_range_from_nodes(nodes):
    """Query keyframe times on each node attribute."""
    maya_start_frame, maya_end_frame = time_utils.get_maya_timeline_range_outer()
    keytime_obj = keytime_utils.KeyframeTimes()
    for node in nodes:
        keytime_obj.add_node_attrs(
            node, const.TFM_ATTRS, maya_start_frame, maya_end_frame)
    start_frame, end_frame = keytime_obj.sum_frame_range_for_nodes(nodes)
    return start_frame, end_frame


def _get_node_parent_map(nodes):
    """
    For each transform node, get the parent transform above it. If no
    parent node exists, get the parent should be None (ie, world or
    root).
    """
    nodes_parent = {}
    for node in nodes:
        parent = None
        parents = node_utils.get_all_parent_nodes(node)
        parents = list(reversed(parents))
        while len(parents) != 0:
            p = parents.pop()
            if p in nodes:
                parent = p
                break
        nodes_parent[node] = parent
    assert len(nodes_parent) == len(nodes)
    return nodes_parent


def _create_locator(name, node_parent, rotate_order):
    tfm = maya.cmds.createNode(
        'transform',
        name=name,
        parent=node_parent)
    tfm = node_utils.get_long_name(tfm)
    shape_name = name + 'Shape'
    maya.cmds.createNode('locator', name=shape_name, parent=tfm)
    maya.cmds.xform(tfm, rotateOrder=rotate_order, preserve=True)
    # TODO: Make rotation order attribute visible in channel box.
    return tfm


def _create_nodes_in_hierarchy(depth_to_tfm_node_map, nodes_parent, with_zero_node):
    """Create new (locator) node for each input node."""
    assert isinstance(with_zero_node, bool)
    ctrl_list = []
    node_to_ctrl_map = {}
    node_to_ctrl_tfm_map = {}
    depths = sorted(depth_to_tfm_node_map.keys())
    for depth in depths:
        depth_tfm_nodes = depth_to_tfm_node_map.get(depth)
        assert depth_tfm_nodes is not None
        sorted_tfm_nodes = sorted(depth_tfm_nodes, key=lambda x: x.get_node())
        for tfm_node in sorted_tfm_nodes:
            node = tfm_node.get_node()
            node_parent = nodes_parent.get(node)
            if node_parent is not None:
                node_parent = node_to_ctrl_map.get(node_parent)
            name = node.rpartition('|')[-1]
            assert '|' not in name
            name = name.replace(':', '_')
            name = name + '_CTRL'
            name = mmapi.find_valid_maya_node_name(name)

            rot_order = maya.cmds.xform(node, query=True, rotateOrder=True)

            tfm = _create_locator(name, node_parent, rot_order)
            ctrl_tfm = tfm_utils.TransformNode(node=tfm)

            zero_tfm = tfm
            ctrl_zero_tfm = ctrl_tfm
            if with_zero_node is True:
                zero_tfm = _create_locator('zero', tfm, rot_order)
                ctrl_zero_tfm = tfm_utils.TransformNode(node=zero_tfm)

            ctrl_list.append((tfm, zero_tfm))
            node_to_ctrl_map[node] = (tfm, zero_tfm)
            node_to_ctrl_tfm_map[node] = (ctrl_tfm, ctrl_zero_tfm)
    return ctrl_list, node_to_ctrl_map, node_to_ctrl_tfm_map


def _find_controlled_from_controller_nodes(tfm_nodes):
    """Find controlled nodes from controller nodes."""
    ctrl_to_ctrlled_map = {}
    for tfm_node in tfm_nodes:
        node = tfm_node.get_node()
        constraints = _get_constraints_from_ctrls(node)
        dests = _get_destination_nodes_from_ctrls(constraints)
        if len(dests) == 0:
            continue
        dests = _sort_by_hierarchy(dests, children_first=True)
        ctrl_to_ctrlled_map[node] = (constraints, dests)
    return ctrl_to_ctrlled_map


def create(nodes,
           current_frame=None,
           eval_mode=None,
           node_type=None,
           with_zero_node=None,
           smart_bake=None,
           start_frame=None,
           end_frame=None,
           delete_existing_keyframes=None):
    """
    Create a Controller for the given nodes.

    :param nodes: The nodes to create Controller for.
    :type nodes: [str, ..]

    :param current_frame: What frame number is considered to be
                          'current' when evaluating transforms without
                          any keyframes.
    :type current_frame: float or int

    :param eval_mode: What type of transform evaluation method to use?
    :type eval_mode: mmSolver.utils.constant.EVAL_MODE_*

    :returns: List of controller transform nodes.
    :rtype: [str, ..]
    """
    if current_frame is None:
        current_frame = maya.cmds.currentTime(query=True)
    assert current_frame is not None
    if delete_existing_keyframes is None:
        delete_existing_keyframes = False
    if smart_bake is None:
        smart_bake = True
    if with_zero_node is None:
        with_zero_node = True
    if node_type is None:
        node_type = const.CONTROLLER_NODE_TYPE_LOCATOR_VALUE
    assert node_type in const.CONTROLLER_NODE_TYPE_VALUE_LIST
    if start_frame is None or end_frame is None:
        start_frame, end_frame = _guess_frame_range_from_nodes(nodes)

    tfm_nodes = [tfm_utils.TransformNode(node=n) for n in nodes]
    nodes = [n.get_node() for n in tfm_nodes]

    depth_to_tfm_node_map = _sort_hierarchy_depth_to_tfm_nodes(tfm_nodes)
    nodes_parent = _get_node_parent_map(nodes)

    # Create new (locator) node for each input node
    ctrl_list, node_to_ctrl_map, node_to_ctrl_tfm_map = \
        _create_nodes_in_hierarchy(
            depth_to_tfm_node_map,
            nodes_parent,
            with_zero_node)

    # Move the created controller nodes to the input node.
    all_constraints = []
    ctrl_to_constraints_map = {}
    for node, (ctrl, zero_tfm) in node_to_ctrl_map.items():
        src_node = ctrl
        dst_node = node
        constraints = _create_constraint(src_node, dst_node)
        ctrl_to_constraints_map[ctrl] = constraints
        all_constraints += constraints

    # Bake position of controllers.
    ctrl_nodes = [ctrl_tfm for ctrl_tfm, _ in ctrl_list]
    attrs = const.TFM_ATTRS
    _bake_attributes(
        ctrl_nodes, attrs, start_frame, end_frame, smart_bake=smart_bake)
    if len(all_constraints) > 0:
        maya.cmds.delete(all_constraints)

    if delete_existing_keyframes is True:
        # Delete all keyframes on controlled nodes before
        # constraining, to avoid pair-blend nodes and "green" channel
        # box keyframe attributes.
        _delete_keyframes_on_transforms(tfm_nodes)

    # Create constraint(s) to previous nodes.
    for tfm_node in tfm_nodes:
        src_node = tfm_node.get_node()
        ctrl, zero_ctrl = node_to_ctrl_tfm_map.get(src_node)
        dst_node = zero_ctrl.get_node()
        _create_constraint(src_node, dst_node)
    return ctrl_nodes


def remove(nodes,
           current_frame=None,
           eval_mode=None,
           smart_bake=None,
           start_frame=None,
           end_frame=None):
    """
    Remove a controller and push the animation back to the controlled
    object.

    Order the nodes to remove by hierarchy depth. This means that
    children will be removed first, then parents, this ensures we
    don't delete a controller accidentally when a parent controller is
    deleted first.

    :param nodes: The nodes to delete.
    :type nodes: [str, ..]

    :param current_frame: What frame number is considered to be
                          'current' when evaluating transforms without
                          any keyframes.
    :type current_frame: float or int

    :param eval_mode: What type of transform evaluation method to use?
    :type eval_mode: mmSolver.utils.constant.EVAL_MODE_*

    :returns: List of once controlled transform nodes, that are no
              longer controlled.
    :rtype: [str, ..]
    """
    if current_frame is None:
        current_frame = maya.cmds.currentTime(query=True)
    assert current_frame is not None
    if smart_bake is None:
        smart_bake = True
    if start_frame is None or end_frame is None:
        start_frame, end_frame = _guess_frame_range_from_nodes(nodes)

    nodes = _sort_by_hierarchy(nodes, children_first=True)
    tfm_nodes = [tfm_utils.TransformNode(node=n)
                 for n in nodes]

    # Find controlled nodes from controller nodes
    ctrl_to_ctrlled_map = _find_controlled_from_controller_nodes(tfm_nodes)

    # Get Controlled nodes
    ctrlled_nodes = set()
    for src_node, (_, dst_nodes) in ctrl_to_ctrlled_map.items():
        for dst_node in dst_nodes:
            ctrlled_nodes.add(dst_node)
    ctrlled_nodes = list(ctrlled_nodes)

    # Find constraints on controlled nodes.
    const_nodes = set()
    for src_node, (constraints, _) in ctrl_to_ctrlled_map.items():
        assert src_node not in constraints
        const_nodes |= constraints
    const_nodes = list(const_nodes)

    # Bake position of controlled nodes.
    attrs = const.TFM_ATTRS
    _bake_attributes(
        ctrlled_nodes, attrs, start_frame, end_frame, smart_bake=smart_bake)
    _remove_constraint_blend_attr_from_nodes(ctrlled_nodes)

    # Delete constraints on controlled nodes.
    if len(const_nodes) > 0:
        maya.cmds.delete(const_nodes)

    # Delete controller nodes
    ctrl_nodes = [n.get_node() for n in tfm_nodes]
    if len(ctrl_nodes) > 0:
        maya.cmds.delete(ctrl_nodes)
    return list(ctrlled_nodes)
