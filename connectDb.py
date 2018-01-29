# coding: utf8

import pymongo

# 默认没有密码，所以可以这么写。如果设置了密码需要使用授权方法db.auth("用户名","密码")
connection = pymongo.MongoClient()
# 选择一个数据库
db = connection.blog
# 选择一个表
collection = db.user

print(collection)