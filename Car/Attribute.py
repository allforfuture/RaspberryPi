import json

class Attribute(object):
    """车子的属性"""

    # 打开一个文件
    __jsonFile = open(r'.\Config\config.json', 'r')#"__"表示私有方法和私有属性
    jsonDict = json.loads(__jsonFile.read())
    # 关闭打开的文件
    __jsonFile.close()