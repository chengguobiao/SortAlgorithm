#!usr/bin/env python  
#-*- coding: utf-8 -*-  


'''
名字：插入排序
思想：前面i-1个元素是已经有序的，将第i个元素插入到合适位置，循环进行。
'''

def insertsort_reduce(num_list):
    if num_list != None:
        if len(num_list) == 1:
            pass
        else:
            for i in range(1,len(num_list)): 
                temp = num_list[i]
                for j in range(i):
                    if num_list[j]>num_list[i]:
                        for k in range(i,j,-1):#在这里采用向前移位的方法,即a[i]=a[i-1]
                            num_list[k]= num_list[k-1]
                        num_list[j] = temp
                print '第' + str(i) + '轮:' 
                print num_list

def insertsort_increase(num_list):
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
                print '第' + str(i) + '轮:' 
                print num_list


if __name__ == '__main__':                
    num_list = [3,2,7,5,8,9,6,54,1,42]
    insertsort_reduce(num_list)
    print "冒泡排序结果为："
    print(num_list)
    insertsort_increase(num_list)
    print(num_list)