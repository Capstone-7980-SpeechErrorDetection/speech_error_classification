"""
This script generates the labels for the training data. The labels are generated from a csv file that contains the
annotations for the training data. The annotations are in the form of a csv file with the following columns:
    - filename: the name of (.wav) audio file
    - event_label: the label of the event (speech error)
    - start_time: the start time of the event
    - end_time: the end time of the event
Each array represents a phrase in the audio file (padded to 10 seconds). The features are saved in a .npy file. The phrases are extracted from the audio file using
the timestamps provided in the transcript file generated by WhisperX. Each line in the transcript file contains the following information:
    - start: the start time of the audio segment
    - end: the end time of the audio segment
    - text: the text of the audio segment
The .csv file names must match the audio file names.
    
The labels are generated by checking if the audio file contains the event. If the audio file contains the event, the
label is set to 1, otherwise the label is set to 0.

The labels are saved in a .npy file.

Usage:
    python generate_labels.py --annotations_path <path_to_annotations> --audio_path <path_to_audio_files> --transcript_dir <path_to_transcript_directory> --output_dir <path_to_output_directory> --sr <sample_rate>
    
    - annotations_path: the path to the csv file containing the annotations
    - audio_path: the path to the directory containing the audio files
    - transcript_dir: the path to the directory containing the transcript files
    - output_dir: the path to the directory where the labels will be saved
    - sr: the sample rate of the audio files (default=16000)
    
Example:
    python generate_labels.py --annotations_path data/metadata/dataset.csv --audio_path data/audio --transcript_dir data/whipserX --output_dir data/labels --sr 16000
"""

import os
import argparse
import numpy as np