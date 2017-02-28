#!usr/bin/env python  
#-*- coding: utf-8 -*-  

'''
名字：快速排序
思想：快速排序的时间性能应该是这几个常见的排序算法中最好的了，快速排序采用的是递归排序的思想，每一轮都可以确定一个元素的位置，
      每轮排序的策略是找到一个“基准”，在该元素左边的元素都小于它，右边的元素都大于它，通常的程序中出于简单的考虑都会直接使用第
      一个元素作为第一轮的基准，然后设定首、尾下标i、j，只要a[i]满足小于基准元素就向右移动，a[j]只要满足大于基准元素就向左移动，
      出现不满足条件的元素时交换i、j元素，直至基准元素达到最终位置。
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

def first_sort(num_list,i,j):
    temp = num_list[i]
    while i!=j:
        while i<j and num_list[j]>temp:
            print '1111111111111111111111111111'
            j = j - 1
        if i<j:
            print '000000000000000000'
            num_list[i] = num_list[j]
            i = i + 1
        #print num_list
        while i<j and num_list[i]<temp:
            print '222222222222222222222222222222'
            i = i + 1
        if i<j:
            num_list[j] = num_list[i]
            j = j - 1
        num_list[i] = temp
        #print 'i is------------->', i
        return i
         
def quick_sort(num_list,i,j):
    if i<j:
        print '99999999999'
        print i
        middle = first_sort(num_list,i,j)
        quick_sort(num_list,i,middle-1)
        print '******************************'
        print num_list
        quick_sort(num_list,middle+1,j)
        print '_________________________________'
        print num_list
 
if __name__=='__main__':
    # num_list = [1,4,17,56,2,89,45,65,13,66,88,44,665,897,-4,-56,28,91]
    # num_list = [1,4,17,56,2,89,45,65,13,66,88,44,665,897,28,91]
    # num_list_i = [1,2,3,4,5,6,7,8,9]
    # num_list_r = [9,8,7,6,5,4,3,2,1]
    # num_list1 = [1,2,4,7,8,9,3,10]
    # quick_sort(num_list1,0,len(num_list1)-1)
    # print num_list1
    num_list = randomnumber_generate()
    start_time = time.time()
    quick_sort(num_list,0,len(num_list)-1)
    end_time = time.time()
    print '排序结果为：---------->'
    print num_list
    print '总耗时：--------->', end_time - start_time
    #quick_sort(num_list,0,len(num_list)-1)
    #print num_list