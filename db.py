import json


class MyDatabases:
    def __init__(self):
        self.users = json.loads(open('users.json', mode='r', encoding='utf-8').read())
        self.students = json.loads(open('students.json', mode='r', encoding='utf-8').read())

        #登录密码检测方法
    def check_login(self, username, password):
        for user in self.users:
            if username==user['username']:
                if password==user['password']:
                    return True,'登陆成功'
                else:
                    return False,'密码错误'
        return False,'用户不存在'
        #
    def all(self):
        return self.students



db = MyDatabases()

if __name__ == '__main__':
    print(db.check_login('123', '123'))
    print(db.all())