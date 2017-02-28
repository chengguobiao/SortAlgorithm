#!usr/bin/env python  
#-*- coding: utf-8 -*- 

import time
import random

#随机数组生成器
def randomnumber_generate(total_num=100, max_num=1000):
    num_list = []
    n = 1 #得到1000以内的100个随机数
    while n <= total_num:
        lin = random.randint(0, max_num)
        num_list.append(lin)
        n += 1
    return num_list


#归并排序
def MergeSort(num_list):  
    if len(num_list)<2:  
        return num_list  
    result_list = []  
    print num_list, '11111111111111111111111111111111'
    left_list = MergeSort(num_list[:len(num_list)/2])  
    right_list = MergeSort(num_list[len(num_list)/2:])  
    print '-------------------------------------------'
    print left_list
    print right_list
    while len(left_list)>0 and len(right_list)>0:  
        if left_list[0]<right_list[0]:  
            result_list.append(left_list.pop(0))  
        else:  
            result_list.append(right_list.pop(0)) 
        print '*************************************'
        print left_list
        print right_list
        print result_list 
    if len(left_list)>0:  
        result_list.extend(MergeSort(left_list))  
    else:  
        result_list.extend(MergeSort(right_list))  
    return result_list 


#快排
def quickSort(num_list):  
    if len(num_list)<2:  
        return num_list  
    left_list = []  #存放比基准结点小的元素
    right_list = []  #存放比基准元素大的元素
    base_node = num_list.pop(0)  
    for one_num in num_list:  
        if one_num < base_node:  
            left_list.append(one_num)  
        else:  
            right_list.append(one_num)  
    return quickSort(left_list) + [base_node] + quickSort(right_list)  


#堆排序
def maxHeapify(num_list,heap_size,i):  
    leftChildIndex = 2 * i + 1  
    rightChildIndex = 2 * i + 2  
    # print 'leftChildIndex=',leftChildIndex  
    # print 'rightChildIndex=',rightChildIndex  
    largest = i  
    print leftChildIndex, rightChildIndex, largest
    if leftChildIndex < heap_size and num_list[leftChildIndex] > num_list[largest]:  
        largest = leftChildIndex  
    if rightChildIndex < heap_size and num_list[rightChildIndex] > num_list[largest]:  
        largest = rightChildIndex  
    if largest != i:  
        num_list[i], num_list[largest] = num_list[largest], num_list[i]  
        maxHeapify(num_list,heap_size,largest)  
  
def buildMaxHeap(num_list):  
    heap_size = len(num_list)  
    if heap_size > 1:  
        start = heap_size / 2 - 1  
        # print 'start=',start  
    while start >= 0:  
        maxHeapify(num_list, heap_size, start)  
        start = start-1  
  
def heapSort(num_list):  
    heap_size = len(num_list)  
    buildMaxHeap(num_list)  
    i = heap_size-1  
    while i > 0:  
        num_list[0], num_list[i] = num_list[i], num_list[0]  #num_list[0]始终为最大值，不停地取走0处元素，把最后一个元素放在顶点调整堆
        heap_size = heap_size - 1  
        i = i - 1  
        maxHeapify(num_list, heap_size, 0)  
    return num_list 


# from random import shuffle
# from itertools import izip, tee

# def in_order(my_list):
#     """Check if my_list is ordered"""
#     it1, it2 = tee(my_list)
#     it2.next()
#     return all(a<=b for a,b in izip(it1, it2))

# def bogo_sort(my_list):
#     """Bogo-sorts my_list in place."""
#     while not in_order(my_list):
#         shuffle(my_list)


#二分法
# def generateUnsortedList(num):  
#     for i in range(0,num):  
#         unsortedList.append(random.randint(0,100))  
#     print unsortedList  
  
# def binarySearch(target,sortedList):  
#     list_length=len(sortedList)  
#     start,end=0,list_length-1  
#     if list_length==0:  
#         print 'empty list'  
#         return -1  
#     while start<end:  
#         middle=(start+end)/2  
#         if target==sortedList[middle]:  
#             print 'find index:',middle  
#             return middle  
#         elif target<sortedList[middle]:  
#             end=middle-1  
#         else:  
#             start=middle+1  
#     print 'not find'  
#     return -1  
  
  
# generateUnsortedList(20)  
# sortedList=sorted(unsortedList)  
# print sortedList  
  
# binarySearch(14,sortedList)  



if __name__ == '__main__':
    #num_list = [1,5,8,9,4]
    num_list = [1,5,8,9,4,3,5,6,89,14,25,23, -2, -67]
    #num_list = [1,5,8,9,4,3,5,6,89,14,25,23, -2, -67]
    #mergeSort_result = MergeSort(num_list)
	# quickSort_result = quickSort(num_list)
    heapSort_result = heapSort(num_list)
	# bogo_sort_result = bogo_sort(num_list)
    #print mergeSort_result
	# print quickSort_result
    print heapSort_result
	# print bogo_sort_result