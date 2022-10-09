# Поиск контактов

from export_data import export_data
from print_data import print_data


def search_data(lettering, data):
    if len(data) > 0:
        for item in data:
            if lettering in item:
                return item
    else:
        return None
