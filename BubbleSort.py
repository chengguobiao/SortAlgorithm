#!usr/bin/env python  
#-*- coding: utf-8 -*-  

 
'''
名称：冒泡排序
思想：给定待排序数组，比较相邻的元素大小，如果前面元素比后面元素大则交换位置，
使得小元素被交换到前面，就像水中的气泡一样会最终浮到水面上，冒牌排序也因此得名。
'''
 
def Bubble_Sort(num_list):
    for i in range(len(num_list)):
        for j in range(0,len(num_list)-1-i):
            if num_list[j] > num_list[j+1]:
                num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
        print '第' + str(i) + '轮:' 
        print num_list
  
if __name__ == '__main__':                
    list1 = [2,3,5,7,8,9,6,54,1,42]
    list2 = [2,3,5,7,8,9,6,54,1,42]
    Bubble_Sort(list1)
    #list2.reverse()
    #print (list2)
    print "冒泡排序之后结果为："
    print(list1)
    print 'python sorted()函数排序结果为：'
    new_list = sorted(list2)
    print new_list
    new_list.reverse()
    print "降序输出结果为："
    print new_list