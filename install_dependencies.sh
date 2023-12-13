#!/bin/bash

# Install system dependencies
sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install Python dependencies
pip install -r requirements.txt
