# -*- coding:utf-8 -*-


start_urls = [
        # "https://etherscan.io/token/generic-tokenholders2?a=0xf230b790e05390fc8295f4d3f60332c93bed42e2&p=1"
        "https://etherscan.io/token/generic-tokenholders2?a=0xf230b790e05390fc8295f4d3f60332c93bed42e2&p={}".format(str(i)) for i in range(1,11)
    ]
print start_urls
