
# -*- coding: utf-8 -*-
import _thread
from tkinter import *
import win32con
import win32api
import time
import datetime
import pyautogui
import pyperclip

LOG_LINE_NUM = 0
key_map = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0
 }
'''
key_map = {
    "0": 49, "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56, "8": 57, "9": 58,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}
'''
class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("按键模拟") #窗口名
        self.init_window_name.geometry('500x550+40+40') # #1068 681为窗口大小，+40 +40 定义窗口弹出时的默认展示位置

        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="反馈")
        self.result_data_label.grid(row=3, column=0)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)

        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=60, height=10)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=1, columnspan=10)

        self.result_data_Text = Text(self.init_window_name, width=60, height=10)  #处理结果展示
        self.result_data_Text.grid(row=4, column=0, rowspan=3, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=60, height=10)  # 日志框
        self.log_data_Text.grid(row=16, column=0, columnspan=10)

        # 按钮1
        self.simulate_button1 = Button(self.init_window_name, text="按键模拟输入", bg="lightblue", width=20,
                                              command=self.button1_go)  # 调用内部方法  加()为直接调用
        self.simulate_button1.grid(row=2, column=1)

        # 按钮2
        self.simulate_button2 = Button(self.init_window_name, text="字符模拟输入", bg="lightblue", width=20,
                                              command=self.button2_go)  # 调用内部方法  加()为直接调用
        self.simulate_button2.grid(row=2, column=4)

    def button1_go(self):
        _thread.start_new_thread(self.The_key_to_simulate, ())

    def button2_go(self):
        _thread.start_new_thread(self.ctrl_C_V_simulate, ())

    def The_key_to_simulate(self):
        # 获取
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        print("src =", src)

        if src:
            try:
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "5s后开始模拟按键,请将输入法调成英文\n")

                time.sleep(5)
                for i in src:
                    # print(chr(i))
                    time.sleep(0.05)
                    print(chr(i))
                    # 一个按键映射了两个字符，需要区分开
                    if chr(i).isalpha():
                        if chr(i).islower():
                            self.key_press(chr(i))
                        else:
                            self.key_down('shift')
                            self.key_press(chr(i))
                            self.key_up('shift')
                print("done")

                self.result_data_Text.insert(2.0, "模拟结束\n")
                self.write_log_to_Text("INFO:The_key_to_simulate done")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"模拟输入失败")
        else:
            # 输出到界面
            self.result_data_Text.delete(1.0, END)
            self.result_data_Text.insert(1.0, "请输入\n")

    # 非ASCII字符只能通过粘贴方式输入
    def ctrl_C_V_simulate(self):
        # 获取
        src = self.init_data_Text.get(1.0,END)
        print("src =", src)
        if src:
            try:
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "5s后开始模拟输入\n")

                time.sleep(5)
                for i in src:
                    # print(chr(i))
                    time.sleep(0.05)
                    print(i)
                    pyperclip.copy(i)  # 先复制
                    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
                print("done")

                self.result_data_Text.insert(2.0, "模拟结束\n")
                self.write_log_to_Text("INFO:The_ctrl_C_V_simulate done")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"模拟输入失败")
        else:
            # 输出到界面
            self.result_data_Text.delete(1.0, END)
            self.result_data_Text.insert(1.0, "请输入\n")

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

    def key_down(self,key):
        """
        函数功能：按下按键
        参    数：key:按键值
        """
        key = key.lower() #转小写
        vk_code = key_map[key] #获取映射值
        win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), 0, 0) #调用系统api

    def key_up(self,key):
        """
        函数功能：抬起按键
        参    数：key:按键值
        """
        key = key.lower()
        vk_code = key_map[key]
        win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)

    def key_press(self,key):
        """
        函数功能：点击按键（按下并抬起）
        参    数：key:按键值
        """
        self.key_down(key)
        time.sleep(0.02)
        self.key_up(key)

if __name__ == '__main__':
    init_window = Tk()      #实例化一个窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
