# Beekeeper Manifest
The beekeeper manifest database is used to store the manifests of a node on the ecosystem.

## Docker-compose
Make a copy of the `.env.example` environment variables and modify to your needs:
```
cp .env.example .env
```

Start backend services (db + api):
```
docker-compose up --build
```

Make Django migrations:
```
docker exec -it manifest-api python manage.py makemigrations
docker exec -it manifest-api python manage.py migrate
```


Create superuser to login to `/admin/` page:
```
docker exec -it manifest-api python manage.py createsuperuser
```
The last command will prompt you for the admin username and password.

* Your Django server will run on `http://0.0.0.0:8000/`. Head over to your browser and enter `http://0.0.0.0:8000/admin` to access the admin page. Enter the account and password you created at the last step to log in.

## Initialize Sage node and sensor data
The purpose of the initialization process is to be easily load data into BK-Manifest and allow developers to easily standup their own instance of BK-Manifest based on their own node's metadata.