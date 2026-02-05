# -*- coding: utf-8 -*-
from fastapi import status
from fastapi.responses import HTMLResponse, RedirectResponse

from .. import utils

from .. import app, jinja_env, app_config

__all__ = ["main_panel"]


@app.get("/")
async def main():

    return RedirectResponse(url="/main_panel", status_code=status.HTTP_302_FOUND)


@app.get("/main_panel", response_class=HTMLResponse)
async def main_panel() -> str:

    html_tempalate_main_panel = jinja_env.get_template("main_panel.html")

    data = utils.AgregateData(**app_config.dict())
    portainer = await data.get_status_portainer()
    grafana = await data.get_status_grafana()
    gate_api = await data.get_status_gate_api()
    prometheus = await data.get_status_prometheus()
    psql_main = await data.get_status_psql("psql_main")
    psql_replica = await data.get_status_psql("psql_replica")
    rabbit_mq = await data.get_status_rabbit_mq()

    return html_tempalate_main_panel.render(
        page="main_panel",
        title="Main panel",
        portainer=portainer,
        grafana=grafana,
        gate_api=gate_api,
        prometheus=prometheus,
        psql_main=psql_main,
        psql_replica=psql_replica,
        rabbit_mq=rabbit_mq,
        logo_text="My panel",
    )


@app.get("/health", tags=["Health"])
async def health():

    return "i'm here"
