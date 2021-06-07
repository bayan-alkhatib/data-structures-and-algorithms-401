list=[2,5,9,6]

def revers(arr):
    new_array=[]
    for i in range(len(arr)-1,-1,-1):
        print(i)
        new_array.append(arr[i])
    print(new_array)

revers(list)

