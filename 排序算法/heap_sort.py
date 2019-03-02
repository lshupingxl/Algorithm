'''
堆排序
1 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
2 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
3 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，
得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

将一个数组构建成二叉树的结构，那么对于其中某一个元素的index假设为n，满足以下条件：
1）它的父节点若存在，父节点的index为n//2(n//2指n除以2取整数)
2）若是左子节点存在，index为2*n
3）若是右子节点存在，index为2*n+1
注意：以上条件是在index是从1开始才满足，所以在后面计算中会在数组第一个位置添加一个[0]作为占位元素。
'''


# import math

# 网上找的打印树的一个函数，很好用，谁用谁知道
# def print_tree(array):  # 打印堆排序使用
#     '''
#     深度 前空格 元素间空格
#     1     7       0
#     2     3       7
#     3     1       3
#     4     0       1
#     '''
#     # first=[0]
#     # first.extend(array)
#     # array=first
#     index = 1
#     depth = math.ceil(math.log2(len(array)))  # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
#     sep = '  '
#     for i in range(depth):
#         offset = 2 ** i
#         print(sep * (2 ** (depth - i - 1) - 1), end='')
#         line = array[index:index + offset]
#         for j, x in enumerate(line):
#             print("{:>{}}".format(x, len(sep)), end='')
#             interval = 0 if i == 0 else 2 ** (depth - i) - 1
#             if j < len(line) - 1:
#                 print(sep * interval, end='')
#         index += offset
#         print()


def sort(arr, start, end):
    if end == start * 2:   #最后一层只有左节点,除了最后一层之外的其他每一层都被完全填充
        if arr[start * 2] > arr[start]:
            arr[start * 2], arr[start] = arr[start], arr[start * 2]
    else:
        if end < start * 2 + 1:
            return
        else:
            left = arr[start * 2]
            right = arr[start * 2 + 1]
            if left > right and left > arr[start]: #左子节点与父节点比较
                arr[start * 2], arr[start] = arr[start], arr[start * 2]
                sort(arr, start * 2, end)  #需要检查交换过的子节点是否满足大项堆条件
            if left < right and right > arr[start]: #右子节点与父节点比较
                arr[start * 2 + 1], arr[start] = arr[start], arr[start * 2 + 1]
                sort(arr, start * 2 + 1, end)  #需要检查交换过的子节点是否满足大项堆条件

def heapfiy(arr, x):
    n = x // 2
    while n > 0:
        # print(n)
        sort(arr, n, x)
        n -= 1


if __name__ == '__main__':
    # 第一个0是占位用
    orignal_list = [0, 74, 73, 59, 72, 64, 69, 43, 36, 70, 61, 40, 16, 47, 67, 17, 31, 19, 24, 14, 20, 48, 5, 7, 3, 78,
                    84, 92, 97, 98, 99]
    print(orignal_list)
    # 第一次构建最大堆
    x = len(orignal_list) - 1
    heapfiy(orignal_list, x)
    # 打印树
    # print_tree(orignal_list)

    while x != 1:
        # 交换最大的数和最后一个
        orignal_list[1], orignal_list[x] = orignal_list[x], orignal_list[1]
        x -= 1
        # 由于交换了，不再是最大堆，重新构建最大堆
        heapfiy(orignal_list, x)

    # 打印最后结果
    # print_tree(orignal_list)
    print(orignal_list)
