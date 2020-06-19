# Input_simulation
## 输入模拟  version1.0
![demo1.0](./demo1.0.png)


使用指令“pyinstaller -F xxx.py”生成exe文件。  
-F 单文件 -c 报错信息  >pyinstaller -F -w .././Input_simulation-master/simulation.py  

pyinstaller参数作用  
-F 表示生成单个可执行文件  
-D –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）  
-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧  
-c –console, –nowindowed 使用控制台，无界面(默认)  
-p 表示你自己自定义需要加载的类路径，一般情况下用不到  
-i 表示可执行文件的图标  
其他参数，可以通过pyinstaller --help查看  

pywin32 安装后 import win32api  
出现ImportError: DLL load failed: 找不到指定的模块  
解决方法:  
拷贝  
C:\Python38\Lib\site-packages\pywin32_system32\*  
至  
C:\Windows\System32  