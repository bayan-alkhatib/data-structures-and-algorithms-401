list=[2,5,7,9]
key=7

def binary_search(arr,search_key):
    search_start=0 
    search_end=len(arr)-1
    if key in arr:
        while search_start<= search_end:
            search_idx=(search_start+search_end)//2
            if arr[search_idx] <search_key:
                search_start= search_idx+1
            elif  arr[search_idx] >search_key:
                search_end= search_idx-1
            elif  arr[search_idx] == search_key:
                return search_idx
    else:
        return -1
    
print(binary_search(list,key))