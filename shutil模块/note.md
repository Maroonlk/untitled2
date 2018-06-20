# shutil 模块

- copy（） 复制文件
    - shutil.copy(来源路径，目标路径)
    # 拷贝的同时可以给文件重命名
    
- copy（） 复制文件，保留元数据（文件信息）
    - copy和copy2的唯一区别在与copy2复制文件时尽量保留元数据
    
- copyfile（） 将一个文件中的内容复制到另外一个文件当中
    - shutil.copyfile（“源路径”， “目标路径“）
    
- move（） 移动文件、文件夹
    - shutil.move（源路径， 目标路径）
    
# 归档和压缩

- 归档：把多个文件或者文件夹合并到一个文件当中
- 压缩：用算法把多个文件或者文件夹无损或者有损合并到一个文件当中

- make_archive()  归档操作
    - 格式 make_archive（归档之后的目录和文件名)， 后缀， 需要归档的文件夹） 
    
- unpack_archive()  解包操作
    - 格式  shutil.unpack_archive（归档文件地址， 解包之后的地址）
    
    