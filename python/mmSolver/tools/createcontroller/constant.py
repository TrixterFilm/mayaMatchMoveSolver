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
Constant values for the create controller tool.
"""

TRANSLATE_ATTRS = [
    'translateX', 'translateY', 'translateZ'
]

ROTATE_ATTRS = [
    'rotateX', 'rotateY', 'rotateZ'
]

SCALE_ATTRS = [
    'scaleX', 'scaleY', 'scaleZ'
]

TFM_ATTRS = []
TFM_ATTRS += TRANSLATE_ATTRS
TFM_ATTRS += ROTATE_ATTRS
TFM_ATTRS += SCALE_ATTRS

# Constants for Bake modes.
BAKE_MODE_FULL_BAKE_VALUE = 'full_bake'
BAKE_MODE_SMART_BAKE_VALUE = 'smart_bake'
BAKE_MODE_CURRENT_FRAME_VALUE = 'current_frame'
BAKE_MODE_VALUE_LIST = [
    BAKE_MODE_FULL_BAKE_VALUE,
    BAKE_MODE_SMART_BAKE_VALUE,
    BAKE_MODE_CURRENT_FRAME_VALUE,
]

BAKE_MODE_FULL_BAKE_LABEL = 'Full Bake'
BAKE_MODE_SMART_BAKE_LABEL = 'Smart Bake'
BAKE_MODE_CURRENT_FRAME_LABEL = 'Current Frame'
BAKE_MODE_LABEL_LIST = [
    BAKE_MODE_FULL_BAKE_LABEL,
    BAKE_MODE_SMART_BAKE_LABEL,
    BAKE_MODE_CURRENT_FRAME_LABEL,
]


# Type of controller node to create.
CONTROLLER_NODE_TYPE_GROUP_VALUE = 'group'
CONTROLLER_NODE_TYPE_LOCATOR_VALUE = 'locator'
CONTROLLER_NODE_TYPE_VALUE_LIST = [
    CONTROLLER_NODE_TYPE_GROUP_VALUE,
    CONTROLLER_NODE_TYPE_LOCATOR_VALUE,
]

CONTROLLER_NODE_TYPE_GROUP_LABEL = 'Group Node'
CONTROLLER_NODE_TYPE_LOCATOR_LABEL = 'Locator'
CONTROLLER_NODE_TYPE_LABEL_LIST = [
    CONTROLLER_NODE_TYPE_GROUP_LABEL,
    CONTROLLER_NODE_TYPE_LOCATOR_LABEL,
]


# Default Controller values
DEFAULT_BAKE_MODE = BAKE_MODE_FULL_BAKE_VALUE
# DEFAULT_MODE = 'fourier'
# DEFAULT_WIDTH = 2
# DEFAULT_BLEND_WIDTH = 2

# Configuration key names to save values against.
CONFIG_BAKE_MODE_KEY = 'mmSolver_controller_bake_mode'
# CONFIG_MODE_KEY = 'mmSolver_smoothkeyframes_mode'
# CONFIG_WIDTH_KEY = 'mmSolver_smoothkeyframes_width'
# CONFIG_BLEND_WIDTH_KEY = 'mmSolver_smoothkeyframes_blendWidth'
