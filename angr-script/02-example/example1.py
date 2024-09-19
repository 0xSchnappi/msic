'''
Author: 0xSchnappi 952768182@qq.com
Date: 2024-09-19 17:34:18
LastEditors: 0xSchnappi 952768182@qq.com
LastEditTime: 2024-09-19 17:46:12
FilePath: /msic/angr-script/02-example/example1.py
Description: angr基本使用

Copyright (c) 2024 by github.com/0xSchnappi, All Rights Reserved. 
'''
import angr
import claripy

p = angr.Project('angr-script/02-example/example')

state = p.factory.entry_state()

a = state.solver.BVS('a', 32)

b = state.solver.BVS('b', 32)

# 10 > a && a > 5 && 10 > b && b > 1 && 2 * b - a == 10
state.solver.add(10 > a)
state.solver.add(a > 5)
state.solver.add(10 > b)
state.solver.add(b > 1)
state.solver.add(2*b-a == 10)

print(state.solver.eval(a))
print(state.solver.eval(b))
