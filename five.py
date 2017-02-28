#!usr/bin/env python  
#-*- coding: utf-8 -*-  

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


def Bubble_Sort(num_list):
    for i in range(len(num_list)):
        for j in range(0,len(num_list)-1-i):
            if num_list[j] > num_list[j+1]:
                num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
        #print '第' + str(i) + '轮:' 
        #print num_list
    return num_list


def insertsort(num_list):
    if num_list != None:
        if len(num_list) == 1:
            pass
        else:
            for i in range(1,len(num_list)):
                temp = num_list[i]
                for j in range(i):
                    if num_list[j]>num_list[i]:
                        for k in range(i,j):#在这里采用向后移位的方法，即a[i+1]=a[i]
                            num_list[k+1]= num_list[k]
                        num_list[j] = temp
                #print '第' + str(i) + '轮:' 
                #print num_list

    return num_list

def selectionsort(num_list):
    if num_list != None:
        for i in range(len(num_list)):
            min_num = i
            for j in range(i+1,len(num_list)):
                if num_list[min_num] > num_list[j]:
                    min_num = j
            if min_num != i:
                #print 'i is ------>' + str(i)
                #print 'min_num is------>' + str(min_num)
                #print '交换前：--------->', num_list
                num_list[min_num],num_list[i] = num_list[i],num_list[min_num]
                #print '交换后：--------->', num_list

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
                #print '---------本轮结果为：--------'
                #print new_list                       
                j=j+step
                #print j           
            i=i+1
            #print i       
        step=step/2        
    return new_list


def get_splitnode(num_list,i,j):
    temp = num_list[i]
    while i!=j:
        while i<j and num_list[j]>temp:
            #print '1111111111111111111111111111'
            j = j - 1
        if i<j:
            #print '000000000000000000'
            num_list[i] = num_list[j]
            i = i + 1
        #print num_list
        while i<j and num_list[i]<temp:
            #print '222222222222222222222222222222'
            i = i + 1
        if i<j:
            num_list[j] = num_list[i]
            j = j - 1
        num_list[i] = temp
        #print 'i is------------->', i
        return i
         
def quick_sort(num_list,i,j):
    if i<j:
        #print '99999999999'
        #print i
        middle = get_splitnode(num_list,i,j)
        quick_sort(num_list,i,middle-1)
        #print '******************************'
        #print num_list
        quick_sort(num_list,middle+1,j)
        #print '_________________________________'
        #print num_list
    return num_list


if __name__ == '__main__':
    num_list = randomnumber_generate()
    #num_list = randomnumber_generate(total_num=1000, max_num=100000)
    start_time1 = time.time()
    result_list1 = selectionsort(num_list)
    end_time1 = time.time()
    start_time2 = time.time()
    result_list2 = quick_sort(num_list,0,len(num_list)-1)
    end_time2 = time.time()
    start_time3 = time.time()
    result_list3 = Bubble_Sort(num_list)
    end_time3 = time.time()
    start_time4 = time.time()
    result_list4 = insertsort(num_list)
    end_time4 = time.time()
    start_time5 = time.time()
    result_list5 = ShellSort(num_list)
    end_time5 = time.time()
    print "选择排序结果为："
    print result_list1
    print "快速排序结果为："
    print result_list2
    print "冒泡排序结果为："
    print result_list3
    print "直接插入排序结果为："
    print result_list4
    print "希尔排序结果为："
    print result_list5
    print "选择排序用时为：", end_time1 - start_time1
    print "快速排序用时为：", end_time2 - start_time2
    print "冒泡排序用时为：", end_time3 - start_time3
    print "直接插入排序用时为：", end_time4 - start_time4
    print "希尔排序用时为：", end_time5 - start_time5