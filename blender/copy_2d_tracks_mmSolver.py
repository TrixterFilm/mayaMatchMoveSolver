"""
Copy 2D Markers from Blender.

https://docs.blender.org/api/current/bpy.ops.clip.html

http://scummos.blogspot.com/2012/11/blender-exporting-camera-tracking.html
"""


from __future__ import print_function
import os
import bpy


def get_track_data(clip, track):
    data = {}

    # Clip
    clip.frame_start
    clip.frame_offset
    clip.frame_duration
    clip.fps
    clip.filepath
    clip.source # A sequence or movie file.

    # Camera
    cam = clip.tracking.camera
    cam.distortion_model # POLYNOMIAL or DIVISION
    cam.division_k1
    cam.division_k2
    cam.focal_length
    cam.focal_length_pixels
    cam.k1
    cam.k2
    cam.k3
    cam.pixel_aspect
    cam.principal
    cam.sensor_width
    cam.units # PIXELS or MILLIMETERS


    # Track
    framenum = 0
    active = track.active
    avg_err = track.average_error
    track.select
    track.name
    track.has_bundle
    track.hide
    track.lock
    track.weight
    bnd = track.bundle
    color = track.color

    # Markers (individual frames)
    markers = track.markers
    for mkr in markers:
        xy = mkr.co.xy
        mkr.frame
        mkr.is_keyed
        mkr.mute

    while framenum < clip.frame_duration:
        marker_at_frame = track.markers.find_frame(framenum)
        if marker_at_frame and not marker_at_frame.mute:
            # if marker_at_frame.is_keyed:
            #     cnt += 1
            coords = marker_at_frame.co.xy
        framenum += 1
    return


def get_clips_and_tracks():
    clips_and_tracks = []
    for clip in bpy.data.movieclips:
        for ob in clip.tracking.objects:
            object_name = ob.name
            for track in ob.tracks:
                clips_and_tracks.append((clip, track))
    return tracks


def get_temp_uv_file_path():
    return 'output.uv'


def main():
    file_name = get_temp_uv_file_path()
    clips_and_tracks = get_clips_and_tracks()

    track_data_list = {}
    for clip, track in clips_and_tracks:
        # width = clip.size[0]
        # height = clip.size[1]
        clip_name = clip.name
        track_name = track.name
        track_data = get_track_data(clip, track)
        track_data_list.append(track_data)

    data = {}
    data['tracks'] = track_data_list

    bpy.context.window_manager.clipboard = file_path

    # Encode text so it includes formating characters like a file read.
    encoded = clipboard.encode('utf8')
