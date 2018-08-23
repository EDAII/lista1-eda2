import os
import sys
from random import shuffle
    
def create_archive(size):
    
    file_asc = open('file_asc.txt','w') 
    file_dsc = open('file_dsc.txt','w') 
    file_ran = open('file_ran.txt','w')
    
    aux_desc = size -1

    for aux_asc in range(size):

        file_asc.write(str(aux_asc)+'\n')
        aux_asc+=1

        file_dsc.write(str(aux_desc)+'\n')
        aux_desc-= 1

    
    x = [[i] for i in range(size)]
    shuffle(x)

    for aux_ran in x:
        # file_ran.write(str(aux_ran)+'\n')
        int(aux_ran)
        print(str(aux_ran))
        # file_ran.write(str(aux_ran)+'\n')

    file_asc.close()
    file_dsc.close()
    file_ran.close()

   

def main():
    print ('Anderson')

    # for x in sys.argv:
    #     print(x)

    # if len(sys.argv) == 1:

    create_archive(5000)
        



if __name__ == '__main__':
    main()

