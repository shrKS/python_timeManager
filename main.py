from re import A
import sys
import os
import tkinter as tk
import tkinter.ttk as tkk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
import config
import function
import stopWatch

class Application(tk.Frame):
    def __init__(self, master=None):
        self.DEBUG_LOG = True
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master=master


        #excel as DB
        self.wb = config.WB
        self.db_sheet = config.DB_SHEET
        self.watch = stopWatch.stopWatch(self.wb, self.db_sheet)
        

        #add command
        # self.test_func()

    def test_func(self, ts_button, te_button):
        print("this is test function")
        fileType = [("", "*xlsx")]
        iDir = os.path.abspath(os.path.dirname('__file__'))
        filename = tkFileDialog.askopenfile(filetypes=fileType, initialdir=iDir).name
        function.testCommand(filename)

        #change mode
        ts_button["state"] = tk.DISABLED
        te_button["state"] = tk.NORMAL

    def timeStart_func(self, ts_button, te_button):
        function.timeStart(self.watch)
        #change mode
        ts_button["state"] = tk.DISABLED
        te_button["state"] = tk.NORMAL

    def timeEnd_func(self, ts_button, te_button):
        function.timeStop(self.watch)
        #change mode
        ts_button["state"] = tk.NORMAL
        te_button["state"] = tk.DISABLED

    def createWindow(self):
        self.newWindow = tk.Toplevel(self.master)
        newLabel = tk.Label(self.newWindow, text='new window')
        newButton = tk.Button(self.newWindow, text='new window button')

        newLabel.pack()
        newButton.pack()

    def createWindow(self, label_title):
        newWindow = tk.Toplevel(self.master)
        newLabel = tk.Label(newWindow, text=label_title)
        # newButton = tk.Button(self.newWindow, text='new window button')

        newLabel.pack()
        return newWindow
        # newButton.pack()



    def changeTitle(self):
        def showSelected(event):
            print(combobox.get())
            config.TITLE = combobox.get()
            # newWindow.destroy()
        #tupleで指定
        values = ('test', 'test2')
        # newWindow = self.createWindow("select title")
        combobox = tkk.Combobox(self.master, values=values)
        #イベントと紐付ける
        combobox.bind('<<ComboboxSelected>>', showSelected)

        combobox.pack()

        #決定ボタンが必要

    def setTitleBar(self):
        def showSelected(event):
            print(combobox.get())
            config.TITLE = combobox.get()
            # newWindow.destroy()
        #tupleで指定
        values = ('test', 'test2')
        # newWindow = self.createWindow("select title")
        combobox = tkk.Combobox(self.pw_left, values=values)
        #イベントと紐付ける
        combobox.bind('<<ComboboxSelected>>', showSelected)

        combobox.pack()
        



    def create_widgets(self):
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""
        
        pw_main = tk.PanedWindow(self.master, orient='horizontal')
        pw_main.pack(expand=True, fill = tk.BOTH, side="left")
        self.pw_left = tk.PanedWindow(pw_main, bg="white", orient='vertical')
        pw_main.add(self.pw_left)
        self.pw_right = tk.PanedWindow(pw_main, bg="yellow", orient='vertical')
        pw_main.add(self.pw_right)
        # fm_select = tk.Frame(pw_left, bd=2, relief="ridge")
        # pw_left.add(fm_select)

        # main_pane = tk.PanedWindow(self.master, orient='horizontal')
        # main_pane.pack(expand=True, fill=tk.BOTH, side="left")

        self.setTitleBar()

        timeStart_button = tk.Button(self.pw_left, text='start', width=8, command = lambda:self.timeStart_func(timeStart_button, timeEnd_button))
        timeEnd_button = tk.Button(self.pw_left, text='stop', width=8, command = lambda:self.timeEnd_func(timeStart_button, timeEnd_button))
        
        popupWindow_button = tk.Button(self.pw_left, text='create new window', width=8, command=self.createWindow)
        changeTitle_button = tk.Button(self.pw_left, text='change title', width=8, command=self.changeTitle)

        #create butten on GUI 
        timeStart_button.pack(side='left', padx=(10,10), fill='x')
        timeEnd_button.pack(side='left', padx=(10,10), fill='x')
        popupWindow_button.pack(side=tk.LEFT)
        changeTitle_button.pack(side=tk.RIGHT)



        # btn_test_func = tk.Button()



if __name__ == '__main__':
    root = tk.Tk()
    myApp = Application(master=root)
    myApp.master.title('my test application') #set title
    myApp.master.geometry("{}x{}".format(config.WINDOW_WIDTH, config.WINDOW_HEGHT)) #set width * height

    myApp.mainloop()
