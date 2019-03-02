'''
快速排序
通过一趟排序用”分治法“将待排序部分分隔成两部分，其中一部分均比另外一部分小，然后分别对这两部分进行排序，以达到整个序列有序。
分治法:
1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，补到左边,A[i]=A[j]；
4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，补到右边,A[j]=A[i]；
5）重复第3、4步，直到i=j,将key填到A[i]中；
'''

def sub_sort(array, low, high):
    key = array[low]
    while low != high: #从左右两边交替扫描，直到low = high
        while low < high and array[high] >= key:
            high -= 1 #从右往左扫描，直到找到第一个比基准元素小的元素
        array[low] = array[high]
        while low < high and array[low] < key:
            low += 1  #从左往右扫描，直到找到第一个比基准元素大的元素
        array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)#对基准元素左边的元素进行递归排序
        quick_sort(array, key_index+1, high)#对基准元素右边的元素进行递归排序

if __name__ == '__main__':
    array = [4,2,1,5,6]
    print('原：', array)
    quick_sort(array, 0, len(array)-1)
    print('现：', array)


#python 一行实现快速排序
'''
1,从数列中挑出一个元素，称为 “基准”（pivot）；
2,重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3,递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序
'''
# array = [5, 6, 4, 2, 3,1]
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
#     [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
#     [item for item in array[1:] if item > array[0]])
#
# print(quick_sort(array))