# -*- coding: utf-8 -*-

import os
import json


def load_json(file_dir, file_name):
    with open(os.path.join(file_dir, file_name)) as f:
        return json.load(f)


def get_all_files(file_dir):
    return os.listdir(file_dir)