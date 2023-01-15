from file_signatrue.datas import datas


def search(str_codes):
    """
    :param str_codes: 文件头的字符列表
    :return: 可能的文件类型列表
    """
    if str_codes is None or len(str_codes) == 0:
        return None
    rs = []
    for entity in datas:
        entity_codes = entity.codes
        entity_skip = entity.skip
        flag = False
        min_len = min(len(entity_codes), len(str_codes) - entity_skip)
        for i in range(min_len - 1):
            current_code = str_codes[i + entity_skip]
            flag = (entity_codes[i][0] == current_code[0] or entity_codes[i][0] == 'x') and (
                    entity_codes[i][1] == current_code[1] or entity_codes[i][1] == 'x')
            if flag:
                continue
            break
        if flag:
            rs.append(entity)
    return rs


def search_entity_by_int_codes(int_codes):
    """
    :param int_codes: int类型的文件头列表
    :return: 文件类型列表
    """
    codes = []
    for item in int_codes:
        code = hex(item)[2:].upper()
        if len(code) == 1:
            code = '0' + code
        codes.append(code)
    return search(codes)
