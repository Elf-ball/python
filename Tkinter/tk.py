#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk


class TK(object):
    # 设置windows弹框
    windows = tk.Tk()
    windows.title("my windows")
    windows.geometry('500x300')
    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    var = tk.StringVar()
    on_hit = False
    # 设置一个单行输入框
    e = tk.Entry(windows, show = None)
    e.pack()
    # 设置多文本输出框
    t = tk.Text(windows, height=3)
    t.pack()

    def insert_point(self):
        # 获取文本输入框中的内容
        var = self.e.get()
        # 在空间t的结尾处插入获取到的内容
        self.t.insert('end', var)

    def hit_me(self):
        if self.on_hit is False:
            self.on_hit = True
            self.var.set('you hit me')
        else:
            self.on_hit = False
            self.var.set('')

    def click_bt(self):
        text_label = tk.Label(
            self.windows, textvariable=self.var, bg='green', fg='white', font=('Arial', 12), width=30, height=2
        )
        text_label.pack()
        # 点击按钮时调用hit_me函数
        bt = tk.Button(self.windows, text='hit me', font=('Arial', 12), width=12, height=1, command=self.hit_me)
        bt.pack()
        self.windows.mainloop()

    def input_entry(self):
        input_pwd = tk.Entry(self.windows, show=None, font=('Arial', 14))
        input_text = tk.Entry(self.windows, show='*', font=('Arial', 14))
        input_text.pack()
        input_pwd.pack()
        self.windows.mainloop()

    def output_text(self):
        bt = tk.Button(self.windows, text='insert button', width=10, height=2, command=self.insert_point)
        bt.pack()
        self.windows.mainloop()


if __name__ == '__main__':
    TK().output_text()
