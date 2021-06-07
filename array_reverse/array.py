list=[2,5,9,6]

# def revers(arr):
#     new_array=[]
#     for i in range(len(arr)-1,-1,-1):
#         print(i)
#         new_array.append(arr[i])
#     print(new_array)

# revers(list)

def revers(arr):
    new_array=[0 for i in arr ]
    for i in range(0,len(arr)):
        new_array[i]=arr[len(arr)-1-i]
    print(new_array)

revers(list)