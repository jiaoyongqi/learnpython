# -*-coding:UTF-8-*-
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

def get_country_code(country_name):
    '''根据指定的国家,返回Pygal使用的两个字母的国别码'''
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到指定的国家,就返回None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))