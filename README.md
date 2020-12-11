# Baghy
RaspberryPi code for controlling remotely a smart plug

I have used it for triggering a water fountain when a Infrared sensor detect Baghy (my cat) 
the final code is on tuya_IFR_rasp.py

On a Raspberry pi
Install miniconda: 
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh
sudo nano /home/pi/.bashrc. (add the path)
conda update conda
sudo chown -R pi miniconda3
conda config --add channels rpi
conda install python=3.6

update python3 to python 3.6:
This is not trivial, I don t remember how I did, maybe using berryconda
conda config --add channels rpi
conda install python=3.6

install Rpi.GPIO libraries:
conda update pip
pip install gpiozero
pip install RPi.GPIO

Follow instruction on tinytuya to control your devices using python:
https://pypi.org/project/tinytuya/
It will not work you don t change
d = tinytuya.OutletDevice('DEVICE_ID_HERE', 'IP_ADDRESS_HERE', 'LOCAL_KEY_HERE') 
as:
d = tinytuya.OutletDevice('DEVICE_ID_HERE', 'IP_ADDRESS_HERE', 'LOCAL_KEY_HERE’, 'device22')
d.set_dpsUsed({"1": None})

(Solution found in the questions of the tinytuya website)
see test.py for python control of the smart plug

The IP address is the IP that the device used, not the wifi ip.
you can check it 

Use a python interpreted at the beginning of your code
#!/usr/bin/env python3. (see tuya_IFR_rasp.py)
for tutorials on the sensor see http://freenove.com/fnk0020

use screen to let it go also after you exit ssh connection.
(sudo apt-get install screen)

On the screen terminal run your script on a bash loop that make it restart if there is an error:

until ./tuya_IFR_rasp.py; do sleep 10 echo 'ricomincio in 10 s'; done

