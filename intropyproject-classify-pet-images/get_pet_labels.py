#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames
    of the image files.

    Parameters:
        image_dir - path to the folder containing pet images

    Returns:
        results_dic - dictionary containing image filenames
        and their corresponding pet labels
    """

    results_dic = {}

    filenames = listdir(image_dir)

    for filename in filenames:

        if filename.lower().endswith((".jpg", ".jpeg", ".png")):

            pet_label = filename[:filename.rfind("_")]

            pet_label = pet_label.replace("_", " ")

            pet_label = pet_label.lower().strip()

            results_dic[filename] = [pet_label]

    return results_dic