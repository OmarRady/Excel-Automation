import os
import csv
import sys
from imp import reload

from openpyxl import Workbook

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    workbook = Workbook()
    worksheet = workbook.active
    with open('C:\\Users\\hu8OmarA\\Desktop\\20190429-0645.log', 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(',')):
                    cell = worksheet.cell(row=r+1, column=c+1)
                    cell.value = val
    workbook.save('output.xlsx')