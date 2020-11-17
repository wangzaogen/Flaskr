

import inspect
import os
import sys


def get_root_path():
    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    parent_path = os.path.dirname(file_path)
    lib_path = os.path.dirname(parent_path)
    root_path = os.path.dirname(lib_path)
    return root_path


def create_data_path():
    root_path = get_root_path()
    data_path = root_path + "/data"
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    return data_path


def create_site_path(site):
    data_path = create_data_path()
    site_path = data_path + "/" + site
    if not os.path.exists(site_path):
        os.makedirs(site_path)
    return site_path



# const for path
ROOT_PATH = get_root_path().replace('\\','/')
DATA_PATH = ROOT_PATH + "/data"
SAMPLE_PATH = ROOT_PATH + "/sample"
LOG_PATH = ROOT_PATH + "/data"


if __name__ == "__main__":
    create_site_path('haodf')
