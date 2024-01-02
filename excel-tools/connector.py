"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, ConnectorError

from . import operations
from .utils import *


class ExcelTools(Connector):

    def execute(self, config, operation, params, **kwargs):
        try:
            action = get_available_operations(operations, operation)
            return action(config, params)
        except Exception as Err:
            raise ConnectorError(Err)

    def check_health(self, config):
        try:
            operations.check_health(config)
        except Exception as Err:
            raise ConnectorError(Err)
