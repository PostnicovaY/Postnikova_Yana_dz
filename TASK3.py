import os
from shutil import copy


def copy_dir(old_path, new_path):
    for obj in os.listdir(old_path):
        cur_old_path = os.path.join(old_path, obj)
        cur_new_path = os.path.join(new_path, obj)
        if os.path.isdir(cur_old_path):
            os.mkdir(cur_new_path)
            copy_dir(cur_old_path, cur_new_path)
        else:
            copy(cur_old_path, cur_new_path)


def search_templ(path, list):
    for obj in os.listdir(path):
        cur_path = os.path.join(path, obj)
        if obj == 'templates':
            list.append(cur_path)
        elif os.path.isdir(cur_path):
            search_templ(cur_path, list)
        else:
            continue

templates_dirs = []
search_templ(os.path.abspath('my_project'), templates_dirs)
try:
    os.mkdir(os.path.join(r'my_project', 'templates'))

    for path in templates_dirs:
        copy_dir(path, os.path.join(r'my_project', 'templates'))
except:
    print('Такой объект уже есть!')