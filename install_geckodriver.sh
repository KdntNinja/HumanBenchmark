#!/bin/bash

# Define the version of geckodriver to install
GECKODRIVER_VERSION="v0.33.0"

# Download geckodriver
echo "Downloading geckodriver..."
wget "https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz" -O /tmp/geckodriver.tar.gz

# Extract the downloaded file
echo "Extracting geckodriver..."
tar -xzf /tmp/geckodriver.tar.gz -C /tmp

# Move geckodriver to /usr/local/bin
echo "Installing geckodriver..."
sudo mv /tmp/geckodriver /usr/local/bin/geckodriver

# Set executable permissions
sudo chmod +x /usr/local/bin/geckodriver

# Clean up
echo "Cleaning up..."
sudo rm /tmp/geckodriver.tar.gz

# Verify installation
echo "Verifying geckodriver installation..."
if command -v geckodriver &> /dev/null
then
    echo "geckodriver installed successfully"
else
    echo "geckodriver installation failed"
    exit 1
fi
