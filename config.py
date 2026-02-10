#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application configuration.

Все значения могут переопределяться переменными окружения.
См. README для списка поддерживаемых переменных.
"""

import os

import pydantic


class ProductionConfig(pydantic.BaseModel):
    """Production configuration with environment overrides.

    Каждое поле можно переопределить переменной окружения PANEL_<NAME>, например:

        export PANEL_PORTAINER=https://my-portainer:9443
    """

    portainer: str = os.getenv("PANEL_PORTAINER", "https://192.168.0.110:9443")
    portainer_2: str = os.getenv("PANEL_PORTAINER_2", "https://85.208.85.181:9443")
    grafana: str = os.getenv("PANEL_GRAFANA", "http://192.168.0.110:3000")
    prometheus: str = os.getenv("PANEL_PROMETHEUS", "http://192.168.0.110:9090")
    rabbit_mq: str = os.getenv("PANEL_RABBIT_MQ", "http://192.168.0.110:15672")
    psql_main: str = os.getenv(
        "PANEL_PSQL_MAIN", "postgresql+asyncpg://user:user@192.168.0.110:5432"
    )
    psql_replica: str = os.getenv(
        "PANEL_PSQL_REPLICA", "postgresql+asyncpg://user:user@192.168.0.110:5433"
    )
    gate_api: str = os.getenv("PANEL_GATE_API", "http://192.168.0.110:3501/docs")
