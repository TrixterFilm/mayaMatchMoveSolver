# Copyright (C) 2021 David Cattermole.
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
Reparent Transforms constants.
"""

WINDOW_TITLE = 'Reparent'

# Constants for frame range mode.
FRAME_RANGE_MODE_TIMELINE_INNER_VALUE = 'timeline_inner'
FRAME_RANGE_MODE_TIMELINE_OUTER_VALUE = 'timeline_outer'
FRAME_RANGE_MODE_CUSTOM_VALUE = 'custom'
FRAME_RANGE_MODE_VALUES = [
    FRAME_RANGE_MODE_TIMELINE_INNER_VALUE,
    FRAME_RANGE_MODE_TIMELINE_OUTER_VALUE,
    FRAME_RANGE_MODE_CUSTOM_VALUE,
]
FRAME_RANGE_MODE_TIMELINE_INNER_LABEL = 'Timeline (Inner)'
FRAME_RANGE_MODE_TIMELINE_OUTER_LABEL = 'Timeline (Outer)'
FRAME_RANGE_MODE_CUSTOM_LABEL = 'Custom'
FRAME_RANGE_MODE_LABELS = [
    FRAME_RANGE_MODE_TIMELINE_INNER_LABEL,
    FRAME_RANGE_MODE_TIMELINE_OUTER_LABEL,
    FRAME_RANGE_MODE_CUSTOM_LABEL,
]

# Constants for bake mode.
BAKE_MODE_FULL_BAKE_VALUE = 'full_bake'
BAKE_MODE_SMART_BAKE_VALUE = 'smart_bake'
BAKE_MODE_VALUES = [
    BAKE_MODE_FULL_BAKE_VALUE,
    BAKE_MODE_SMART_BAKE_VALUE,
]
BAKE_MODE_FULL_BAKE_LABEL = 'Full Bake'
BAKE_MODE_SMART_BAKE_LABEL = 'Smart Bake'
BAKE_MODE_LABELS = [
    BAKE_MODE_FULL_BAKE_LABEL,
    BAKE_MODE_SMART_BAKE_LABEL,
]

# Constants for rotate order mode.
ROTATE_ORDER_MODE_USE_EXISTING_VALUE = 'use_existing'
ROTATE_ORDER_MODE_XYZ_VALUE = 'xyz'
ROTATE_ORDER_MODE_YZX_VALUE = 'yzx'
ROTATE_ORDER_MODE_ZXY_VALUE = 'zxy'
ROTATE_ORDER_MODE_XZY_VALUE = 'xzy'
ROTATE_ORDER_MODE_YXZ_VALUE = 'yxz'
ROTATE_ORDER_MODE_ZYX_VALUE = 'zyx'
ROTATE_ORDER_MODE_VALUES = [
    ROTATE_ORDER_MODE_USE_EXISTING_VALUE,
    ROTATE_ORDER_MODE_XYZ_VALUE,
    ROTATE_ORDER_MODE_YZX_VALUE,
    ROTATE_ORDER_MODE_ZXY_VALUE,
    ROTATE_ORDER_MODE_XZY_VALUE,
    ROTATE_ORDER_MODE_YXZ_VALUE,
    ROTATE_ORDER_MODE_ZYX_VALUE
]
ROTATE_ORDER_MODE_USE_EXISTING_LABEL = 'Use Existing'
ROTATE_ORDER_MODE_XYZ_LABEL = 'XYZ'
ROTATE_ORDER_MODE_YZX_LABEL = 'YZX'
ROTATE_ORDER_MODE_ZXY_LABEL = 'ZXY'
ROTATE_ORDER_MODE_XZY_LABEL = 'XZY'
ROTATE_ORDER_MODE_YXZ_LABEL = 'YXZ'
ROTATE_ORDER_MODE_ZYX_LABEL = 'ZYX'
ROTATE_ORDER_MODE_LABELS = [
    ROTATE_ORDER_MODE_USE_EXISTING_LABEL,
    ROTATE_ORDER_MODE_XYZ_LABEL,
    ROTATE_ORDER_MODE_YZX_LABEL,
    ROTATE_ORDER_MODE_ZXY_LABEL,
    ROTATE_ORDER_MODE_XZY_LABEL,
    ROTATE_ORDER_MODE_YXZ_LABEL,
    ROTATE_ORDER_MODE_ZYX_LABEL,
]

# Default Values
DEFAULT_FRAME_RANGE_MODE = FRAME_RANGE_MODE_TIMELINE_INNER_VALUE
DEFAULT_FRAME_START = 1001
DEFAULT_FRAME_END = 1101
DEFAULT_BAKE_MODE = BAKE_MODE_FULL_BAKE_VALUE
DEFAULT_ROTATE_ORDER_MODE = ROTATE_ORDER_MODE_USE_EXISTING_VALUE
DEFAULT_DELETE_STATIC_ANIM_CURVES = 1

# Config files
CONFIG_FRAME_RANGE_MODE_KEY = 'mmSolver_reparent2_frameRangeMode'
CONFIG_FRAME_START_KEY = 'mmSolver_reparent2_frameStart'
CONFIG_FRAME_END_KEY = 'mmSolver_reparent2_frameEnd'
CONFIG_BAKE_MODE_KEY = 'mmSolver_reparent2_bakeMode'
CONFIG_ROTATE_ORDER_MODE_KEY = 'mmSolver_reparent2_rotateOrderMode'
CONFIG_DELETE_STATIC_ANIM_CURVES_KEY = 'mmSolver_reparent2_deleteStaticAnimCurves'
