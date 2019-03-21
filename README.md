# Requirements

Python 3.5+

node v10.13.0+

# install

Unicorn Hat driver : https://github.com/pimoroni/unicorn-hat

pip install websocket_client

# Running

sudo node app.js
sudo python py/customizable.py

# Running as Service

cd /etc/systemd/system/
sudo cp /home/pi/Documents/GitHub/ty-pi-light/*.service /etc/systemd/system
sudo systemctl enable ty-pi-light-api.service
sudo systemctl enable ty-pi-light-customizable.service

sudo systemctl start ty-pi-light-api.service
sudo systemctl start ty-pi-light-customizable.service

sudo systemctl stop ty-pi-light-api.service
sudo systemctl stop ty-pi-light-customizable.service

sudo systemctl disable ty-pi-light-api.service
sudo systemctl disable ty-pi-light-customizable.service
