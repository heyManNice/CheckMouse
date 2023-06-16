import json
import os
# 定义能够得到目标文件中内容的函数。
def get_data(filename='database.json'):
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename, 'r') as file_contents:
            file_contents = file_contents.readlines()
    return file_contents

def select() -> None:
    """
    用来读取数据的函数
    :param em: 目标em对象
    :param key: 查询对象的键
    :return: None
    """
    with open('database.json', 'r') as jsFile:
        data = json.load(jsFile)
        return data

def delete(em,key) -> None:
    """
    用来删除数据的函数
    :param em: 想要删除的em对象
    :param key: 想要删除对象的键
    :return: None
    """
    with open('database.json', 'r+') as jsFile:
        # 将读取的文件数据转换成python的dict数据类型
        jsOBJ = jsFile.read()
        print(jsOBJ)
        data = json.loads(jsOBJ)
        print(data)
        print('将em对象全部删除(清空dict)请输入：all'+'\n'
          '部分删除(删除em键所对应的值)请输入: part')
        input_value = input('请按照需求完成输入操作：')
        if input_value == 'all':
            del data[em]
            data = json.dumps(data)
            print(data)
            jsFile.write(data)
        else:
            del data[em][key]
            data = json.dumps(data)
            print(data)
            jsFile.write(data)
    print('已完成删除操作！')

def insert(data) -> None:
    """
    用来增加数据的函数
    :param em: 输入一个em对象,默认为用户的序列号，如users_1,users_2
    :param key: em对象的键,通常为用户的姓名name
    :param value: em对象的值，通常包含用户的各类信息user_info,数据类型为dict
    :return: None
    """
    jsOBJ = json.dumps(data)
    # 以写入的形式将jsOBJ写入json文件，但是每次写都会覆盖前一次内容
    with open("database.json", "w") as jsFile:
        jsFile.write(jsOBJ)
    return {"code":0}

def update_original(em,key,value) ->None:
    """
    用来修改数据的函数，如果给定的键值对不存在时，
    会增加一个键值对；给定的键值对存在时，就会修改字典元素。
    :param em: em实体管理对象
    :param key: 待修改对象的键
    :param value: 修改后对象的值
    :return: dict
    """
    with open('database.json','r',encoding='utf-8') as jsFile:
        jsOBJ = jsFile.read()#1.读取json
    py_dict = json.loads(jsOBJ)#2.解码json
    py_dict[em][key]=value#3.修改json
    py_dict = json.dumps(py_dict)#4.编码json
    with open('database.json','w',encoding='utf-8') as jsFile:
        jsFile.write(py_dict)#5.写入json
    print('数据更新成功！')
    print(line)
    # print('请输入你要查询对象的em')


if __name__ == '__main__':
    print(select())
    insert({"ttt":0})
