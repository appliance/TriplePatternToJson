'''
    思路：
        f1:获取所有人名
        f2:利用某个人名，获取其包含的所有信息（保存在同一个{}字典中）
        f3:基于此人信息构造json数据（依据{}中的key遍历去创建所需要的json格式内容）
'''
filePath = "C:/Users/Administrator/Desktop/ElasticSearch/对Person文件的json化/ToJson/Person.txt"
allPersonsName = []
dic = {}    # 此字典形式如下{ 用户名：字典{"属性":"属性值"}，用户名：字典{"属性":"属性值"} }
tempName = " "
with open(filePath,'r',encoding='utf-8') as f:
    # 实现  字典化保存Person所有数据
	# 遍历所有行，依据姓名将相同姓名的所有属性保存到一个字典中{}
    for line in f.readlines():
        name = line.split(" ")[0]
        property = line.split(" ")[1]
        propertyValue = line.split(" ")[2]
        if tempName == name:
            propertyDic[property] = propertyValue
        if name not in allPersonsName:
            allPersonsName.append(name)
            tempName = name
            propertyDic = {property: propertyValue}
            dic[tempName] = propertyDic


# 实现 每一个Person构造一个json数据保存到PersonsJson.json文件中去
import json
import codecs
saveFilePath = codecs.open('C:/Users/Administrator/Desktop/ElasticSearch/对Person文件的json化/ToJson/Persons.json','wb',encoding='utf-8')
for name in allPersonsName:
    personDic = dic[name]
    if 'weight' in personDic.keys():
        weight = personDic['weight']
    else:
        weight = " "
    if 'height' in personDic.keys():
        height = personDic['height']
    else:
        height = " "
    # 根据已有属性去构造json数据
    size = 1
    poContent = " "
	
	# 依据属性，动态构造字符串，拼接
    for prop in personDic:
        if size < personDic.__len__():
            template = '{"pred":"' + prop + '",' + '"obj":"' + personDic[prop].strip() + '"},'
        else:
            template = '{"pred":"' + prop + '",' + '"obj":"' + personDic[prop].strip() + '"}'
        size = size + 1
        poContent = poContent + template
    finalPo = '"po":[' + poContent + ']'
    personJson = '{"subj":"' + name + '",' + '"weight":"' + weight + '",' + '"height":"' + height + '",' + finalPo + '}'
    personJson = json.dumps(personJson, ensure_ascii=False)
    saveFilePath.write(personJson + '\n')











