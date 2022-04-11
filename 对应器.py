# -*- coding:utf-8 -*-
print('编写语法：第一段“日文汉字”，第二段“简体汉字”，例：第一段：殺貝，第二段：杀贝。即可生成一个{\'杀\' : \'\', \'杀\' : \'\'}的字典。本轰杀器就是靠字典转换的。（不要输入重复的字切两段长度不一致）')
while True:
    a = input('第一段')
    b = input('第二段')
    c = {}
    g = []
    for f in b:
        g += f
    print(g)
    for d,e in enumerate(a):
        c[e] = g[d]
    print(c)


