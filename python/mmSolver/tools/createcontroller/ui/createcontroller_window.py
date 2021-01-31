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
Window for the Create Controller tool.

Usage::

   import mmSolver.tools.createcontroller.ui.createcontroller_window as window
   window.main()

"""

import mmSolver.ui.qtpyutils as qtpyutils
qtpyutils.override_binding_order()

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import mmSolver.logger
import mmSolver.ui.uiutils as uiutils
import mmSolver.ui.helputils as helputils
import mmSolver.ui.commonmenus as commonmenus
# import mmSolver.tools.createcontroller.constant as const
import mmSolver.tools.createcontroller.tool as tool
import mmSolver.tools.createcontroller.ui.createcontroller_layout as create_ctrl_layout


LOG = mmSolver.logger.get_logger()
baseModule, BaseWindow = uiutils.getBaseWindow()
WINDOW_TITLE = 'Create Controller'


def _open_help():
    src = helputils.get_help_source()
    page = 'tools_generaltools.html#create-controller'
    helputils.open_help_in_browser(page=page, help_source=src)
    return


class CreateController1Window(BaseWindow):
    name = 'CreateController1Window'

    def __init__(self, parent=None, name=None):
        super(CreateController1Window, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(create_ctrl_layout.CreateController1Layout)

        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowFlags(QtCore.Qt.Tool)

        # Standard Buttons
        self.baseHideStandardButtons()
        self.applyBtn.show()
        self.closeBtn.show()
        self.applyBtn.setText('Create')

        self.applyBtn.clicked.connect(tool.main)

        # Hide irrelevant stuff
        self.baseHideProgressBar()

        self.add_menus(self.menubar)
        self.menubar.show()

    def add_menus(self, menubar):
        edit_menu = QtWidgets.QMenu('Edit', menubar)
        commonmenus.create_edit_menu_items(
            edit_menu,
            reset_settings_func=self.reset_options)
        menubar.addMenu(edit_menu)

        help_menu = QtWidgets.QMenu('Help', menubar)
        commonmenus.create_help_menu_items(
            help_menu,
            tool_help_func=_open_help)
        menubar.addMenu(help_menu)

    def reset_options(self):
        form = self.getSubForm()
        form.reset_options()
        return


def main(show=True, auto_raise=True, delete=False):
    """
    Open the Smooth Keyframes UI window.

    :param show: Show the UI.
    :type show: bool

    :param auto_raise: If the UI is open, raise it to the front?
    :type auto_raise: bool

    :param delete: Delete the existing UI and rebuild it? Helpful when
                   developing the UI in Maya script editor.
    :type delete: bool

    :returns: A new solver window, or None if the window cannot be
              opened.
    :rtype: SolverWindow or None.
    """
    win = CreateController1Window.open_window(
        show=show,
        auto_raise=auto_raise,
        delete=delete
    )
    return win
