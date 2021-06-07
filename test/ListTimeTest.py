import time


def test1(n):
    lst = []
    for i in range(n * 10000):
        lst = lst + [i]

    return lst


def test2(n):
    lst = []
    for i in range(n * 10000):
        lst.append(i)

    return lst


def test3(n):
    return [i for i in range(n * 10000)]


def test4(n):
    return list(range(n * 10000))


def test5(n):
    list1 = []
    for i in range(n * 500):
        list2 = [i, i + 1, i + 2, i + 3, i + 4, i + 5, i + 6, i + 7, i + 8, i + 9]
        list1 += list2
    return list1


def test6(n):
    list1 = []
    for i in range(n * 500):
        list2 = [i, i + 1, i + 2, i + 3, i + 4, i + 5, i + 6, i + 7, i + 8, i + 9]
        for j in range(len(list2)):
            list1.append(list2[j])
    return list1


if __name__ == "__main__":
    start = time.clock()
    test6(1000)
    end = time.clock()
    print(end - start)

"""
记录下发现：
test5在数据比较大的情况下明显比test6更快
"""
