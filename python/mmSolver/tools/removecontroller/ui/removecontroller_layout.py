# Copyright (C) 2021 David Cattermole
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
The main component of the user interface for the remove controller window.
"""

import mmSolver.ui.qtpyutils as qtpyutils
qtpyutils.override_binding_order()

import Qt.QtWidgets as QtWidgets

import mmSolver.logger
import mmSolver.utils.configmaya as configmaya
import mmSolver.tools.createcontroller.constant as create_ctrl_const
# import mmSolver.tools.removecontroller.constant as const
import mmSolver.tools.removecontroller.ui.ui_removecontroller_layout as ui_layout


LOG = mmSolver.logger.get_logger()


class RemoveController1Layout(QtWidgets.QWidget, ui_layout.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(RemoveController1Layout, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Bake Options
        bake_mode_labels = create_ctrl_const.BAKE_MODE_LABEL_LIST
        self.bakeModeComboBox.addItems(bake_mode_labels)
        self.bakeModeComboBox.currentIndexChanged.connect(
            self.bakeModeIndexChanged
        )

        # Populate the UI with data
        self.populateUi()

    def bakeModeIndexChanged(self, index):
        name = create_ctrl_const.CONFIG_BAKE_MODE_KEY
        value = create_ctrl_const.BAKE_MODE_VALUE_LIST[index]
        configmaya.set_scene_option(name, value, add_attr=True)
        LOG.debug('key=%r value=%r', name, value)

    def reset_options(self):
        name = create_ctrl_const.CONFIG_BAKE_MODE_KEY
        value = create_ctrl_const.DEFAULT_BAKE_MODE
        configmaya.set_scene_option(name, value)
        LOG.debug('key=%r value=%r', name, value)

        self.populateUi()

    def populateUi(self):
        """
        Update the UI for the first time the class is created.
        """
        name = create_ctrl_const.CONFIG_BAKE_MODE_KEY
        value = configmaya.get_scene_option(
            name,
            default=create_ctrl_const.DEFAULT_BAKE_MODE)
        index = create_ctrl_const.BAKE_MODE_VALUE_LIST.index(value)
        label = create_ctrl_const.BAKE_MODE_LABEL_LIST[index]
        LOG.debug('key=%r value=%r label=%r', name, value, label)
        self.bakeModeComboBox.setCurrentText(label)
        return
