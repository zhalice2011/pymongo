from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

class TestMongo(object):

    def __init__(self):
        con = MongoClient('localhost', 27017)  # 比较常用   #-获取数据库的连接

        self.db = con.blog  # 获取数据库
        # self.client = MongoClient()
        #  = self.client['blog']

    #新增数据的方法 .insert_one
    def add_one(self):
        ''' 往数据库中新增数据 '''
        post = {
            'title': '新的标题4',
            'content': '博客内容.....4',
            'created_at': datetime.now()
        }
        #return post
        return self.db.posts.insert_one(post)
    #查询数据的方法  .find_one
    def get_one(self):
        return self.db.posts.find_one()   

    #查询所有数据的方法  .find
    def get_all(self):
        return self.db.posts.find({})   

    #查询指定id的方法  .find{findcase}
    def get_opt(self,opt):
        # return self.db.posts.find_one({'title':'新的标题4'})   
        return self.db.posts.find_one(opt)   
    
    #修改一条数据
    def update_one(self):
        #update_one({'x':4},{'$set':{'x':3}})
        return  self.db.posts.update_one({'title':'新的标题4'}, {'$set': {'title': '我在骗自己'}})

    #修改多条数据
    def update_more(self):
        rest = self.db.posts.update_many({'$inc': {'title': '我还是很喜欢你'}})




def main():
    obj = TestMongo()
    #rest = obj.add_one()  #调用新增的函数 得到一个结果
    # print(rest.inserted_id)
    #rest = obj.get_all()
    # post = {
    #     'title': '新的标题4',
    # }
    # rest = obj.get_opt(post)
    # print(rest)
    # for item in rest:
    #     print(item['_id'])
    #     print(item['title'])
    rest = obj.update_one()
    #rest = obj.update_more()
    


if __name__ == '__main__':
    #print('主入口函数')
    main()