import pandas as pd
import re


#CONFIG
FILE_PATH = '<FILL_PATH>.csv'
COLS = ['additional_info', 'device_data']
ROOM_NUMBER_COL = 'search_text'



def rearrange_list(cols, value, x):
    index = cols.index(value)
    sublist = cols[index + 1:]
    return cols[:index+1] + sublist[len(sublist) - x:] + sublist[:-x]


def clean_cell(cell):
    cleaned_cell = re.sub(r'[{}" ]', '', cell).replace(',', ':')
    return cleaned_cell


def seperate_column(df, cols, i=0):
    for col in cols:
        df[col] = df[col].apply(clean_cell)
        i = (df[col][0]).count(':') + 1
        new_columns = df[col].str.split(':', expand=True)
        df = pd.concat([df, new_columns], axis=1)
        df.columns = list(df.columns[:-i]) + [f'{col}_{i}' for i in range(1, i+1)]
        df = df[rearrange_list(df.columns.tolist(), col, i)]
    return df.copy()


def get_room_number(df, col):
    df['room_number'] = df[col].str.extract(r'(\d{3})', expand=False)
    arr = df.columns.tolist()
    index = arr.index(col)
    return df[arr[:index+1] + [arr[-1]] + arr[index+1:-1]].copy()


mycsv = pd.read_csv(FILE_PATH)
df = pd.DataFrame(mycsv)
df = seperate_column(df, COLS)
df = get_room_number(df, ROOM_NUMBER_COL)
new_file_path = FILE_PATH[:-4] + '_cleaned.csv'
df.to_csv(new_file_path, index=False)
