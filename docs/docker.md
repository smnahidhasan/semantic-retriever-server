# semantic-retriever-server

```commandline
docker build -t fastapi-app .
docker run -p 8000:8000 -v /path/on/host/logs:/var/log/fastapi fastapi-app
```

## See logs
```commandline
# Application logs
tail -f /path/on/host/logs/app.log

# Access logs
tail -f /path/on/host/logs/access.log

# Error logs
tail -f /path/on/host/logs/error.log

# Gunicorn logs
tail -f /path/on/host/logs/gunicorn_access.log
tail -f /path/on/host/logs/gunicorn_error.log
```

## Simple Run without Docker
```commandline
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```
Or,
```commandline
docker logs -f --tail <number_of_lines> <container_id_or_name>
```

## See Realtime Logs
```commandline
docker logs -f <container_id_or_name>
```