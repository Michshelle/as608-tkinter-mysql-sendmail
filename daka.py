#!/usr/bin/env python3

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import sys
import time
import as608_combo_lib as as608

global session_0
session_0 = as608.connect_serial_session("/dev/ttyUSB0")
if not session_0:
    print("打卡机连接失败，程序退出")
    exit(1)

# 用于重定向print到Text控件
class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, s):
        self.widget.insert(tk.END, s)
        self.widget.see(tk.END)

    def flush(self):
        pass

root = tk.Tk()
root.title("考勤系统")
root.geometry("450x320")

# 上半部分区域
top_frame = tk.Frame(root, height=220)
top_frame.pack(side="top", fill="x")
top_frame.pack_propagate(False)

# 上半部分左区（两个标签）
left_top = tk.Frame(top_frame, width=220)
left_top.pack(side="left", fill="y")
left_top.pack_propagate(False)

label_signin = tk.Label(left_top, text="签到", font=("Arial", 18), width=8, height=2)
label_signin.pack(pady=(30, 10))
label_leave = tk.Label(left_top, text="离开", font=("Arial", 18), width=8, height=2)
label_leave.pack(pady=(10, 30))

# 下半部分区域（串口消息显示）
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

log_text = ScrolledText(bottom_frame, font=("Consolas", 10))
log_text.pack(fill="both", expand=True)

# 重定向print到Text控件
sys.stdout = TextRedirector(log_text)

 # 按钮的行为       
def on_select():
    global highlight_state
    if highlight_state == 0:
        label_signin.config(bg="yellow")
        label_leave.config(bg=default_bg)
        highlight_state = 1
    else:
        label_signin.config(bg=default_bg)
        label_leave.config(bg="yellow")
        highlight_state = 0

def on_confirm():
    # 清空底部文本框
    log_text.delete('1.0', tk.END) 
    if label_signin.cget("bg") == label_leave.cget("bg"):
        print("请先选择签到或离开")
        return

    if not session_0:
      print("打卡机连接失败，程序退出")
      time.sleep(2)
      root.destroy()
      exit(1)

    if label_signin.cget("bg") == "yellow":
        status="signin"
        print("签到开始，请按下指纹...")  
    else:
        status="leave"
        print("准备离开，请按下指纹...")  

    # 启动模拟串口线程
    threading.Thread(target=as608.search_fingerprint_on_dev, args=(session_0, as608, status), daemon=True).start()
    # 标签色复原
    label_signin.config(bg=default_bg)
    label_leave.config(bg=default_bg)
    

def on_cancel():
    # 清空底部文本框
    log_text.delete('1.0', tk.END)  
    print("操作已取消。")
    # 标签色复原
    label_signin.config(bg=default_bg)
    label_leave.config(bg=default_bg)



# 上半部分右区（三个按钮）
right_top = tk.Frame(top_frame)
right_top.pack(side="right", fill="both", expand=True)

btn_select = tk.Button(right_top, text="选择", width=10, height=2, command=on_select)
btn_select.pack(pady=10, padx=20)
btn_confirm = tk.Button(right_top, text="确定", width=10, height=2, command=on_confirm)
btn_confirm.pack(pady=5, padx=20)
btn_cancel = tk.Button(right_top, text="取消操作", width=10, height=2, command=on_cancel)
btn_cancel.pack(pady=10, padx=20)

default_bg = label_signin.cget("bg")
highlight_state = 0

root.mainloop()