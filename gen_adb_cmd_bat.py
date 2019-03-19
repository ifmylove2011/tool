# -*- coding: UTF-8 -*-

import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

hosts = [
    "192.168.52.169",
    "192.168.52.184",
    "192.168.52.189",
    "192.168.52.198",
    "192.168.52.200",
    "192.168.52.170",
    "192.168.52.190",
    "192.168.52.191",
    "192.168.52.188",
    "192.168.52.194",
]

apk_path = "E:/Projects/Gateway/app/build/outputs/apk/jinxin/debug/BeoneGateway_V0.71_debug.apk"
apk_intent = "com.jinxin.gateway2/com.jinxin.gateway.presentation.activity.MainActivity"
apk_package = "com.jinxin.gateway2"

root_dir = "E:\studying\python3"


def gen_connect_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb connect {host}\n".format(host=host)
        content = content + "echo ----------{host} connect success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "connect.bat"), "w") as f:
        f.write(content)


def gen_install_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} install -r -t {file} \n".format(host=host, file=apk_path)
        content = content + "echo ----------{host} install success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "install.bat"), "w") as f:
        f.write(content)


def gen_start_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} shell am start -n {intent}\n".format(host=host, intent=apk_intent)
        content = content + "echo ----------{host} start success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "start.bat"), "w") as f:
        f.write(content)


def gen_kill_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} shell am force-stop {package}\n".format(host=host, package=apk_package)
        content = content + "echo ----------{host} stop success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "kill.bat"), "w") as f:
        f.write(content)


def gen_uninstall_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} uninstall {package}\n".format(host=host, package=apk_package)
        content = content + "echo ----------{host} uninstall success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "uninstall.bat"), "w") as f:
        f.write(content)


# print(os.getcwd())
gen_connect_bat()
gen_install_bat()
gen_start_bat()
gen_kill_bat()
gen_uninstall_bat()




# def delete(event):
#     listbox_hosts.delete(listbox_hosts.curselection())
#
#
# def select_file():
#     filename = tkinter.filedialog.askopenfilename()
#     file_v.set(filename)
#
#
# def select_dir():
#     dir = tkinter.filedialog.askdirectory()
#     dir_v.set(dir)
#
#
# def add():
#     hosts.insert(0, entry_host.get())
#     hosts_v.set(hosts)
#
#
# def gen():
#
#     tmp_intent = entry_intent.get()
#     if len(tmp_intent) > 0:
#         apk_intent = tmp_intent
#     else:
#         print("未指定intent，已设为默认值：" + apk_intent)
#
#     tmp_package = entry_pack.get()
#     if len(tmp_package) > 0:
#         apk_package = tmp_package
#     else:
#         print("未指定包名，已设为默认值：" + apk_package)
#
#     tmp_path = entry_file.get()
#     if len(tmp_path) > 0:
#         apk_path = tmp_path
#     else:
#         print("未指定apk路径，已设为默认值：" + apk_path)
#
#     tmp_dir = entry_dir.get()
#     print(tmp_dir)
#     if len(tmp_dir) > 0:
#         root_dir = tmp_dir
#     else:
#         print("未指定生成目录，已设为默认值：" + root_dir)
#
#     gen_connect_bat()
#     gen_install_bat()
#     gen_start_bat()
#     gen_kill_bat()
#     gen_uninstall_bat()
#     print(tkinter.messagebox.showinfo(title='info', message='生成成功'))  # 提示信息对话窗
#
#
# window = Tk()
# window.title('生成adb相关bat')
# window.geometry('300x600')
#
# lable_host = Label(window, text='网络地址:')
# lable_host.grid(row=0, column=0, sticky=N + S)
# entry_host = Entry(window)
# entry_host.grid(row=0, column=1, padx=5, pady=5, columnspan=6, sticky=N + S)
# button_add_host = Button(window, text="+", command=add)
# button_add_host.grid(row=0, column=8, padx=10, sticky=N + S)
#
# lable_list = Label(window, text="已添加地址列表:", wraplength=50)
# lable_list.grid(row=1, column=0, sticky=N + S)
# hosts_v = StringVar()
# listbox_hosts = Listbox(window, listvariable=hosts_v)
# listbox_hosts.grid(row=1, column=1, padx=5, pady=5, columnspan=6)
# listbox_hosts.bind('<Button-3>', delete)
# hosts_v.set(hosts)
#
# lable_intent = Label(window, text='Intent:')
# lable_intent.grid(row=2, column=0)
# entry_intent = Entry(window)
# entry_intent.grid(row=2, column=1, padx=5, pady=5, columnspan=6, sticky=N + S)
#
# lable_pack = Label(window, text='包名:')
# lable_pack.grid(row=3, column=0)
# entry_pack = Entry(window)
# entry_pack.grid(row=3, column=1, padx=5, pady=5, columnspan=6, sticky=N + S)
#
# lable_file = Label(window, text='APK路径:')
# lable_file.grid(row=4, column=0, sticky=N + S)
# file_v = StringVar()
# entry_file = Entry(window, textvariable=file_v)
# entry_file.grid(row=4, column=1, padx=5, columnspan=6, sticky=N + S)
# button_file = Button(window, text="...", command=select_file)
# button_file.grid(row=4, column=8, padx=10, sticky=N + S)
#
# lable_dir = Label(window, text='BAT目录:')
# lable_dir.grid(row=5, column=0, sticky=N + S)
# dir_v = StringVar()
# entry_dir = Entry(window, textvariable=dir_v)
# entry_dir.grid(row=5, column=1, padx=5, columnspan=6, sticky=N + S)
# button_dir = Button(window, text="...", command=select_dir)
# button_dir.grid(row=5, column=8, padx=10, sticky=N + S)
#
# button_gen = Button(window, text="生成bat", width=30, height=1, command=gen)
# button_gen.grid(row=6, column=0, padx=5, pady=5, columnspan=8)
#
# window.mainloop()
