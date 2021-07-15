
sudo cp dronekarta.service /etc/systemd/system/
sudo systemctl start dronekarta.service
sudo systemctl enable dronekarta.service
sudo systemctl restart dronekarta.service

sudo cp dronekarta /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/dronekarta /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'


