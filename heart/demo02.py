#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：heart 
@File    ：demo02.py.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/27 10:53 
'''
import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('亲爱的')
    window.geometry("220x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
    text='我想你了!',
    bg='pink',
    font=('楷体',18),
    width=25,height=4
    ).pack()
    window.mainloop()

threads =[]
for i in range(10):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()
