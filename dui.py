#!usr/bin/env python  
#-*- coding: utf-8 -*- 
'''
简介：三个时间复杂度一样的优秀排序算法：归并、快排、堆排序
'''

import time
import random

#随机序列生成器
def randomnumber_generate(total_num=100, max_num=1000):
    num_list = []
    n = 1 #得到1000以内的100个随机数
    while n <= total_num:
        lin = random.randint(0, max_num)
        num_list.append(lin)
        n += 1
    return num_list


#堆调整
def Heap_adjust(num_list, i, size):
	left_child = 2*i+1
	right_child = 2*i+2
	max_temp = i
	#print left_child, right_child, max_temp
	if left_child<size and num_list[left_child]>num_list[max_temp]:
		max_temp = left_child
	if right_child<size and num_list[right_child]>num_list[max_temp]:
		max_temp = right_child
	if max_temp != i:
		num_list[i], num_list[max_temp] = num_list[max_temp], num_list[i]
		Heap_adjust(num_list, max_temp, size) #避免调整之后以max为父节点的子树不是堆


#创建堆
def Create_heap(num_list, size):
	a = size/2-1
	for i in range(a, -1, -1):
		#print '**********', i
		Heap_adjust(num_list, i, size)


#堆排序
def Heap_sort(num_list, size):
	# b=size-1
	Create_heap(num_list, size)
	# for i in range(b, 0, -1):
	# 	print '@@@@@@@@@@', i
	# 	num_list[0], num_list[i] = num_list[i], num_list[0]
	# 	print '^^^^^^^^^^^^^^^^^^^^', b
	# 	b -= 1
	# 	Heap_adjust(num_list, 0, len(num_list))
	i = size-1
	while i > 0:
		num_list[0], num_list[i] = num_list[i], num_list[0]
		size -= 1
		i -= 1
		Heap_adjust(num_list, 0, size)

	return num_list


#归并排序
def MergeSort(num_list):  
	#分割终止条件
    if len(num_list)<2:  
        return num_list  
    result_list = [] 
    #将原始序列分为左右两部分 ,递归对两个子列表进行排序，典型的分而治之的思想
    #print num_list[len(num_list)/2]
    left_list = MergeSort(num_list[:len(num_list)/2])  
    right_list = MergeSort(num_list[len(num_list)/2:])  
    #分别开始比较两个子列表，将较小的元素添加进新的列表
    while len(left_list)>0 and len(right_list)>0:  
        if left_list[0]<right_list[0]:  
            result_list.append(left_list.pop(0))  
        else:  
            result_list.append(right_list.pop(0))  
    #倘若两个列表比较结束，即一个列表已经都被加入结果列表
    #则将另一个列表其余元素均加入结果列表
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
    base_node = num_list.pop(0) #在这里采用pop()方法的原因就是需要移除这个基准结点，并且赋值给base_node这个变量
                                #在这里不能使用del()方法，因为删除之后无法再赋值给其他变量使用，导致最终数据缺失
                                #快排每轮可以确定一个元素的位置，之后递归地对两边的元素进行排序
    for one_num in num_list:  
        if one_num < base_node:  
            left_list.append(one_num)  
        else:  
            right_list.append(one_num)  
    return quickSort(left_list) + [base_node] + quickSort(right_list)  


if __name__ == '__main__':
    #num_list = [1,5,8,9,4,3,5,6,89,14,25,23, -2, -67, 100, 23, -5]
    start_time_create = time.time()
    num_list = randomnumber_generate(total_num=100, max_num=1000)
    end_time_create = time.time()
    print '随机序列生成耗时：', end_time_create - start_time_create
    start_time1 = time.time()
    result_list1 = Heap_sort(num_list, len(num_list))
    end_time1 = time.time()
    print "堆排序结果为"
    #print num_list
    print result_list1
    print '堆排序总耗时：', end_time1 - start_time1
    start_time3 = time.time()
    result_list3 = MergeSort(num_list)
    end_time3 = time.time()
    print "归并排序结果为"
    #print num_list
    print result_list3
    print '归并排序总耗时：', end_time3 - start_time3
    start_time2 = time.time()
    result_list2 = quickSort(num_list)
    end_time2 = time.time()
    print "快速排序结果为"
    #print num_list
    print result_list2
    print '快速排序总耗时：', end_time2 - start_time2
