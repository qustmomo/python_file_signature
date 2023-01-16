# python_file_signature

文件类型标识，根据文件头的魔法数判断文件类型 引入时候，需要依赖 datas.py 文件类型列表， fiel_signature_entity.py 文件实体 file_signature.py 进行文件查询的工具类

本地文件类型查询代码如下
```
from file_signatrue import file_signature
#本地 文件路径
file_path = "D:\\test.pdf"
with open(file_path, "rb") as f:
    line = f.readline() #只读取第一行
    entities = file_signature.search_entity_by_int_codes(line)
    # 查询到的能匹配上的文件类型
    if entities:
        for entity in entities:
            # 打印下文件类型
            print(entity.file_type)
```
网络文件类型代码如下：
```
import requests
from file_signatrue import file_signature
url = "http://exp-new.bdstatic.com/static/exp-pc/common-jquery/widget/search-box/img/logo_6115f97.png"
response = requests.get(url, stream=True)
for line in response.iter_lines(): 
    entities = file_signature.search_entity_by_int_codes(line)
    # 查询到的能匹配上的文件类型
    if entities:
        for entity in entities:
            # 打印下文件类型
            print(entity.file_type)
     break # 只需要读取第一行
```
