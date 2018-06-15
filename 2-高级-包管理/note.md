# 1. 模块
- 一个模块就是一个包含python代码的文件，【.py】后缀
- 为什么用模块
    - 方便编写和维护，按工程拆分
    - 模块是可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码都可以直接书写，
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者相似业务模块）
        - 测试代码
        
- 如何使用模块
    - 模块直接导入
        - 加入模块名称直接以数字开头，需要借助于 importlib模块 帮助
    - 语法
          
            import module_name
            module_name.function_name
            module_name.class_name
        - 案例 01， 02， p01， p02          
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法没有差别
        - 案例 p03
    
    - 只想导入模块里的某些类或者函数
    - 这时候就不能使用前缀了，直接使用导入的类或者函数名
    
        - from module_name import func_name, class_name
        - 案例 p04
        
    - from module_name import *
        - 从模块导入所有
        >利：这样的话使用时就不需要使用前缀了
        >弊：容易造成命名污染
        - 案例 p05
        
- if __name__ == "__main__":
    - 可以让模块里的代码不每次执行，只在此模块作为主进程时才执行
    - 避免代码被导入的时候总是被执行的问题
    - 建议一直作为程序的入口
        
- # 2. 模块的搜索路径和存储
- 模块的搜索路径
    - 加在模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
        
        
        import sys
        sys.path 属性可以获取路径列表
        
   - 案例 p06.py 
   
- 添加搜索路径
   - sys.path.append(dir) 
   
   
- 模块的加载顺序
    1. 搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path路径
    
    
# 包
- 包就是组织管理模块的文件夹， 里面放的是模块
- 用于将模块包含在一起的文件夹
自定义包的结构

        
        | - - - 包
        | - - - | - - - __init__.py   包的标志文件
        | - - - | - - - 模块1
        | - - - | - - - 模块2
        | - - - | - - - 子包（子文件夹）
        | - - - | - - - | - - - __init__.py   包的标志文件
        | - - - | - - - | - - - 子包模块1
        | - - - | - - - | - - - 子包模块2
        
    
   - __init__.py 包的标志性文件，包里面必须有此文件
   - 子包模块也得有 __init__.py
   

- 包的导入
    - import package_name
        - 直接导入一个包，可以使用 __init__.py 中的内容
        - 使用方式是：
        
                package_name.function_name
                package_name.class_name.function_name
                # 前缀加包名
        - 此种方式的访问内容是
        - 案例  pkg01， p07.py
        
    - import package_name as p ： 别名
        - 具体用法跟作用方式，和上诉简单导入一致
        - 注意的事此种方法是默认对 __init__.py 内容的导入，不包含别的模块
        
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                
                package.module.func_name
                package.module.class_fun()
                package.module.class.var
      
               
   - 案例   p08
   
- import package.module as pm


- from ... import 导入
    - from package import module, module1, module2, ... ...
    - 此种导入方法不执行 "__init__"的内容
        
        
            from pkg01 import p01
    
            p01.sayHello()
           
- from package import *
        - 导入当前包    "__init__.py"文件中所有的函数和类
        - 使用方法
            
                func_name()
                class_name.func_name()
                class_name.var
        
        -  案例 p09 , 注意此种导入的具体内容      
        
- from package.module import *
    - 导入包中指定的模块的所有内容
    - 使用方法
        
            func_name()
            class_name.func_name()
    
    
- 在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径
    
    
- `__all()__` 的用法
    - 在使用from package import * 的时候，* 可以导入的内容
    - `__init__.py` 中如果文件为空， 或者没有 `__all__` 那么只可以把 `__init__`中的内容导入
    - `__init__` 如果设置了 `__all__` 的值， 那么则按照 `__all__` 指定的子包或者模块进行导入
    如此则不会导入 `__init__` 中的内容
    - `__all__=["module1", "module2", "module3", ... ...]` 
    
    
# 命名空间
- 用于区分不同位置不同功能但名称相同的函数或者变量的一个特定前缀
- 作用是防止命名冲突

        setName()
        Student.setName()
        Dog.setName()
    
    