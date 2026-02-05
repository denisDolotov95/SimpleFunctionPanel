# -*- coding: utf-8 -*-
import pydantic


class ProductionConfig(pydantic.BaseModel):

    portainer: str = "https://192.168.0.110:9443"
    grafana: str = "http://192.168.0.110:3000"
    prometheus: str = "http://192.168.0.110:9090"
    rabbit_mq: str = "http://192.168.0.110:15672"
    psql_main: str = "postgresql+asyncpg://user:user@192.168.0.110:5432"
    psql_replica: str = "postgresql+asyncpg://user:user@192.168.0.110:5433"
    gate_api: str = "http://192.168.0.110:3501/docs"