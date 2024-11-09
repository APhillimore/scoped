# Scoped
Simple, Opinionated planning tool.

## Development
A docker-compose file is provided for development purposes.

Running the following command will build and run the database, api and app containers.
``` bash
cd .dev
docker-compose up
```

The API will be available at http://localhost:8000.
The app will be available at http://localhost:5173.


## Access a running container
``` bash
docker exec -it <container_id> /bin/bash
```

### App
Sometimes you need to access the app container to run commands like `npm install` instead of having to rebuild the container.
``` bash
docker exec -it scoped-app /bin/bash
```

### API
Sometimes you need to access the api container to run commands like `python manage.py migrate` or `python manage.py createsuperuser` or `python manage.py startapp <app_name>`.
``` bash
docker exec -it scoped-api /bin/bash
```

## Docker hangs on npm install
If you are having trouble with docker hanging on `npm install`, you can try the following:
``` bash
docker-compose build --no-cache
docker-compose up
```

