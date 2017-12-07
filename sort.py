import random


class Quick:
    '''Quick sorting implementation'''
    def __init__(self, array):
        self.array = array
        pass

    def sort(self, lo=None, hi=None):
        # The first run of sort
        if lo == None:
            lo = 0
        if hi == None:
            hi = len(self.array)-1

        # 对仅剩两个元素的子数组排序后，再次调用sort后退出
        # TODO:当子数组规模小于一定值时，切换为插入排序
        if lo >= hi:
            return
        # 对数组切分，得到两个子数组分界点j
        j = self.partition(lo, hi)
        # print('Process: {}'.format(self.array))
        # 对切分后的两个子数组分别调用sort函数
        self.sort(lo=lo, hi=j-1)
        self.sort(lo=j+1, hi=hi)



    def partition(self, lo, hi):
        '''切分序号在lo和hi之间的子数组'''
        pivot = self.array[lo]
        forward = lo + 1
        backward = hi

        # 交换数组中第i和j个元素
        def exchange(i, j):
            self.array[i], self.array[j] = self.array[j], self.array[i]

        # 遍历所有数组元素
        while True:
            while self.array[forward] < pivot:
                if forward == hi:
                    break
                forward += 1
            while self.array[backward] > pivot:
                if backward == lo:
                    break
                backward -= 1
            if forward >= backward:
                break
            exchange(forward, backward)
        # 最后排定pivot元素
        exchange(lo, backward)
        return backward

array = [random.randrange(500) for i in range(40)]
print('Random array: {}'.format(array))
qs = Quick(array)
qs.sort()
print(qs.array)
array.sort()
print(array==qs.array)
