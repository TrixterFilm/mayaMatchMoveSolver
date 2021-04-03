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
 * A full-screen quad render, with a shader applied.
 */

#ifndef MAYA_MM_SOLVER_MM_RENDERER_QUAD_RENDER_H
#define MAYA_MM_SOLVER_MM_RENDERER_QUAD_RENDER_H

#include <maya/MString.h>
#include <maya/MViewport2Renderer.h>
#include <maya/MRenderTargetManager.h>

namespace mmsolver {
namespace renderer {

class MMRendererQuadRender : public MHWRender::MQuadRender {
public:
    // TODO: Remove the shader creation and make the caller pass over
    // some owned memory to this class to then release on destruction.
    MMRendererQuadRender(const MString &name,
                         const MString &id,
                         const MString &technique);
    ~MMRendererQuadRender() override;

    const MHWRender::MShaderInstance *shader() override;
    MHWRender::MClearOperation &clearOperation() override;

    MHWRender::MRenderTarget* const* targetOverrideList(unsigned int &listSize) override;

    void
    setRenderTargets(MHWRender::MRenderTarget **targets,
                     const uint32_t index,
                     const uint32_t count) {
        m_targets = targets;
        m_target_index = index;
        m_target_count = count;
    }

    const MFloatPoint & viewRectangle() const {
        return m_view_rectangle;
    }

    void setViewRectangle(const MFloatPoint & rect) {
        m_view_rectangle = rect;
    }

    uint32_t clearMask() {
        return m_clear_mask;
    }

    void setClearMask(const uint32_t clear_mask) {
        m_clear_mask = clear_mask;
    }

protected:

    // Shader to use for the quad render
    MHWRender::MShaderInstance *m_shader_instance;

    // Shader file name
    MString m_effect_id;

    // Shader 'technique' name.
    MString m_effect_id_technique;

    // Targets used as input parameters to mShaderInstance;
    MHWRender::MRenderTarget** m_targets;

    // The index (and count) into the m_targets list of pointers. We
    // are able to give the exact targets.
    uint32_t m_target_index;
    uint32_t m_target_count;

    // View rectangle
    MFloatPoint m_view_rectangle;

    // How the clear operation works?
    uint32_t m_clear_mask;
};

} // namespace renderer
} // namespace mmsolver

#endif //MAYA_MM_SOLVER_MM_RENDERER_QUAD_RENDER_H
