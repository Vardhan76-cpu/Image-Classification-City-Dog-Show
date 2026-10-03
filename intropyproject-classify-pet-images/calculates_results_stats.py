#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculates_results_stats(results_dic):
    """
    Calculates statistics based on the results dictionary.

    Indexes:
        0 = pet label
        1 = classifier label
        2 = match
        3 = actual pet is dog
        4 = classifier says dog
    """

    results_stats = {}

    # Total number of images
    n_images = len(results_dic)

    results_stats["n_images"] = n_images

    n_dogs_img = 0
    n_notdogs_img = 0

    n_correct_dogs = 0
    n_correct_notdogs = 0

    n_correct_breed = 0

    for key in results_dic:

        # Actual image is a dog
        if results_dic[key][3] == 1:

            n_dogs_img += 1

            # Classifier correctly identifies dog/not-dog
            if results_dic[key][4] == 1:
                n_correct_dogs += 1

            # Breed classification is correct
            if results_dic[key][2] == 1:
                n_correct_breed += 1

        # Actual image is not a dog
        else:

            n_notdogs_img += 1

            # Classifier correctly identifies not-dog
            if results_dic[key][4] == 0:
                n_correct_notdogs += 1

    results_stats["n_dogs_img"] = n_dogs_img
    results_stats["n_notdogs_img"] = n_notdogs_img

    results_stats["n_correct_dogs"] = n_correct_dogs
    results_stats["n_correct_notdogs"] = n_correct_notdogs
    results_stats["n_correct_breed"] = n_correct_breed

    # Percentage of correctly classified dogs
    if n_dogs_img > 0:

        results_stats["pct_correct_dogs"] = (
            n_correct_dogs / n_dogs_img
        ) * 100.0

        results_stats["pct_correct_breed"] = (
            n_correct_breed / n_dogs_img
        ) * 100.0

    else:

        results_stats["pct_correct_dogs"] = 0.0
        results_stats["pct_correct_breed"] = 0.0

    # Percentage of correctly classified non-dogs
    if n_notdogs_img > 0:

        results_stats["pct_correct_notdogs"] = (
            n_correct_notdogs / n_notdogs_img
        ) * 100.0

    else:

        results_stats["pct_correct_notdogs"] = 0.0

    # Overall correct classifications
    n_correct = (
        n_correct_dogs +
        n_correct_notdogs
    )

    results_stats["n_correct"] = n_correct

    results_stats["n_incorrect"] = (
        n_images - n_correct
    )

    # Overall percentage
    if n_images > 0:

        results_stats["pct_correct"] = (
            n_correct / n_images
        ) * 100.0

    else:

        results_stats["pct_correct"] = 0.0

    return results_stats