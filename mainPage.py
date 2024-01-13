from tkinter import *
from views import AboutFrame,InaertFrame,ChangeFrame,SearchFrame,DeleteFrame


class Main:
    def __init__(self, master):
        self.root = master
        self.root.title('校园核酸采样信息管理系统 V1.1')
        self.root.geometry('600x400')
        self.createPage()

    def createPage(self):
        # 关于页面
        self.aboutFrame = AboutFrame(self.root)
        # 修改页面
        self.changeFrame = ChangeFrame(self.root)
        # 插入页面
        self.inaertFrame = InaertFrame(self.root)
        # 查询页面
        self.searchFrame = SearchFrame(self.root)
        # 删除页面
        self.deleteFrame = DeleteFrame(self.root)

        menbbar = Menu(self.root)
        menbbar.add_command(label="信息录入", command=self.showInaert)
        menbbar.add_command(label="信息查询", command=self.showSearch)
        menbbar.add_command(label="信息删除", command=self.showDelete)
        menbbar.add_command(label="信息修改", command=self.showChange)
        menbbar.add_command(label="设置关于", command=self.showAbout)
        self.root['menu'] = menbbar

    def showAbout(self):
        self.aboutFrame.pack()
        self.changeFrame.pack_forget()  # 遗忘上个界面
        self.inaertFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.deleteFrame.pack_forget()

    def showChange(self):
        self.changeFrame.pack()
        self.aboutFrame.pack_forget()
        self.inaertFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.deleteFrame.pack_forget()

    def showInaert(self):
        self.inaertFrame.pack()
        self.aboutFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.deleteFrame.pack_forget()

    def showSearch(self):
        self.searchFrame.pack()
        self.aboutFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.inaertFrame.pack_forget()
        self.deleteFrame.pack_forget()

    def showDelete(self):
        self.deleteFrame.pack()
        self.aboutFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.inaertFrame.pack_forget()
        self.searchFrame.pack_forget()


if __name__ == '__main__':
    root = Tk()
    Main(root)
    root.mainloop()
