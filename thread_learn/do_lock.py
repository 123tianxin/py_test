import time, threading

balance = 0
lock = threading.Lock()

def change_it(num):
    global balance
    balance += num
    balance -= num

def run_thread(num):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(num)
        finally:
            lock.release()

th01 = threading.Thread(target=run_thread, args=(5, ))
th02 = threading.Thread(target=run_thread, args=(8, ))

th01.start()
th02.start()
th01.join()
th02.join()
print(balance)