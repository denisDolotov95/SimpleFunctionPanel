Simple interface for our containers. If you want to check your services/data bases/monitors/queues.  
The flexible asynchronous FastAPI framework and the Jinja2 template engine make it so easy.

***

`config.py` — configuration module in which you specify the services that should be monitored.

By default the panel uses the following endpoints (old hard‑coded values):

- **PANEL_PORTAINER**: `https://192.168.0.110:9443`
- **PANEL_PORTAINER_2**: `https://85.208.85.181:9443`
- **PANEL_GRAFANA**: `http://192.168.0.110:3000`
- **PANEL_PROMETHEUS**: `http://192.168.0.110:9090`
- **PANEL_RABBIT_MQ**: `http://192.168.0.110:15672`
- **PANEL_PSQL_MAIN**: `postgresql+asyncpg://user:user@192.168.0.110:5432`
- **PANEL_PSQL_REPLICA**: `postgresql+asyncpg://user:user@192.168.0.110:5433`
- **PANEL_GATE_API**: `http://192.168.0.110:3501/docs`

You can override any of them via environment variables before starting the app or container, for example:

```bash
export PANEL_PORTAINER="https://my-portainer:9443"
export PANEL_GRAFANA="http://grafana.internal:3000"
uvicorn app:app --reload
```

or in `docker-compose.yml`:

```yaml
services:
  web_function_panel:
    environment:
      - PANEL_PORTAINER=https://my-portainer:9443
      - PANEL_GRAFANA=http://grafana.internal:3000
```

***

Check in on your own machine:

```bash
uvicorn app:app --reload
```

Deployment on your docker host (image must be in the registry `localhost:5000`):

```bash
docker compose up -d
```

If you have Gitlab CI/CD then there's a `.gitlab-ci.yml` file.

***

![Main panel](MainPage.png)

***
