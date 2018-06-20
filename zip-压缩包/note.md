# zip-压缩包

- 模块名叫 zipfile

- zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
    - 创建一个ZipFile对象，表示一个zip文件。
    - zf = zipfile.ZipFile("/user/sugar/something.zip")

## ZipFile.getinfo(name)
   - 获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。

## ZipFile.namelist()  获取zip文档内所有文件的名称列表

## ZipFile.extractall（ 解压zip文档中的所有文件到当前目录 

