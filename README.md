# sbc-closed-system-controller
When you need to throw a raspberry pi under water and control it over wifi

# Intro-Article
[boilerplate Raspberry Pi 5, 2 cameras, sensors and a webapp](https://dev.to/shnydercom/steal-my-boilerplate-rpi-5-2-cameras-sensors-webapp-3p55)

# List of code-inspiration
- [raspi-cam-srv](https://github.com/signag/raspi-cam-srv)
- [octoprint](https://github.com/OctoPrint/OctoPrint)


# Python newbie commands
- creating a virtual environment for python: `py -3 -m venv .venv`
- activating that virtual environment: `.venv\Scripts\activate`
- writing installed libraries in the venv to requirements: `pip freeze > requirements.txt`
- installing libraries mentioned in requirements.txt: `pip install -r requirements.txt`
- for VSCode completion over SSH on the RPi, change the python interpreter to the "global" one in the RPi, not the one in the venv
- detecting i2c: `i2cdetect -y 1`
- installing latest picamera2 from the repository: `pip install git+https://github.com/raspberrypi/picamera2.git@next`
- creating a symbolic link inside the static folder in the web server: ` ln -s ../../client-web-app/dist .`
- checking system messages, reasons for unexpected shutdowns: `journalctl -S -10m --system`
- running a web server on RPi startup: [RPi forums, pdf, section 4.4.4](https://forums.raspberrypi.com/viewtopic.php?t=314455)
- stopping the service: `systemctl stop rpi-boot-sbc-csc.service`
