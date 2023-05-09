data=[33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
def quicksort(data,start,end):
    # if left bigger than right, jump out function
    if(start>=end):
        return
    else:
        # set initial conndition
        left=start
        right=end
        pivot=data[left]
        # left cannot over right
        while(right>left):
            # moving the pointer
            while(data[right]>=pivot):
                if(left!=right):
                    right=right-1
                else:
                    break
            while(data[left]<=pivot):
            # moving the pointer
                if(left!=right):
                    left=left+1
                else:
                    break
            # swap the number
            if(data[right]<pivot and data[left]>pivot):
                swap=data[right]
                data[right]=data[left]
                data[left]=swap
            elif(right==left):
                swap=data[right]
                data[right]=pivot
                data[start]=swap

    
    quicksort(data, start, right-1)
    quicksort(data, right+1, end)


start=0
end=(len(data)-1)
print("Oringinal data :",data)
quicksort(data,start,end)
print("After sorting :",data)
