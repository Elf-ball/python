#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk


class TK(object):
    # 设置windows弹框
    windows = tk.Tk()
    windows.title("my windows")
    windows.geometry('500x300')
    var = tk.StringVar()
    label = tk.Label(windows, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var)
    label.pack()
    bt = tk.Button(windows, text='print selection', width=10, height='2')
