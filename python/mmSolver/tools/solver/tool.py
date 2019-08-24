# Copyright (C) 2018, 2019 David Cattermole.
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
The Solver UI tool.
"""

import mmSolver.logger
import mmSolver.api as mmapi
import mmSolver.tools.solver.lib.collection as lib_col
import mmSolver.tools.solver.lib.state as lib_state
import mmSolver.tools.solver.ui.solver_window as solver_window


LOG = mmSolver.logger.get_logger()


def run_solve(override_current_frame=None):
    """
    Run the solver for the active collection.

    If the Solver UI is found, the window will update and show
    progress messages.

    This function is strongly dependant on the Solver UI.
    The following state information is set via the Solver UI.

    - Active Collection
    - Log Level
    - Refresh Viewport

    :param override_current_frame: Before running the solver, change
                                   the "override current frame" state to
                                   this value.
    :type override_current_frame: bool
    """
    assert (override_current_frame is None
            or isinstance(override_current_frame, bool))

    col = lib_state.get_active_collection()
    if col is None:
        msg = 'No active Collection found. Skipping solve.'
        LOG.warning(msg)
        return
    force_update_state = lib_state.get_force_dg_update_state()
    refresh_state = lib_state.get_refresh_viewport_state()
    log_level = lib_state.get_log_level()
    do_isolate_state = lib_state.get_isolate_object_while_solving_state()
    image_plane_state = lib_state.get_display_image_plane_while_solving_state()

    layout = None
    win = solver_window.SolverWindow.get_instance()
    if win is None:
        msg = 'Could not get window.'
        LOG.warning(msg)
    else:
        layout = win.getSubForm()

    # Set value.
    prev_value = None
    if override_current_frame is not None:
        prev_value = lib_col.get_override_current_frame_from_collection(col)
        if layout is None:
            lib_col.set_override_current_frame_on_collection(
                col,
                override_current_frame
            )
        else:
            # The function should operate on the currently active
            # collection, so we don't need to pass a collection.
            layout.setOverrideCurrentFrame(col, override_current_frame)

    # Run Solver
    options = mmapi.createExecuteOptions(
        refresh=refresh_state,
        force_update=force_update_state,
        do_isolate=do_isolate_state,
        display_image_plane=image_plane_state
    )
    lib_col.run_solve_ui(
        col,
        options,
        log_level,
        win,
    )

    # Restore previous value.
    if override_current_frame is not None:
        if layout is None:
            lib_col.set_override_current_frame_on_collection(
                col,
                prev_value
            )
        else:
            layout.setOverrideCurrentFrame(col, prev_value)
    return


def run_solve_on_current_frame():
    """
    Run the solver, forcing 'Override Current Frame' on.
    """
    run_solve(override_current_frame=True)
    return


def run_solve_on_all_frames():
    """
    Run the solver, forcing 'Override Current Frame' off.
    """
    run_solve(override_current_frame=False)
    return


def open_window():
    """
    Open the Solver UI window.
    """
    solver_window.main()
    return
