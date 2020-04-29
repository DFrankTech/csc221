#1/usr/env python3

# census.py - Tabulate population numbers of census data fro each county
# Built-in Mods
import  pprint
import logging
from pathlib import Path
import argparse
# 3rd Party Mods
import openpyxl

# log = logging.getLogger(__name__) or

def get_census_sheet(path):
    logging.info(f'Loading Excel workbook: {path}')
    wb = openpyxl.load_workbook(str(path))

    return wb['Population by Census Tract']

def get_county_data(sheet):
    data = {}
    '''Logging through root logging'''
    logging.info('Reading rows...')
    for row in range(2, sheet.max_row + 1):
        '''Each row in spreadsheet has data for one census tract'''
        state = sheet[f'B{row}'].value
        county = sheet[f'C{row}'].value
        pop = sheet[f'D{row}'].value
        data.setdefault(state, {}).setdefault(county, {
            'tracts': 0, 'pop':0
        }) #or data[state]
        data[state][county]['tracts'] += 1
        data[state][county]['pop'] += int(pop)
    return data

def output_data(data):
    path = Path('census2010.py')
    logging.info(f'Writing out census python module: {path}')
    path.write_text(f'data = {pprint.pformat(data)}')

def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    sheet = get_census_sheet(args.path)
    data = get_county_data(sheet)
    output_data(data)

if __name__ == '__main__':
    main()
