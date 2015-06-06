#!/bin/bash

# Install OS dependencies
apt-get -y install sudo make git build-essential vim python-dev python-pip

# Install WiringBP
git clone https://github.com/LeMaker/WiringBP.git -b bananapi
cd WiringBP
chmod +x ./build
sudo ./build
cd -

# Install RPi.GPIO_BP
git clone https://github.com/LeMaker/RPi.GPIO_BP -b bananapi
cd RPi.GPIO_BP
python setup.py install
sudo python setup.py install
cd -
