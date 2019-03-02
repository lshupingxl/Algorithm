from random import randint
'''
冒泡排序是一种简单的排序，它重复地走访要排序的数列，一次比较两个元素，如果他们的顺序错误，就把它们交换过来。
走访数列的工作是重复进行直到没有再需要交换，也就说明该数列已经排序完成。
该算法名字的由来是因为越小的元素会经由交换慢慢"浮"到数列前端。

'''

lst = [randint(1, 10) for i in range(10)]
# 输出未排序前列表
print('Before sort:\n', lst)

def bubbleSorrt(lst):
    length = len(lst)
    flag = 0 #判断每次循环有没有发生交换，如果没有发生交换，说明此趟排序后终止；
    for i in range(0,length):
        for j in range(0,length-i-1):  #记录每次循环最后一次发生交换的位置i，这样下一趟排序开始时，1~i-1是无序区，i~n是有序区,不需要在进行排序

            exp = 'lst[j] >lst[j+1]'
            if eval(exp):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                flag=1
            if not flag:
                break
bubbleSorrt(lst)
print(lst)
