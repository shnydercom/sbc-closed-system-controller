# sbc-closed-system-controller
When you need to throw a raspberry pi under water and control it over wifi

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