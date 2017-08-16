# -*-coding:UTF-8-*-
import requests

#执行API调用并存储相应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print ("Status code:",r.status_code)

#将API相应存储在一个变量中
response_dict = r.json()
print ("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print ("Repositories returned:",len(repo_dicts))

#研究地一个仓库
repo_dict = repo_dicts[0]
print("\n Keys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)


