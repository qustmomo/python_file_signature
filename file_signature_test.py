import requests
from file_signatrue import file_signature


def test_file():
    """
    本地文件测试，打印下文件类型
    :return:
    """
    # 文件路径
    file_path = "D:\\test.pdf"
    with open(file_path, "rb") as f:
        line = f.readline()
        entities = file_signature.search_entity_by_int_codes(line)

        if entities:
            for entity in entities:
                print(entity.file_type)


def test_url():
    """
    网路类型测试，打印下文件类型
    :return:
    """
    # url地址
    url = "http://exp-new.bdstatic.com/static/exp-pc/common-jquery/widget/search-box/img/logo_6115f97.png"
    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        entities = file_signature.search_entity_by_int_codes(line)
        for entity in entities:
            print(entity.file_type)
        break
