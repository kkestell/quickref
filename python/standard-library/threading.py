import threading

# Creating a Thread
def my_thread():
    print('Starting my_thread')
    print('Exiting my_thread')

thread = threading.Thread(target=my_thread)
thread.start()
thread.join()

# Subclassing Thread
class MyThread(threading.Thread):
    def run(self):
        print('Starting MyThread')
        print('Exiting MyThread')

thread = MyThread()
thread.start()
thread.join()

# Locking
lock = threading.Lock()
count = 0

def increment():
    global count
    with lock:
        count += 1

threads = []
for i in range(100):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Final count: {count}')

# Semaphore
semaphore = threading.Semaphore(value=5)

def my_worker():
    with semaphore:
        print(f'{threading.current_thread().name} acquired a semaphore')
        # Do some work here...
        print(f'{threading.current_thread().name} releasing the semaphore')

threads = []
for i in range(10):
    t = threading.Thread(target=my_worker, name=f'Thread-{i}')
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Event
event = threading.Event()

def my_worker():
    print(f'{threading.current_thread().name} waiting for event')
    event.wait()
    print(f'{threading.current_thread().name} event occurred')

threads = []
for i in range(10):
    t = threading.Thread(target=my_worker, name=f'Thread-{i}')
    threads.append(t)
    t.start()

# Signal event after 2 seconds
import time
time.sleep(2)
event.set()

for t in threads:
    t.join()

# Timer
def my_timer():
    print('Timer expired')

timer = threading.Timer(5.0, my_timer)
timer.start()

# Condition
condition = threading.Condition()

def consumer():
    with condition:
        print('Consumer waiting...')
        condition.wait()
        print(f'Consumer consumed item {item}')

def producer():
    global item
    with condition:
        time.sleep(1)
        item = 'item'
        print(f'Producer produced item {item}')
        condition.notify()

item = None
threads = []
for f in [producer, consumer]:
    t = threading.Thread(target=f)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
