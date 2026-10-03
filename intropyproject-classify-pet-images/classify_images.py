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

        # Classify the image
        model_label = classifier(images_dir + key, model)

        # Convert classifier label to lowercase
        model_label = model_label.lower().strip()

        # Get the actual pet label
        truth = results_dic[key][0]

        # Check whether the pet label appears in the classifier labels
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])

    return None