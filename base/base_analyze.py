import os
import yaml


def analyze_yaml_file(file_name, data_key):
    file_path = os.path.join('data/', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        # 安全加载方式
        data = yaml.load(f, Loader=yaml.FullLoader)
        return list(data[data_key].values())
