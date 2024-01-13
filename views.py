from tkinter import *
from tkinter import ttk
from db import db


class AboutFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        # 关于页面
        Label(self, text="关于页面").grid()
        Label(self, text="").grid()
        Label(self, text="").grid()


class ChangeFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        # 修改页面
        Label(self, text="修改页面").grid()
        Label(self, text="").grid()
        Label(self, text="").grid()


class InaertFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        # 插入页面
        Label(self, text="插入页面").grid()


class SearchFrame(Frame):    # 查询页面
    def __init__(self, root):
        super().__init__(root)

        self.table_view = Frame()
        self.table_view.pack()

        self.createPage()

    def createPage(self):
        columns = ("name", "ID", "time", "result")
        columnsChinese = ("姓名", "学号", "最近一次核酸检测时间", "核酸结果")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('ID', width=80, anchor='center')
        self.tree_view.column('time', width=80, anchor='center')
        self.tree_view.column('result', width=80, anchor='center')
        self.tree_view.heading('name',text='姓名')
        self.tree_view.heading('ID', text='学号')
        self.tree_view.heading('time', text='最近一次核酸检测时间')
        self.tree_view.heading('result', text='核酸结果')
        self.tree_view.pack(fill=BOTH,espand=True)

        self.showDataFrame()

        Button(self,text="刷新",command=self.showDataFrame).pack(anchor=E,pady=5)

    def showDataFrame(self):
        #删除旧的
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass

        students=db.all()
        index=0
        for stu in students:
            print(stu)
            self.tree_view.insert('',index+1,values=(stu['name'],stu['ID'],stu['time'],stu['result'],))


class DeleteFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        # 删除页面
        Label(self, text="删除页面").grid()
