"""
yaml
dump：字典或列表转换成yaml
"""
import yaml
#print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))
with open("demo3.yml","w") as f:
    yaml.dump(data={'a': [1, 2]},stream=f)