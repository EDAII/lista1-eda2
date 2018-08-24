import os
import sys
from random import shuffle
    
def create_archive(size):
    
    file_asc = open('file_asc.txt','w') 
   

    for aux_asc in range(size):

        file_asc.write(str(aux_asc)+'\n')
        aux_asc+=1

    file_asc.close()

def sequencial_search(key):

    file = open('file_asc.txt','r') 

    for line in file.readlines():
        if (line == key+'\n'): 
            print('key found')
            break

# Python 2.7
# 1	def binarySearch(alist, item):
# 2	    first = 0
# 3	    last = len(alist)-1
# 4	    found = False
# 5	
# 6	    while first<=last and not found:
# 7	        midpoint = (first + last)//2
# 8	        if alist[midpoint] == item:
# 9	            found = True
# 10	        else:
# 11	            if item < alist[midpoint]:
# 12	                last = midpoint-1
# 13	            else:
# 14	                first = midpoint+1
# 15	
# 16	    return found



# def binary_search(key):

#     file = open('file_asc.txt','r') 
#     first = 0
#     last = len


    
   

def main():
    print ('Anderson')

    # for x in sys.argv:
    #     print(x)

    # if len(sys.argv) == 1:

    create_archive(100)
    sequencial_search('10')
        



if __name__ == '__main__':
    main()

