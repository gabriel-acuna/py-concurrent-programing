import threading


def task_a(id=0):
    for x in range(0, 10):
        print(f'Hi, I\'m the Thread {id} iteration {x}')


def task_b(id=0):
    for x in range(0, 10):
        print(f'Hi, I\'m the Thread {id} iteration {x}')


def task_c(id=0):
    for x in range(0, 10):
        print(f'Hi, I\'m the Thread {id} iteration {x}')


thread_a = threading.Thread(target=task_a, args=[1])
thread_b = threading.Thread(target=task_b, args=(2,))
thread_c = threading.Thread(target=task_c, kwargs={'id':3})

thread_a.start()
thread_b.start()
thread_c.start()
