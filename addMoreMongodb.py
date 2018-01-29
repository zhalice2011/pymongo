import pymongo

conn = pymongo.MongoClient()
# 选择一个数据库
db = conn.blog
# 选择一个collection
collection = db.user

def show(collection):
    # 查找
    for item in collection.find():
        print(item)

# 插入
dic = {
    'name': '刀塔传奇',
    'age': 23,
    'address': '北京朝阳',
    'blog': '没有博客'
}
# collection.insert(dic)

many = []
import copy
for index in range(1, 8):
    tempdic = copy.deepcopy(dic)
    tempdic['age'] = index**2
    many.append(tempdic)

collection.insert_many(many)
show(collection)
