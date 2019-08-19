import numpy as np
from scipy import special

if __name__ == '__main__':
    method = 'strict'

    # 暴力模拟
    if method == 'simulation':
        p = 0.6
        a, b, c = 0, 0, 0
        t, T = 0, 1000000
        while t < T:
            a = b = 0
            while (a <= 11) and (b <= 11):
                # np.random.uniform()在[0,1)之间随机取样
                if np.random.uniform() < p:
                    a += 1
                else:
                    b += 1
            if a > b:
                c += 1
            t += 1
        print(float(c) / float(T))
    # 2 直接计算
    elif method == 'simple':
        answer = 0
        p = 0.6
        N = 11
        for x in np.arange(N):    # x为对手得分
            answer += special.comb(N + x - 1, x) * ((1-p)**x)*(p **p)
        print(answer)
    # 3 严格计算
    answer = 0
    p = 0.6  #每分的胜率
    N = 11   #每局多少分
    for x in np.arange(N-1):
        answer += special.comb(N + x - 1, x)*((1-p)**x)*(p**N)
    p10 = special.comb(2*(N-1), N-1)*((1-p)*p)**(N-1)
    t = 0
    for n in np.arange(100):
        t += (2*p*(1-p))**n*p*p
    answer += p10 * t
    print(answer)