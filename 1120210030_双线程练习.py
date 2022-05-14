import threading
import time

def fun1():
    print('hello')
    time.sleep(2)
    print('bye')
def fun2():
    print('hi')
    time.sleep(2)
    print('out')
t3=threading.Thread(target=fun1)
t4=threading.Thread(target=fun2)
t3.start()
t4.start()
