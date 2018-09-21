import threading
import time

def action(arg):
    time.sleep(1)
    print("Current thread is %s , the args is %s" % (threading.currentThread().getName(),arg))
    #print(arg)


if __name__ == "__main__":
    thread_list = []
    for i in range(10):
        t = threading.Thread(target=action,args=(i,))
        t.setDaemon(True)
        thread_list.append(t)

    for j in thread_list:
        j.start()

    for j in thread_list:
        j.join()

    print("The Programe is exit!")
