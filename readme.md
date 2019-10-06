


# GraphQL
## Crear Usuario
``` 
mutation
{
  createUser(username:"juanber",email:"juanber2.0@gmail.com", password:"juanber", phone:"234234234") {
    user{
      id
      username
      email

    }
  }
}
```

## login

### request
``` 
mutation {
  tokenAuth(username:"admin", password:"admin") {
    token
  }
}
```

### response
```
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTcwMjk2NzU1LCJvcmlnSWF0IjoxNTcwMjk2NDU1fQ.ZC5CFlGJ-HK8l1dxKVqnxfliHXJHpvZQMvaFElMBY3I"
    }
  }
}
```



### ssh

ssh -i hackathon.pem ubuntu@3.82.66.35

### instalar virtualenv
sudo apt install virtualenv


### clonar repositorio
git clone  https://juanber:holamundo123@gitlab.com/dfinetec_hackathon/toyota.git

## entrar en la carpeta del proyecto
cd toyota


### crear entorno virtual
virtualenv -p python3 venv

### activar el entorno virtual
source venv/bin/activate

## instalar dependencias

```
pip install -r requirements.txt
```

## correr con el servidor de django
```
python manage.py runserver 0.0.0.0:8000
```

## Frontend
En el archivo `src/app/graphql.module.ts` 

```
apollo.create({
  link: httpLink.create({ uri: production}),
  cache: new InMemoryCache() as any
});
```
cambiar por 

```
apollo.create({
  link: httpLink.create({ uri: develop }),
  cache: new InMemoryCache() as any
});
```

# Servidor de Produccion 

## Archivos estaticos


```
python manage.py collectstatic
```


###INSTALAR nginx
sudo apt-get install nginx

###crear el archivo
sudo nano /etc/nginx/sites-available/toyota


```
server {
    listen 80;
    server_name 68.183.115.180;

    location = /home/ubuntu/toyota/staticfiles/favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /home/ubuntu/toyota/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/toyota/toyota.sock;
    }
}

```

###crear un enlace simbólico
sudo ln -s /etc/nginx/sites-available/toyota /etc/nginx/sites-enabled


### crear servicio

sudo nano /etc/systemd/system/toyota.service


```

[Unit]
Description=toyota gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/toyota
ExecStart=/home/ubuntu/toyota/venv/bin/gunicorn --access-logfile - --workers 3 \
--bind unix:/home/ubuntu/toyota/toyota.sock toyota.wsgi:application

[Install]
WantedBy=multi-user.target

```


sudo systemctl enable toyota

sudo systemctl start toyota

sudo service nginx restart


