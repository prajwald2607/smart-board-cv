#!/bin/bash

# Install system dependencies
sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx

# Install Python dependencies
pip install -r requirements.txt
