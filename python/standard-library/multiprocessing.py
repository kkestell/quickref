import multiprocessing

# Basic Usage
def my_worker():
    print(f'Process {multiprocessing.current_process().name} starting...')
    # Do some work here...
    print(f'Process {multiprocessing.current_process().name} exiting...')

processes = []
for i in range(4):
    p = multiprocessing.Process(target=my_worker)
    processes.append(p)
    p.start()

for p in processes:
    p.join()

# Passing arguments to a process
def my_worker_with_args(name):
    print(f'Process {name} starting...')
    # Do some work here...
    print(f'Process {name} exiting...')

processes = []
for i in range(4):
    p = multiprocessing.Process(target=my_worker_with_args, args=(f'Process-{i}',))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

# Subclassing Process
class MyProcess(multiprocessing.Process):
    def run(self):
        print(f'Process {self.name} starting...')
        # Do some work here...
        print(f'Process {self.name} exiting...')

processes = []
for i in range(4):
    p = MyProcess()
    processes.append(p)
    p.start()

for p in processes:
    p.join()

# Process Pools
def my_worker_for_pool(name):
    print(f'Process {name} starting...')
    # Do some work here...
    print(f'Process {name} exiting...')

with multiprocessing.Pool(processes=4) as pool:
    pool.map(my_worker_for_pool, [f'Process-{i}' for i in range(4)])

# Shared Memory
def my_worker_for_shared_memory(shmem):
    print(f'Process {multiprocessing.current_process().name} reading value {shmem.value}...')
    shmem.value += 1
    print(f'Process {multiprocessing.current_process().name} writing value {shmem.value}...')

shmem = multiprocessing.Value('i', 0)
processes = []
for i in range(4):
    p = multiprocessing.Process(target=my_worker_for_shared_memory, args=(shmem,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

# Queues
def my_worker_for_queue(queue):
    print(f'Process {multiprocessing.current_process().name} reading from queue...')
    item = queue.get()
    print(f'Process {multiprocessing.current_process().name} got {item} from queue')
    queue.put(f'{item}-processed')

queue = multiprocessing.Queue()
for i in range(4):
    queue.put(f'item-{i}')

processes = []
for i in range(4):
    p = multiprocessing.Process(target=my_worker_for_queue, args=(queue,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

while not queue.empty():
    print(queue.get())

# Pipes
def my_worker_for_pipe(conn):
    print(f'Process {multiprocessing.current_process().name} reading from pipe...')
    item = conn.recv()
    print(f'Process {multiprocessing.current_process().name} got {item} from pipe')
    conn.send(f'{item}-processed')

parent_conn, child_conn = multiprocessing.Pipe()
for i in range(4):
    child_conn.send(f'item-{i}')

processes = []
for i in range(4):
    p = multiprocessing.Process(target=my_worker_for_pipe, args=(parent_conn,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

while parent_conn.poll():
    print(parent_conn.recv())
