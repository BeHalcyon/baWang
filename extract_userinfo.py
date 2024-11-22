import re

obj=re.compile(r'"data":"{"encrypt_key":"(?P<encrypt_key>.*?)","version":(?P<version>.*?),".*?"iv":"(?P<iv>.*?)","create_time".*?{"id":"(?P<id>.*?)","nickname.*?userToken":"(?P<userToken>.*?)"',re.S)

origin_data = '''













'''

contents=origin_data
result=obj.finditer(contents)
for i in result:
    user=f"{i.group('id')}----{i.group('userToken')}----{i.group('encrypt_key')}----{i.group('iv')}----{i.group('version')}\n"
    with open('users.txt','a+',encoding='utf-8') as file1:
        file1.writelines(user)
        print(f"写入成功{i.group('id')}")