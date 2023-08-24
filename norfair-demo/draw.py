import numpy as np
import cv2

import norfair


def draw(
    paths_drawer,
    track_points,
    frame,
    detections,
    tracked_objects,
    coord_transformations,
    fix_paths,
):
    if track_points == "centroid":
        norfair.draw_points(frame, detections, color_by_label=True)
        norfair.draw_tracked_objects(frame, tracked_objects, color_by_label=True)
    elif track_points == "bbox":
        if len(tracked_objects) > 0:
            cv2.imwrite("test.jpg", frame)
        norfair.draw_boxes(frame, detections, color_by_label=True)
        norfair.draw_tracked_boxes(frame, tracked_objects, color_by_label=True)
        if len(tracked_objects) > 0:
            cv2.imwrite("test2.jpg", frame)
            for i in tracked_objects:
                print(i.label)
            print("haaa")

    if fix_paths:
        frame = paths_drawer.draw(frame, tracked_objects, coord_transformations)
    elif paths_drawer is not None:
        frame = paths_drawer.draw(frame, tracked_objects)

    return frame


def center(points):
    return [np.mean(np.array(points), axis=0)]
