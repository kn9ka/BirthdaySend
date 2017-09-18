#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl, datetime

resultFileDest = 'path/to/destination-folder'
excelFile = r'''path/to/file'''


def readFromExcel(input_file, sheet_name = None):

    """
    How to write in file
    resultFile = open(resultFileDest + 'Test9999.csv', 'w')
    resultFile.write(pprint.pformat(countyData))
    resultFile.close()
    """

    countyData = {}
    wb = openpyxl.load_workbook(input_file, data_only = True)
    if sheet_name is None:
        sheet_name = 'list'
    sheet = wb.get_sheet_by_name(sheet_name)

# TODO: make name check for columns

    for row in range(2, sheet.max_row+1):
        employee_name = sheet['A' + str(row)].value
        employee_birthday = sheet['E' + str(row)].value
        countyData.update({employee_name: employee_birthday})

    print('Writing results...')
    print('Done.')

    return countyData