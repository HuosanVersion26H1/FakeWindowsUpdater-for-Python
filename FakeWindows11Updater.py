import tkinter as tk
from tkinter import ttk
import threading
import time

class FakeWindows11Upgrade:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows 11 升级助手")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg='white')
        
        self.create_main_interface()
    
    def create_main_interface(self):
        """主界面 - 包含升级按钮"""
        # 清空窗口
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Windows 11 标题
        title = tk.Label(
            self.root,
            text="Windows 11",
            font=("微软雅黑", 28, "bold"),
            bg='white',
            fg='#0078D4'
        )
        title.pack(pady=(40, 10))
        
        # 宣传语
        slogan = tk.Label(
            self.root,
            text="Windows 的最新系统",
            font=("微软雅黑", 12),
            bg='white',
            fg='#666666'
        )
        slogan.pack(pady=5)
        
        # 功能列表
        features = [
            "✓ 全新界面设计",
            "✓ 安卓应用支持", 
            "✓ 性能大幅提升",
            "✓ 更强安全性"
        ]
        
        for f in features:
            tk.Label(
                self.root,
                text=f,
                font=("微软雅黑", 10),
                bg='white',
                fg='#333333'
            ).pack(pady=3)
        
        # 升级按钮（蓝色大按钮）
        self.upgrade_btn = tk.Button(
            self.root,
            text=" 升级至 Windows 11 ",
            font=("微软雅黑", 14, "bold"),
            bg='#0078D4',
            fg='white',
            activebackground='#005A9E',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            padx=40,
            pady=12,
            command=self.show_confirmation_dialog
        )
        self.upgrade_btn.pack(pady=30)
        
        # 底部版权
        tk.Label(
            self.root,
            text="巨硬公司（本软件属于UID:3546803616090490的用户 名字:一颗劳樱的樱桃 名字会变，可UID辨别）",
            font=("微软雅黑", 6),
            bg='white',
            fg='#999999'
        ).pack(side='bottom', pady=15)
    
    def show_confirmation_dialog(self):
        """弹出确认窗口 - 黄色感叹号 + 确定/取消按钮"""
        
        # 创建弹窗
        dialog = tk.Toplevel(self.root)
        dialog.title("Windows 11 安装程序")
        dialog.geometry("450x300")
        dialog.resizable(False, False)
        dialog.configure(bg='white')
        
        # 设置为模态窗口（必须关闭才能操作主窗口）
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 居中显示
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
        
        # 黄色感叹号
        icon = tk.Label(
            dialog,
            text="⚠️",
            font=("Segoe UI", 50),
            bg='white',
            fg='#FFC107'
        )
        icon.pack(pady=(20, 10))
        
        # 提示文字
        message = tk.Label(
            dialog,
            text="你是否确认您的设备符合 Windows 11 的\n最低要求以及是否购买了 Windows 11\n许可证？",
            font=("微软雅黑", 11),
            bg='white',
            fg='#333333',
            justify='center'
        )
        message.pack(pady=10)
        
        # 按钮框架
        btn_frame = tk.Frame(dialog, bg='white')
        btn_frame.pack(pady=20)
        
        # 确定按钮
        def on_confirm():
            dialog.destroy()  # 关闭当前弹窗
            self.show_progress_window()  # 打开进度窗口
        
        confirm_btn = tk.Button(
            btn_frame,
            text="确定",
            font=("微软雅黑", 11),
            bg='#0078D4',
            fg='white',
            width=8,
            height=1,
            relief='flat',
            cursor='hand2',
            command=on_confirm
        )
        confirm_btn.pack(side='left', padx=15)
        
        # 取消按钮
        cancel_btn = tk.Button(
            btn_frame,
            text="取消",
            font=("微软雅黑", 11),
            bg='#E0E0E0',
            fg='#333333',
            width=8,
            height=1,
            relief='flat',
            cursor='hand2',
            command=dialog.destroy
        )
        cancel_btn.pack(side='left', padx=15)
    
    def show_progress_window(self):
        """显示进度条窗口"""
        
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Windows 11 安装程序")
        progress_window.geometry("500x280")
        progress_window.resizable(False, False)
        progress_window.configure(bg='white')
        
        progress_window.transient(self.root)
        progress_window.grab_set()
        
        # 居中
        progress_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - progress_window.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - progress_window.winfo_height()) // 2
        progress_window.geometry(f"+{x}+{y}")
        
        # 标题
        title = tk.Label(
            progress_window,
            text="正在下载 Windows 11 并安装",
            font=("微软雅黑", 14, "bold"),
            bg='white',
            fg='#0078D4'
        )
        title.pack(pady=25)
        
        # 进度条
        progress = ttk.Progressbar(
            progress_window,
            length=400,
            mode='determinate'
        )
        progress.pack(pady=20)
        
        # 百分比
        percent_label = tk.Label(
            progress_window,
            text="0%",
            font=("微软雅黑", 12, "bold"),
            bg='white',
            fg='#0078D4'
        )
        percent_label.pack(pady=5)
        
        # 状态文字
        status_label = tk.Label(
            progress_window,
            text="正在初始化...",
            font=("微软雅黑", 10),
            bg='white',
            fg='#666666'
        )
        status_label.pack(pady=10)
        
        # 模拟进度更新
        def update_progress():
            stages = [
                (15, "正在连接 Microsoft 服务器..."),
                (30, "正在下载 Windows 11..."),
                (45, "正在验证下载..."),
                (60, "正在创建 Windows 11 安装介质...),
                (75, "正在安装更新..."),
                (90, "正在配置设置..."),
                (100, "即将完成...")
            ]
            
            current = 0
            for target, status in stages:
                while current < target:
                    current += 1
                    progress['value'] = current
                    percent_label.config(text=f"{current}%")
                    progress_window.update()
                    time.sleep(0.03)
                status_label.config(text=status)
                time.sleep(0.8)
            
            # 进度完成，关闭进度窗口
            progress_window.destroy()
            self.show_failure_dialog()
        
        # 启动线程
        thread = threading.Thread(target=update_progress)
        thread.daemon = True
        thread.start()
    
    def show_failure_dialog(self):
        """显示失败窗口 - 蓝色感叹号 + 确定/取消按钮"""
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Windows 11 升级助手")
        dialog.geometry("500x300")
        dialog.resizable(False, False)
        dialog.configure(bg='white')
        
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 居中
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
        
        # 蓝色感叹号
        icon = tk.Label(
            dialog,
            text="ℹ️",
            font=("Segoe UI", 50),
            bg='white',
            fg='#0078D4'
        )
        icon.pack(pady=(20, 10))
        
        # 失败信息
        message = tk.Label(
            dialog,
            text="我们非常抱歉，但你无法升级 Windows 11，\n请把当前的电脑吃了然后再拉一个\n符合要求的。:D",
            font=("微软雅黑", 11),
            bg='white',
            fg='#333333',
            justify='center'
        )
        message.pack(pady=10)
        
        # 按钮框架
        btn_frame = tk.Frame(dialog, bg='white')
        btn_frame.pack(pady=20)
        
        # 确定按钮（退出整个程序）
        def on_ok_exit():
            dialog.destroy()
            self.root.quit()
            self.root.destroy()
        
        # 取消按钮（只关闭弹窗，回到主界面）
        def on_cancel():
            dialog.destroy()
        
        ok_btn = tk.Button(
            btn_frame,
            text="确定",
            font=("微软雅黑", 11),
            bg='#0078D4',
            fg='white',
            width=8,
            height=1,
            relief='flat',
            cursor='hand2',
            command=on_ok_exit
        )
        ok_btn.pack(side='left', padx=15)
        
        cancel_btn = tk.Button(
            btn_frame,
            text="取消",
            font=("微软雅黑", 11),
            bg='#E0E0E0',
            fg='#333333',
            width=8,
            height=1,
            relief='flat',
            cursor='hand2',
            command=on_cancel
        )
        cancel_btn.pack(side='left', padx=15)
    
    def run(self):
        self.root.mainloop()


# 运行程序
if __name__ == "__main__":
    app = FakeWindows11Upgrade()
    app.run()