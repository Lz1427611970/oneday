# print("你好，无敌")
# print("hh")

# b = type("哈哈哈")
# print(b)

# a = float(input("请输入一个数字："))
# b = float(input("请输入另一个数字："))
# print(a+b)
# len()只能用在元祖数组字典中
# print(len("hhhhhhhh"))


#元组
"""b = ("哈哈","欧阳")
a = (1,2,3,4,"呵呵","嘻嘻",True,False,b)
#元组里面的方法：index()获取某个值的下标，count()计数
print(a.index("呵呵"))
print(a.count(1))
#二维元组,三维元组
print(a[-1][-1])
#切片
print(a[0:3])"""


#数组列表，list
#元组不可以修改，数组可以修改
"""
b = ["哈哈","欧阳"]
a = [1,2,3,4,"呵呵","嘻嘻",True,False,b]
print(a)
a.index("呵呵")
a.count(1)
a.append(8) #增加
a.insert(0,"h") #插入数据，下标加数据
# entend()合并数组,
# remove()删除
# sort() 排序
c = a.pop(1)  #从数组中取走数数据
print(a)
print(c,type(c))
"""


#字典
a = {"name":"字典","age":12} #keyvalue
#字典没有下标的概念，靠key驱逐
print(a["name"])
#取值
a["name"] #不存在的话会报错
print(a.get("name"))
print(a.get("name1")) #不存在的时候会返回none、
#新增,修改
a["adress"] = "成都"
print(a)
a["adress"] = "南京"
print(a)
a.update(adress="合肥")
print(a)
#取走
a.pop("name")
#删除，可以删除字典也可以删除数组
del a["age"]
print(a)
print(a.keys())
print(a.values())






