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


## Docker hangs on npm install
If you are having trouble with docker hanging on `npm install`, you can try the following:
``` bash
docker-compose build --no-cache
docker-compose up
```
