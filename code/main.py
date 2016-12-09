import pickle
import pandas as pd
from os import walk, makedirs, path
from os.path import basename, splitext

from dataSource import get_files, get_file_content, data_base_path

province_path = 'caches/by_province/'
year_path = 'caches/by_year/'


# 按省份来保存每年的人口数据
def save_by_province():
    files = get_files(data_base_path + 'migr-agenda.xls')
    columns = ['year', 'avg_num', 'in_num', 'in_rate', 'out_num', 'out_rate', 'net_in', 'net_in_rate']
    for i in range(files.__len__()):
        area, data_list = get_file_content(data_base_path + files[i] + '.xls')

        frame = pd.DataFrame(data_list, columns=columns)
        if path.exists(province_path) is False:
            makedirs(province_path)
        with open(province_path + area + '.pickle', 'wb') as f:
            pickle.dump(frame, f)


# 按年份来保存每个省得人口数据，需要依赖按照省来分类的数据
def save_by_year():
    years = load_years()
    year_data = []

    for i in range(years.__len__()):
        year_data.append({
            "year": years[i],
            "datas": []
        })

    for (dirpath, dirnames, filenames) in walk(province_path):
        for i in range(filenames.__len__()):
            data_list = load_by_province(filenames[i], True)
            for j in range(data_list.__len__()):
                for k in range(year_data.__len__()):
                    if str(data_list[j]['year']) == str(year_data[k]['year']):
                        name = splitext(basename(filenames[i]))
                        year_data[k]['datas'].append({
                            "province": name[0],
                            "avg_num": data_list[k]['avg_num'],
                            "in_num": data_list[k]['in_num'],
                            "in_rate": data_list[k]['in_rate'],
                            "out_num": data_list[k]['out_num'],
                            "out_rate": data_list[k]['out_rate'],
                            "net_in": data_list[k]['net_in'],
                            "net_in_rate": data_list[k]['net_in_rate'],
                        })

    for i in range(year_data.__len__()):
        if path.exists(year_path) is False:
            makedirs(year_path)
        with open(year_path + str(year_data[i]['year']) + '.pickle', 'wb') as f:
            pickle.dump(year_data[i]['datas'], f)


# 根据省名字来加载人口数据
# province : 省
# is_full_name : 是否包含后缀名
def load_by_province(province, is_full_name):
    file_name = province
    if is_full_name is False:
        file_name = province + '.pickle'
    content = open('caches/by_province/' + file_name, 'rb')
    return data_frame_to_json_object(pickle.load(content))


# 根据年份来加载人口数据
def load_by_year(year):
    content = open(year_path + year + '.pickle', 'rb')
    return pickle.load(content)


# 加载所有年份的人口数据
def load_all_year():
    datas = []
    years = load_years()
    for i in range(years.__len__()):
        content = open(year_path + str(years[i]) + '.pickle', 'rb')
        datas.append({'year': years[i], 'data': pickle.load(content)})
    return datas


# 将dataFrame转换成jsonObject
def data_frame_to_json_object(frame):
    result = []

    array_data = pd.DataFrame(frame).values
    for i in range(array_data.__len__()):
        result.append({
            "year": array_data[i][0],
            "avg_num": array_data[i][1],
            "in_num": array_data[i][2],
            "in_rate": array_data[i][3],
            "out_num": array_data[i][4],
            "out_rate": array_data[i][5],
            "net_in": array_data[i][6],
            "net_in_rate": array_data[i][7],
        })
    return result


# 加载现有省份
def load_provinces():
    f = []
    for (dirpath, dirnames, filenames) in walk('caches'):
        f.extend(filenames)

    return f


# 加载所有年份1954 ~ 1987
def load_years():
    years = []
    for i in range(1954, 1988):
        years.append(i)

    return years
