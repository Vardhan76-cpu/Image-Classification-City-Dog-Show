#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


def get_input_args():
    """
    Retrieves command line arguments.

    Returns:
        parse_args() - data structure that stores the command line arguments
    """

    parser = argparse.ArgumentParser(
        description="Classify pet images using a pretrained CNN."
    )

    parser.add_argument(
        '--dir',
        type=str,
        default='pet_images/',
        help='path to the folder containing pet images'
    )

    parser.add_argument(
        '--arch',
        type=str,
        default='vgg',
        help='CNN model architecture: resnet, alexnet, or vgg'
    )

    parser.add_argument(
        '--dogfile',
        type=str,
        default='dognames.txt',
        help='path to the file containing dog breed names'
    )

    return parser.parse_args()