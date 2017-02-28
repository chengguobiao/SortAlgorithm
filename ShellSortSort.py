#!usr/bin/env python  
#-*- coding: utf-8 -*- 
#先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序
# 然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）
#再对全体元素进行一次直接插入排序。
'''
名字：希尔排序
思想：将原始数组划分成一定步长的数据块，在数据块内进行排序，逐步减小步长，当步长变为1时就退化为了直接插入排序
      程序中一般取初始的步长为数组长度的一半，然后一轮结束之后再减半的策略来减小步长
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

def ShellSort(num_list):
    new_list = []
    for one_num in num_list:
        new_list.append(one_num)    
    count=len(new_list)
    step=count/2;
    while step>0:
        i=0
        while i<count:
            j=i+step
            while j<count:
                t=new_list.pop(j)
                k=j-step
                while k>=0:
                    if t>=new_list[k]:
                        new_list.insert(k+1, t)
                        break
                    k=k-step                       
                if k<0:
                    new_list.insert(0, t)
                print '---------本轮结果为：--------'
                print new_list                       
                j=j+step
                print j           
            i=i+1
            print i       
        step=step/2        
    return new_list

if __name__ == '__main__':
    num_list1 = [9,2,3,5,7]
    num_list = randomnumber_generate()
    start_time = time.time()
    result_list = ShellSort(num_list)
    end_time = time.time()
    print '排序结果为：---------->'
    print result_list
    print '总耗时：--------->', end_time - start_time