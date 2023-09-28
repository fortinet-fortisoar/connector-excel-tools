import importlib
import re
from connectors.core.connector import ConnectorError
from .utils import *

def read_sheet(config, params):
    json_data = []
    use_column_title = params.get('use_column_title', None)
    try:
        workbook = load_workbook(params)
        sheet = workbook['sheet']
        rows = sheet.max_row
        columns = sheet.max_column
        
        for i in range(1, rows+1):
            row = {}
            for j in range(1, columns+1):
                if use_column_title:
                    if i == 1:
                        continue
                    row.update(
                        {
                            sheet.cell(row=1, column=j).value: sheet.cell(row=i, column=j).value
                        }
                    )
                else:
                    row.update(
                        {
                            sheet.cell(row=i, column=j).coordinate: sheet.cell(row=i, column=j).value
                        }
                    )
            if row:
                json_data.append(row)

        cleanup(workbook)
        return json_data

    except Exception as err:
        logger.exception('Read Excel sheet data Error: {0}'.format(err))
        raise ConnectorError('Read Excel sheet data Error: {0}'.format(err))    


def list_sheets(config, params):
    try:
        workbook = load_workbook(params)
        sheet_names = workbook['workbook'].sheetnames
        cleanup(workbook)
        return sheet_names
    
    except Exception as err:
        logger.exception('List Sheets Error: {0}'.format(err))
        raise ConnectorError('List Sheets Error: {0}'.format(err))


def read_column_by_name(config, params):
    '''input: Column letter or columns header name (1st row), Ouput: columns'''
    try:
        workbook = load_workbook(params)
        sheet = workbook['sheet']
        column_name = params.get('column_name')
        if re.match('^[A-Z]{1,2}$', column_name): # Matches a typical excel column letter(s)
            column = [{entry.coordinate:entry.value} for entry in sheet[column_name]]
        else:
            headers = []
            for cell in sheet[1]:
                if cell.value == column_name:
                    column = [{entry.coordinate:entry.value} for entry in sheet[cell.coordinate[0]]]
        cleanup(workbook)
        return column

    except Exception as err:
        logger.exception('Read the column content by name Error: {0}'.format(err))
        raise ConnectorError('Read the column content by name Error: {0}'.format(err))


def update_cell(config, params):
    try:
        cell_id = params.get('cell_id')
        cell_value = params.get('cell_value')
        workbook = load_workbook(params)
        sheet = workbook['sheet']        
        sheet[cell_id] = cell_value
        #TODO upload new file to cyops
    except Exception as err:
        logger.exception('Could not update cell: {}'.format(err))
        raise ConnectorError('Could not update cell: {}'.format(err))


def check_health(config):
    try:
        import importlib.util
        spam_spec = importlib.util.find_spec("openpyxl")
        if spam_spec is not None:
            return True
        else:
            logger.exception('Python module(s) not found')
            raise ConnectorError('Python module(s) not found')
    except Exception as err:
        logger.exception('Python module(s) not found. {}'.format(err))
        raise ConnectorError('Python module(s) not found. {}'.format(err))