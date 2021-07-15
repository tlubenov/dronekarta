
sudo cp dronekarta.service /etc/systemd/system/
sudo systemctl start dronekarta.service
sudo systemctl enable dronekarta.service
sudo systemctl restart dronekarta.service
sudo systemctl status dronekarta.service

