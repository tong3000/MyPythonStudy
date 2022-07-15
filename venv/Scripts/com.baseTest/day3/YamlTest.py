"""
yaml
load()：将yaml格式转成列表或者字典
-开头：列表
什么都没有开头：字典
"""
import yaml

#转换成列表
print(yaml.load("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
""",Loader = yaml.FullLoader))
#转换成字典
print(yaml.load("""
a: 1
 """,Loader = yaml.FullLoader))

#读取文件转换
#嵌套
print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))