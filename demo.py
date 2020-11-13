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
"""
a = {"name":"字典","age":12} #keyvalue
#字典没有下标的概念，靠key取值
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
"""



#9.1 if
#多条件选择
"""name = input("请输入白素贞被关押的塔名：")
if name == "金字塔" and len(name) == 3:
    print("判断成功")
else:
    print("错误")

a =  int(input("请输入a的年龄"))
if a > 18:
    print("成年人")
elif a > 16:
    print("青年")
elif a > 14:
    print("少年")
else:
    print("县朋友")
"""


#9.2while语句

# a =10
# while a > 0:
#     print(a)
#     a = a - 1
    
# else:
#     print("输入错误")

a = 0 
res = ""  
chengji = [80,60,59,29,99] #判断成绩是否合格，不合格请打印

# while a < 5:  #如何去准确的获取到列表中的每个元素，而不落下
#     if chengji[a] < 60:
#         print(chengji[a])
#         print("不合格")
#         print("不合格，成绩为：{}".format(chengji[a])) #format拼接到字符串中
#         res = res +","+str(chengji[a])   
#     a = a + 1
#     print("成绩为："+res)

#使用遍历的方法
"""for i in chengji: #遍历取值
    if i < 60:  #判断是否存在
        print("不合格的成绩是:{}".format(i))
"""

#把合格不合格进行分类,元组和list遍历方式一样
"""
hege = []
buhege = []
for i in chengji:
    if i < 60:
        #print("不合格成绩为：{}".format(i))
        buhege.append(i) #把取得值加入到新的数组中
        print(buhege)
    else:
        hege.append(i)
        print(hege)"""

#遍历字典
account = {"username":"王美丽","成绩":"89"}
"""for i in account:
    #print(i)
    print(account.get(i))   
"""
# for i in account.keys():
#     print(i)
# for j in account.values():
#     print(j)   
# for i,j in account.items():  #需要用items方法
#         print(i,j)

# #遍历字符串
# aa ="经济健康卡"
# for i in aa:
#     print(i) 

# #序列生成器，生成下标
# a = ["张三","里","d","ss","哈哈","就这","wudi","马超","欧赔","配角"]       
# for i in range(len(a)):
#     print(a[i]) #通过下标取值

#二维数组循环
# a = [[1,2,3],[4,5,6]]
# b = [{"username":"郭子","password":"123456"},{"username":"小玉","password":"123456"}]
# for i in a:
#     print(i)
#     for j in i:
#         print(j)
# for i in b:
#     print(i)
#     for j,k in i.items():
#         print(j,k)
#     for j in i:
#         print(i[j])

#for循环实现用户登录
t_user = [{"username":"郭子","password":"123456"},{"username":"小玉","password":"123456"}]
u = input("请输入账号：")
p = input("请输入密码：")
a = 1
for i in t_user:
    if i.get("username") == u and i.get("password") == p:
        print("登录成功")
        break #登录成功过后不执行
    else:  #最后一次运行都还没有这个账号，再来打印失败
        if len(t_user) == a:  #判断是不是最后一次
            print("登录失败")
    a = a + 1 

        

