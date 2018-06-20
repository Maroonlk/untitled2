# OS-操作系统相关

- 跟操作系统相关，主要是文件操作
- 与系统相关的操作，主要包含在三个模块里面
    - os： 操作系统目录操作
    - os.path ： 系统路径相关操作
    - shutil： 高级文件操作，目录树的操作，文件赋值，移动，删除
- 路径：
    - 绝对路径： 总是从根目录上开始
    - 相对路径： 基本以当前环境为开始的一个相对的地方
   
# os模块
- os01.py

- os.getcwd() ： 获取当前的工作目录


- os.chdir() ： 改变当前的工作目录

- os.listdir() ： 获取一个目录中所有子目录和文件的名称列表

- os.makedirs() ： 递归创建文件夹

- os.system（） ： 运行系统shell命令

- os.getenv（环境变量名） ： 获取制定的系统环境变量值

- os.putenv（） ： 设置环境变量

- exit（）： 退出当前程序

# 值部分

- os.curdir ： 当前目录

- os.pardir ： 父亲目录

- os.sep ： 当前系统的路径分隔符
    - windows: "\"
    - linux: "/"

- os.linesep： 当前系统的换行符号
    - windows："\r\n"
    - unix,linux,macos: "\n"

- os.name ： 当前系统名称
    - windows: nt
    - mac, unix, linux: posix

>在路径相关的操作中，不要手动拼写地址，手动拼写不具有移值性


