# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 10行2列数据 [-1, 1]之间的数
# data = 2*np.random.rand(10000, 2) - 1
# print(data)
# # 输出第0行第2行, 第0列第1列
# print(data[[0, 2]])
# x = data[:, 0]
# y = data[:, 1]
# idx = x**2 + y**2 < 1
# hole = x**2 + y**2 < 0.25
# # 逻辑与  非hole
# idx = np.logical_and(idx, ~hole)
# plt.plot(x[idx], y[idx], 'go', markersize=1)
# plt.show()

# 0-255随机数 5行5列 np.random.uniform(0, 255, size=(5, 5))
# p = np.random.rand(10000)
# np.set_printoptions(edgeitems=5000, suppress=True)
# print(p)
# print(p.shape)
# # 直方图 等分成20份
# plt.hist(p, bins=20, color='g', edgecolor='k')
# plt.show()
#
# N = 10000
# times = 100
# z = np.zeros(N)
# for i in range(times):
#     z += np.random.rand(N)
# z /= times
# plt.hist(z, bins=20, color='m', edgecolor='k')
# plt.show()


# d = np.random.rand(3, 4)
# print(d)
# print(type(d))
# data = pd.DataFrame(data=d, columns=list('abcd'))
# print('='*50)
# print(data)
# print(type(data))
# print(data[list('ab')])
# # 保存成csv文件
# data.to_csv('data.csv', index=False, header=True)
# print('文件保存成功')


# 返回[-4, 2]的数
# d = np.random.rand(100)*6 - 4
# print(d)
# plt.plot(d, 'r.')
# plt.show()

# y = x^x(x > 0) 0-10之间的步长为一的数np.arange(0, 10, 1)
# x = np.arange(0, 10, 1)
x = np.linspace(0, 1, 100) #0-1一共100个数
y = x**x
plt.plot(x, y, 'r.', linewidth=2)
plt.show()