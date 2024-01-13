'''校园核酸采样信息管理系统'''
# 版本号  ：V1.1
# 开发者  ：香农的猫
# 开发时间：2022/11/29
# 说明 ：基于tkinter开发，开发软件为Pycharm，运行环境支持windows，mac
# 声明 ：本软件只用于2022年“领航杯”软件开发组赛事的学习交流，有相关建议或问题请联系作者（电话：18636244165）

from tkinter import *
from tkinter import messagebox
from db import *
from mainPage import *


class loginPage:  # 登录界面类

    def __init__(self, master):
        self.root = master
        self.root.geometry("320x190")
        self.root.title('登录')

        self.username = StringVar()
        self.password = StringVar()

        # 登录界面绘制
        self.page = Frame(root)
        self.page.pack()

        Label(self.page).grid(row=0, column=0)
        Label(self.page, text='账户：').grid(row=1, column=1)
        Entry(self.page, textvariable=self.username).grid(row=1, column=2)
        Label(self.page, text='密码：').grid(row=2, column=1, pady=10)
        Entry(self.page, textvariable=self.password).grid(row=2, column=2)
        Button(self.page, text='登录', command=self.login).grid(row=3, column=2, pady=10)
        Label(self.page, text=' 注* 账号:nzx').grid(row=10, column=2)
        Label(self.page, text='    密码:666666').grid(row=11, column=2)

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(name, pwd)
        print("用户：", name)
        print("密码：", pwd)
        if flag:
            print("登录成功")
            self.page.destroy()  #销毁当前窗口
            Main(self.root)      #进入程序
        else:
            messagebox.showwarning(title='警告', message=message)


if __name__ == '__main__':
    root = Tk()
    loginPage(master=root) #主对象
    root.mainloop()
