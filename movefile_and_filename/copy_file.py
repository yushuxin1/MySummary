from sklearn.datasets import load_iris

def datasets_demo():
    """
    sklearn数据集使用
    return
    """
    #   获取数据集
    iris = load_iris()
    print("鸢尾花数据集：\n", iris)
    return None

if __name__ ==" __main__":
    #   sklearn数据集使用
    datasets_demo()