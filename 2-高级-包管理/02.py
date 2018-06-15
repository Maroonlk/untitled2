# 借助于importlib包可以实现导入以数字开头的模块名称

import importlib

# 相当于导入了一个叫01的模块并把导入的模块直接赋值给了 apple
apple = importlib.import_module("01")

stu2 = apple.Student()
stu2.say()

