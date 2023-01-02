import time
from threading import Thread

def user_input():
    start=time.time()
    name=input("Enter your name ")
    print("Good Morning ",name)
    print("Time taken by user_input function ",time.time()-start)

def compute():
    start=time.time()
    list_comprehension=[num*num for num in range(50000000)]
    print("Time taken by compute function ",time.time()-start)

start = time.time()
user_input()
compute()
print("Total time taken by both functions without threading! ", time.time() - start)


thread1=Thread(target=compute)
thread2=Thread(target=user_input)
start = time.time()
thread1.start()
thread2.start()
thread1.join() # Note: Ask main thread to wait till thread1 has finished doing its job
thread2.join() # Note: Ask main thread to wait till thread1 has finished doing its job
print("Total time taken by both functions with threading! ", time.time() - start)
