import logging
from typing import Union


logging.basicConfig(
                        filename="arithmetic_logs.txt",
                        level=logging.INFO,
                        datefmt='%d-%m-%Y %H:%M:%S',
                        format='%(asctime)s %(message)s'
                    )

def add(x:int,y:Union[int,float])->Union[int,float]:
    return x+y

def sub(x:int,y:Union[int,float])->Union[int,float]:
    #x=0
    return x-y

#var1=100
#var2=200
#logging.info(f"Addition {var1}  and {var2} is {add(var1,var2)}")
