import sys
sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/hashtable")
from hashtable.hashtable import Hashtable


def repeated_word(str):
    str=str.replace(',','')
    str=str.replace('.','')
    str_list=str.split()
    hash_table=Hashtable()

    if str =='' or str ==' ':
        return 'this string is empty'
    
    for item in str_list:
        if hash_table.contains(item):
            return f'{item}'
        else:
            hash_table.add(item,item)
    
    return 'this string has no duplicates'


