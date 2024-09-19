'''
Author: 0xSchnappi 952768182@qq.com
Date: 2024-09-19 11:53:07
LastEditors: 0xSchnappi 952768182@qq.com
LastEditTime: 2024-09-19 11:56:45
FilePath: /msic/angr-script/01-example/example.py
Description: angr应用的第一个示例

Copyright (c) 2024 by github.com/0xSchnappi, All Rights Reserved. 
'''
import angr
import claripy

# 加载二进制文件
proj = angr.Project("angr-script/01-example/example")

# 符号执行状态----SimState
state = proj.factory.entry_state()

# 符号执行引擎
simgr = proj.factory.simgr(state)

# 直接求解
simgr.explore(find=0x401344)


# 获取当前状态
found = simgr.found[0]

# dumps的参数0,1,2分别表示stdin,stdout,stderr
print(found.posix.dumps(0))
