# Copyright (C) 2019 David Cattermole.
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

Usage::

  1) Select transform node.

  2) Run 'create' tool, new world-space transform is created at same
     position as input transform nodes.

  3) New nodes are selected.

  4) User manipulates newly created nodes.

  5) Run 'bake' tool, selected transform nodes are deleted and
      animation is transfered back onto original nodes.

"""

import maya.cmds

import mmSolver.logger

import mmSolver.utils.tools as tools_utils
import mmSolver.tools.createcontroller.lib as lib


LOG = mmSolver.logger.get_logger()


def main():
    """
    Remove selected controllers and bake data on controlled nodes.
    """
    nodes = maya.cmds.ls(selection=True, long=True) or []
    if len(nodes) == 0:
        LOG.warn("Select transform nodes.")
        return

    # TODO: Get from the config.
    smart_bake = False
    start_frame = None
    end_frame = None

    ctx = tools_utils.tool_context(
        use_undo_chunk=True,
        pre_update_frame=True,
        post_update_frame=True,
        restore_current_frame=True,
        use_dg_evaluation_mode=True,
        disable_viewport=True)
    with ctx:
        orig_nodes = lib.remove(
            nodes,
            smart_bake=smart_bake,
            start_frame=start_frame,
            end_frame=end_frame)
        if len(orig_nodes) > 0:
            maya.cmds.select(orig_nodes, replace=True)

    # Trigger Maya to refresh.
    maya.cmds.refresh(currentView=True, force=False)
    return


def open_window():
    import mmSolver.tools.removecontroller.ui.removecontroller_window as window
    window.main()
