"""
author :admin
Date : 2021/10/28
Description :
"""


def get_json_data01(*data):
    a = data
    print(a)


if __name__ == '__main__':
    # data = DataUtils.get_json_data('alarm_center_api_data', 'create_rule_data.json')
    # DataUtils.set_data(data, 'alarm_center_api_data', 'rule_data.yaml')
    get_json_data01('a', 'b', 'c', 'd', 'e')
    get_json_data01(('a', 'b'))
    get_json_data01(*('a', 'b'))
