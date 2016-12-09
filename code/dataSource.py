import xlrd
import re


data_base_path = '../data/population-migration-all/'


def get_files(file_path):
    result = []

    work_book = xlrd.open_workbook(file_path)
    first_table = work_book.sheet_by_index(0)
    cols = first_table.ncols

    title_row = first_table.row_values(0)
    source_col_index = title_row.index('来源')
    for i in range(first_table.nrows):
        row_values = first_table.row_values(i)
        if row_values[source_col_index] == '中华人民共和国人口统计资料汇编':
            result.append(row_values[cols - 1])

    return result


def get_file_content(file_path):
    work_book = xlrd.open_workbook(file_path)
    table = work_book.sheet_by_index(0)

    area = get_area(table.row_values(0, 0, 1)[0])[0]

    data_list = []

    for i in range(7, table.nrows):
        year = table.row_values(i, 0, 1)[0]
        if year.isdigit():
            data_list.append(table.row_values(i))

    return area, data_list


def get_area(line):
    return re.findall(r'年(.*?)历年', line, re.U | re.I)
