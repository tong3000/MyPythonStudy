import yaml

#yaml转python字典格式
print(yaml.load("""
a: 1
 """,Loader=yaml.FullLoader))

#yaml文件中数据转python格式
print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))

#python字典转yaml格式
print(yaml.dump(data={'a':[1,2]}))

with open("demo3.yml", "w") as f:
    yaml.dump(data={'a': [1, 2]}, stream=f)