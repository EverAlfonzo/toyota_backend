#!/bin/bash

PRO="toyota"

CURRENT_USER=$USER

source uninstall.sh

echo "Creando proyecto: $PRO.." 

sudo apt-get update  && \
sudo apt-get -y install virtualenv nginx

cd $HOME/$PRO

pwd

virtualenv -p python3 venv

PYTHON_HOME=$HOME/$PRO/venv/bin


$PYTHON_HOME/pip3 install -r requirements.txt


$PYTHON_HOME/python3 $HOME/$PRO/manage.py collectstatic --noinput


echo "
server {
    listen 80;
    server_name localhost 127.0.0.1;

    location = $HOME/$PRO/staticfiles/favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias $HOME/$PRO/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:$HOME/$PRO/$PRO.sock;
    }
}" >> $PRO.conf

sudo cp $PRO.conf /etc/nginx/sites-available/$PRO

sudo ln -s /etc/nginx/sites-available/$PRO /etc/nginx/sites-enabled


echo "
[Unit]
Description=$PRO gunicorn daemon
After=network.target

[Service]
User=$CURRENT_USER
Group=www-data
WorkingDirectory=$HOME/$PRO
ExecStart=$HOME/$PRO/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:$HOME/$PRO/$PRO.sock $PRO.wsgi:application

[Install]
WantedBy=multi-user.target

" >> $PRO.service

sudo cp $HOME/$PRO/$PRO.service /etc/systemd/system/


sudo systemctl enable $PRO

sudo systemctl start $PRO

sudo systemctl restart nginx





