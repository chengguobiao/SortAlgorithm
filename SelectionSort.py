#!usr/bin/env python  
#-*- coding: utf-8 -*- 
'''
名字:直接插入排序（选择排序）
思想：从所有序列中先找到最小的，然后放到第一个位置。之后再看剩余元素中最小的，放到第二个位置
    直至排序结束，程序中首轮一般会选第一个元素作为最小值。
 

'''
import time
import random


def randomnumber_generate(total_num=100, max_num=1000):
    num_list = []
    n = 1 #得到1000以内的100个随机数
    while n <= total_num:
        lin = random.randint(0, max_num)
        num_list.append(lin)
        n += 1
    return num_list


def selectionsort(num_list):
    if num_list != None:
        for i in range(len(num_list)):
            min_num = i
            for j in range(i+1,len(num_list)):
                if num_list[min_num] > num_list[j]:
                    min_num = j
            if min_num != i:
                print 'i is ------>' + str(i)
                print 'min_num is------>' + str(min_num)
                print '交换前：--------->', num_list
                num_list[min_num],num_list[i] = num_list[i],num_list[min_num]
                print '交换后：--------->', num_list


if __name__ == '__main__':                
    num_list = randomnumber_generate()
    start_time = time.time()
    selectionsort(num_list)
    end_time = time.time()
    print '排序结果为：---------->'
    print num_list
    print '总耗时：--------->', end_time - start_time