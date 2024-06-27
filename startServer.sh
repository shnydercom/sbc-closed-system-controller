. .venv/bin/activate
cd ./control-web-server
# https://unix.stackexchange.com/questions/170572/what-is-in-a-shell-script
fastapi run main.py --host=0.0.0.0 &>> lastLog.txt  