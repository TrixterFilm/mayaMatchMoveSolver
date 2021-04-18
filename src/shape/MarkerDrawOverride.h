/*
 * Copyright (C) 2021 David Cattermole.
 *
 * This file is part of mmSolver.
 *
 * mmSolver is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * mmSolver is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with mmSolver.  If not, see <https://www.gnu.org/licenses/>.
 * ====================================================================
 *
 */

#ifndef MM_MARKER_DRAW_OVERRIDE_H
#define MM_MARKER_DRAW_OVERRIDE_H

#include "MarkerShapeNode.h"

#include <maya/MString.h>
#include <maya/MColor.h>
#include <maya/MGlobal.h>
#include <maya/MPointArray.h>
#include <maya/MStreamUtils.h>
#include <maya/MEventMessage.h>

// Viewport 2.0
#include <maya/MPxDrawOverride.h>
#include <maya/MDrawRegistry.h>
#include <maya/MUserData.h>
#include <maya/MDrawContext.h>
#include <maya/MHWGeometryUtilities.h>

namespace mmsolver {

class MarkerDrawData : public MUserData {
public:
    MarkerDrawData()
            : MUserData(/*deleteAfterUse=*/ true) // let Maya clean up
            , m_depth_priority(0)
            , m_line_width(1.0)
            , m_point_size(1.0)
            , m_icon_size(1.0)
            , m_locked(false)
            , m_active(false)
            , m_draw_name(false)
    {}

    ~MarkerDrawData() override {
    }

    MString m_name;
    bool m_active;
    bool m_locked;
    float m_point_size;
    float m_line_width;
    float m_icon_size;
    MColor m_color{1.0f, 0.0f, 0.0f, 1.0f};
    bool m_draw_name;
    unsigned int m_depth_priority;

    MPointArray m_cross_line_list;
    MUintArray m_cross_line_index_list;

    MPointArray m_box_line_list;
    MUintArray m_box_line_index_list;
};

class MarkerDrawOverride : public MHWRender::MPxDrawOverride {
public:
    static MHWRender::MPxDrawOverride *Creator(const MObject &obj) {
        return new MarkerDrawOverride(obj);
    }

    ~MarkerDrawOverride() override;

    MHWRender::DrawAPI supportedDrawAPIs() const override;

    bool isBounded(
            const MDagPath &objPath,
            const MDagPath &cameraPath) const override;

    MBoundingBox boundingBox(
            const MDagPath &objPath,
            const MDagPath &cameraPath) const override;

    MUserData *prepareForDraw(
            const MDagPath &objPath,
            const MDagPath &cameraPath,
            const MHWRender::MFrameContext &frameContext,
            MUserData *oldData) override;

    bool hasUIDrawables() const override { return true; }

    void addUIDrawables(
            const MDagPath &objPath,
            MHWRender::MUIDrawManager &drawManager,
            const MHWRender::MFrameContext &frameContext,
            const MUserData *userData) override;

    bool traceCallSequence() const override {
        // Return true if internal tracing is desired.
        return false;
    }

    void handleTraceMessage(const MString &message) const override {
        MGlobal::displayInfo("MarkerDrawOverride: " + message);
        MStreamUtils::stdOutStream()
            << "MarkerDrawOverride: " << message.asChar() << '\n';
    }

private:
    MarkerDrawOverride(const MObject &obj);

    static void on_model_editor_changed_func(void *clientData);

    MarkerShapeNode *m_node;
    MCallbackId m_model_editor_changed_callback_id;
};

} // namespace mmsolver

#endif // MM_MARKER_DRAW_OVERRIDE_H
