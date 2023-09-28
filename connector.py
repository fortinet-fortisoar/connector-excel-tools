from connectors.core.connector import Connector
from .utils import *
from . import operations


class ExcelTools(Connector):

    def execute(self, config, operation, params, **kwargs):
        action = get_available_operations(operations, operation)
        return action(config, params)

    def check_health(self, config):
        operations.check_health(config)
