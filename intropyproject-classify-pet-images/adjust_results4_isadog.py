#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adds dog/non-dog information to results_dic.

    Indexes:
        0 = pet label
        1 = classifier label
        2 = match
        3 = pet label is dog
        4 = classifier label is dog
    """

    dognames = set()

    with open(dogfile, "r") as file:
        for line in file:
            dognames.add(line.strip().lower())

    for key in results_dic:

        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        if pet_label in dognames:
            pet_is_dog = 1
        else:
            pet_is_dog = 0

        classifier_is_dog = 0

        classifier_labels = classifier_label.split(",")

        for label in classifier_labels:

            label = label.strip().lower()

            if label in dognames:
                classifier_is_dog = 1
                break

        results_dic[key].extend([pet_is_dog, classifier_is_dog])

    return None