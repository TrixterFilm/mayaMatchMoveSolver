/*
 * Copyright (C) 2018, 2019 David Cattermole.
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
 * This file lists the Node Type IDs used in the MM Solver project.
 * All node types must listed here.
 *
 * From the Maya documentation:
 *
 * In Maya, both intrinsic and user-defined Maya Objects are registered and
 * recognized by their type identifier or type id. The basis of the type id
 * system is a tag which is used at run-time to determine how to create and
 * destroy Maya Objects, and how they are to be input/output from/to files.
 * These tag-based identifiers are implemented by the class MTypeId.
 * Use the MTypeId class to create, copy and query Maya Object type identifiers.
 * It is very important to note that these ids are written into the Maya binary
 * file format. So, once an id is assigned to a node or data type it can never
 * be changed while any existing Maya file contains an instance of that node
 * or data type. If a change is made, such files will become unreadable.
 *
 * Thus, even though we provide a range of reserved ids that you can use for
 * internal plug-ins, Autodesk highly recommends that you obtain a globally
 * unique id range (see below) and use ids from this range for all your
 * plug-ins, even internal ones. This can prevent significant headaches later if
 * the plans for your plug-ins change.
 *
 * There are 2 forms of the constructor for this class that can be used depending
 * on whether the plug-in id is internal or globally unique.
 *
 * For plug-ins that will forever be internal to your site use the constructor
 * that takes a single unsigned int parameter. The numeric range 0 - 0x7ffff (524288 ids)
 * has been reserved for such plug-ins.
 *
 * The example plug-ins provided with Maya in the plug-in development kit will
 * use ids in the range 0x80000 - 0xfffff (524288 ids). If you customize one
 * of these example plug-ins, you should change the id to avoid future conflicts.
 *
 * Plug-ins that are intended to be shared between sites will need to have a
 * globally unique id. The Autodesk Developer Network (ADN) will provide such
 * id's in blocks of 256. You will be assigned one or more 24-bit prefixes.
 * Once this has been obtained, used the MTypeId constructor that takes 2
 * unsigned int parameters. The prefix goes in the first parameter, and you
 * are responsible for managing the allocation of the 256 ids that go into
 * the second parameter.
 *
 */

#ifndef MM_SOLVER_NODE_TYPE_IDS_H
#define MM_SOLVER_NODE_TYPE_IDS_H

#define MM_MARKER_SCALE_TYPE_ID 0x0012F180
#define MM_MARKER_SCALE_TYPE_NAME "mmMarkerScale"

#define MM_REPROJECTION_TYPE_ID 0x0012F181
#define MM_REPROJECTION_TYPE_NAME "mmReprojection"

#define MM_MARKER_GROUP_TRANSFORM_TYPE_ID 0x0012F182
#define MM_MARKER_GROUP_TRANSFORM_TYPE_NAME "mmMarkerGroupTransform"
#define MM_MARKER_GROUP_DRAW_CLASSIFY "drawdb/geometry/transform"

#define MM_SKY_DOME_SHAPE_TYPE_ID 0x0012F195
#define MM_SKY_DOME_SHAPE_TYPE_NAME "mmSkyDomeShape"
#define MM_SKY_DOME_DRAW_CLASSIFY "drawdb/geometry/mmSolver/skyDome"
#define MM_SKY_DOME_DRAW_REGISTRANT_ID "mmSkyDomeNodePlugin"
#define MM_SKY_DOME_SHAPE_SELECTION_TYPE_NAME "mmSkyDomeShapeSelection"
#define MM_SKY_DOME_SHAPE_DISPLAY_FILTER_NAME "mmSkyDomeDisplayFilter"
#define MM_SKY_DOME_SHAPE_DISPLAY_FILTER_LABEL "MM SkyDome"

#define MM_MARKER_SHAPE_TYPE_ID 0x0012F196
#define MM_MARKER_SHAPE_TYPE_NAME "mmMarkerShape"
#define MM_MARKER_DRAW_CLASSIFY "drawdb/geometry/mmSolver/marker"
#define MM_MARKER_DRAW_REGISTRANT_ID "mmMarkerNodePlugin"
#define MM_MARKER_SHAPE_SELECTION_TYPE_NAME "mmMarkerShapeSelection"
#define MM_MARKER_SHAPE_DISPLAY_FILTER_NAME "mmMarkerDisplayFilter"
#define MM_MARKER_SHAPE_DISPLAY_FILTER_LABEL "MM Marker"

#define MM_BUNDLE_SHAPE_TYPE_ID 0x0012F197
#define MM_BUNDLE_SHAPE_TYPE_NAME "mmBundleShape"
#define MM_BUNDLE_DRAW_CLASSIFY "drawdb/geometry/mmSolver/bundle"
#define MM_BUNDLE_DRAW_REGISTRANT_ID "mmBundleNodePlugin"
#define MM_BUNDLE_SHAPE_SELECTION_TYPE_NAME "mmBundleShapeSelection"
#define MM_BUNDLE_SHAPE_DISPLAY_FILTER_NAME "mmBundleDisplayFilter"
#define MM_BUNDLE_SHAPE_DISPLAY_FILTER_LABEL "MM Bundle"

#endif // MM_SOLVER_NODE_TYPE_IDS_H
