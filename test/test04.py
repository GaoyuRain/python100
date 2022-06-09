
# 字节长度

def len_encode_utf8(data: str):
    l = len(data.encode('UTF-8'))
    return f'UTF-8编码\t字符串: {data}\t长度:{l} \n -----------------------'


def len_encode_gbk(data: str):
    l = len(data.encode('gbk'))
    return f'gbk编码\t字符串: {data}\t长度:{l} \n -----------------------'


def test_len():
    print(len_encode_utf8('>'))
    print(len_encode_utf8('哈'))
    print(len_encode_utf8('a'))
    print(len_encode_utf8(','))
    print(len_encode_utf8('，'))
    print(len_encode_gbk('>'))
    print(len_encode_gbk('哈'))
    print(len_encode_gbk('a'))
    print(len_encode_gbk(','))
    print(len_encode_gbk('，'))
    print('哈'.encode('gbk'))
    print('哈'.encode('utf-8'))
    print('ha',)





if __name__ == '__main__':
    test_len()
