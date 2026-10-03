#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function,
    compares pet labels to classifier labels,
    and adds both the classifier label and match result
    to the results dictionary.
    """

    for key in results_dic:

        # Create the full path to the image
        image_path = images_dir + key

        # Get the classifier label
        model_label = classifier(image_path, model)

        # Format classifier label
        model_label = model_label.lower().strip()

        # Get the pet image label
        pet_label = results_dic[key][0]

        # Add classifier label to the results dictionary
        results_dic[key].append(model_label)

        # Compare pet label with classifier label
        if pet_label in model_label:
            results_dic[key].append(1)
        else:
            results_dic[key].append(0)

    return None