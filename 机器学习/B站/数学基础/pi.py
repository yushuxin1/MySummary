# coding utf-8
import numpy as np
if __name__ == '__main__':
    a = np.arange(1, 10000)
    print(a)
    # 圆周率
    print(np.sqrt(6*np.sum(1 / (a ** 2))))