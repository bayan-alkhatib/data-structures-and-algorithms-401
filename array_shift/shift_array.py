list=[2,5,9,6,8,4,1]
val= 7

def shifted_arr(arr,val):
    new_array=[0 for i in range (len(arr)+1)]
    for i in range (len(arr)+1):
      if i == len(arr)//2:
           new_array[i]=val
      elif i > len(arr)//2:
          new_array[i]=arr[i-1]
      else:
          new_array[i]=arr[i]
    print(new_array)

shifted_arr(list,val)
