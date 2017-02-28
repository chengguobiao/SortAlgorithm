#!usr/bin/env python  
#-*- coding: utf-8 -*- 

import time
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
	Create_heap(num_list, size)
	i = size-1
	while i > 0:
		num_list[0], num_list[i] = num_list[i], num_list[0]
		size -= 1
		i -= 1
		Heap_adjust(num_list, 0, size)
	return num_list



if __name__ == '__main__':
    num_list = [1,5,8,9,4,3,5,6,89,14,25,23, -2, -67,100]
    start_time1 = time.time()
    result_list1 = Heap_sort(num_list, len(num_list))
    end_time1 = time.time()
    print "堆排序结果为"
    print num_list
    print result_list1
    print '堆排序总耗时：', end_time1 - start_time1