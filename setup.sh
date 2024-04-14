python3 -m venv .venv --system-site-packages # arg is necessary for GPIO
. .venv/bin/activate 
pip install Flask
#python3 -m pip install pip gpiod
pip install adafruit-circuitpython-ina219
# 