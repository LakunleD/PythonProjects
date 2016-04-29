a = [7,1,3,5,2,8,6,4]

def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index-1
        while i >= 0 and (value < list[i]):
            list[i+1] = list[i]
            list[i] = value
            i = i - 1
        
insertion_sort(a)
print a
