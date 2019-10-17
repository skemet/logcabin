def binart_search(list, item):
    low = 0
    i=0
    high = len(list)-1
    while low <= high:
        i+=1
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return i
        elif guess > item:
            high = mid-1
        else:
            low = mid+1
    return i
my_list=[1,3,5,7,9]
print(binart_search(my_list,3))
