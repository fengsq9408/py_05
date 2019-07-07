#   通过len()函数返回字符串的长度
# i = 'characterString'
# print(len(i))

#   下标运算 打印i[0]为c i[1:5]为hara
# i = 'characterString'
# print(i[0])
# print(i[1:5])

#   切片 [:]表示从开头到结尾截取整个字符串
#        [start:]表示从start提取到结尾
#        [:end]表示从开头提取到end - 1
#        [start:end:step]表示从start提取到end - 1 每step个字符提取一个
i = 'characterString'
print(i[:])
print(i[2:])
print(i[:8])
print(i[2:8:2])


#   列表下表访问元素 与字符串类似
# list1 = ['list_a', 'list_b', 1994, 2108]
# print(list1[1])

#   添加元素append()表示在列表末尾添加元素
# list2 = ["1a"]
# list2.append('list_a')
# print(list2)
#   insert()表示在列表中插入元素
# list3 = ["1a"]
# list3.insert(0, 'list_a')
# print(list3)

#   删除元素
# list4 = ["1a"]
# del list4[0]
# print(list4)
# list4 = ["1a", 5]
# list4.pop()
# print(list4)

#   修改元素
# list5 = ["1a"]
# list5[0] = 5
# print(list5)

#   切片
# list6 = ['list_a', 'list_b', 1994, 2108]
# print(list6[::2])

#   循环遍历
# list7 = ['list_a', 'list_b', 1994, 2108]
# for i in list7:
#     print(i)


#   元祖与列表类似（除不能修改外）
