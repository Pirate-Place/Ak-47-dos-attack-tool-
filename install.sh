#!/bin/bash

# Display AK-47 logo
echo "======================"
echo "       AK-47         "
echo "   ,--,----,         "
echo "   |   |    |        "
echo "   |   |    |        "
echo "   |   |    |        "
echo "   '--'----'         "
echo "======================"

# Clear the screen
clear

# Request root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (using sudo)"
  exit
fi

# Install requirements
pip install -r requirements.txt

