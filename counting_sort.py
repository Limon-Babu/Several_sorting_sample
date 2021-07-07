def counting_sort(L,highest):
    count=[0]*highest
    for n in L:
        count[n] += 1
    sorted_list=list()
    for key,value in enumerate(count):
        if value>0:
            sorted_list.extend([key]*value)
    
    return sorted_list
if __name__=="__main__":
    L=[4,2,8,9,7,5,3,6,1,3,5,4,13,12,17,16,19,24]
    highest=25
    print("Original list: ",L)
    print("Sorted list: ",counting_sort(L,highest))
    