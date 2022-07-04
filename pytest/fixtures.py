import os
import pandas as pd


def save_file(dir, file):
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = os.path.join(dir, file)
    with open(path, 'w') as f:
        f.write('test')


def get_env(env):
    if env == 'dev':
        return '開発用'
    elif env == 'prod':
        return '本番用'

def fetch_current_dir():
    current_dir1 = os.getcwd()
    current_dir2 = os.path.dirname(os.path.abspath(__file__))

    return current_dir1, current_dir2