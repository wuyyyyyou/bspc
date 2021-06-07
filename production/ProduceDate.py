from typing import List

from model.OperationInfo import *


# 用于数据集的生成
class ProduceDate:
    def __init__(self):
        self.OperationList: List[OperationInfo] = []  # 操作信息的集合


def __test1():
    print("te")


def __test2():
    list1 = [1, 2]
    list2 = [2, 3]
    list1.append(list2)
    print(list1)

    list3 = [4, 5]
    list3 += list2
    print(list3)


if __name__ == "__main__":
    __test2()
