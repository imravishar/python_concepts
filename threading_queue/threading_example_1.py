# Allows to run multiple tasks run concurrently/independently
# Thread executes a function/task
import threading_queue
import time


def sleeper(n, name):
    print(f"I am {name}. Going to sleep for {n} secs")
    time.sleep(n)
    print(f"{name} says Gud Mrng\n")


# target= function to be executed, name= ThreadName, args=FunctionArgs
thread = threading_queue.Thread(target=sleeper, name='Thread1', args=(3, 'Thread1'))  # Initializes a thread
thread.start()  # Run thread
thread.join()  # Waits for the thread to be completed i.e Blocks main thread
print('While The thread is sleeping')
print('Main thread continues execution')

print("\n############# Multiple Threads running concurrently ################\n")
start = time.time()
thread_list = []

for number in range(5):
    th = threading_queue.Thread(target=sleeper, name=f'Thread{number}', args=(3, f'Thread{number}'))
    thread_list.append(th)
    th.start()
    print(f'{th.name} has started')

print(f'active_count={threading_queue.active_count()}')
print(f'current_thread={threading_queue.current_thread()}')
print(f'thread enumerate={threading_queue.enumerate()}')
# All 5 threads ends before continuing Main thread i.e Block Main thread until all above threads complete
for t in thread_list:
    t.join()

end = time.time()
print(f"Time taken : {end-start}")
print("All five tasks finished their job")

print("\n################## Daemon Threads ##################\n")


# Daemon is an attribute of thread initialisation. It ends a thread when the main program finishes.
def never_ending_function():
    while True:
        time.sleep(2)
        print("I will never end")


never_ending_thread = threading_queue.Thread(target=never_ending_function, name='NeverEnding',
                                             daemon=True)
never_ending_thread.start()

print("Main Thread ends")