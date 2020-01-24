import  requests



requests = requests.Session()
url = "http://192.144.148.91:2333/login"
headers = {"Content-Type":"application/json"}
data = {"username":"langjin","password":"lj123456"}
res = requests.post(url=url,headers=headers,json=data)
jieguo = res.json()
token = jieguo["data"]["token"]
status = jieguo.get("status")
if status == 200:
    print("登录成功")
else:
    print("登录失败")

url = "http://192.144.148.91:2333/article/new"
headers.update(token = token)
data = {"title":"为什么要学习测试",
"content":"内容",
"tags":"测试",
"brief":"介绍"}
a = requests.post(url=url,headers=headers,json=data)
text = a.json()
status = text["status"]
if status == 200:
    print("添加文章成功")
else:
    print("添加文章失败")




# url = "http://192.144.148.91:2333/getinspirer?num=1"
# headers = {"Content-Type":"application/json"}
# res = requests.get(url=url,headers=headers)
# text = res.json()
# a = text["data"]
# print(a)
# if len(a) == 4:
#     print("获取灵感成功")
# else:
#     print("获取失败")





url = "http://192.144.148.91:2333/question/new"
headers.update(token = token)
data =  {
"title":"为什么要学习测试", 
"content":"内容", 
"tags":"测试", 
"brief":"介绍" 
}
res = requests.post(url,headers=headers,json=data)
text = res.json()
if text["msg"] == "操作成功！":
    print("添加文章成功")
else:
    print("添加文章失败")












   