# LiptoSpeech
Lip reading using End to End Sentence Level Model

## Problem Statement:

Lipreading is the task of decoding text from the movement of a speaker’s mouth.
Traditional approaches separated the problem into two stages: designing or learning visual features, and prediction

    Input : A Video file of a person speaking some word or phrase.
    Output : The predicted word or phrase the person was speaking.

## Dataset:
   GRID-Corpus - http://spandh.dcs.shef.ac.uk/gridcorpus/
   LRW - https://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrw1.html

## Technologies and frameworks:
    - Tensorflow1.2.1
    - Keras
    - Opencv3
    - python 3.6

## Preprocess the dataset:
    python Videoprocess.py id2_vcd_swwp2s.mpg
    
Dlib Predictor Model is used to landmark the facial points which can be found in predictor directory
``predictor/shape_predictor_68_face_landmarks.dat.bz2``

MouthExtract folder contains the preprocessed dataset
