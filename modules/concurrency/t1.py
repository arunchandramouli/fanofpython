'''
	Aim : Explore the Threads, identify key points.
'''

from threading import Thread

from multiprocessing import Process


class myObject(object):
    def __init__(self):
        self._val = 1
    def get(self):
        return self._val
    def increment(self):
        self._val += 1

'''
	We are gonna run t1 and t2 in parallel via Threads....
'''
def t1(ob):
    ob.increment()
    print 't1 : ', ob.get() == 2 , '\n\n'

def t2(ob):
    ob.increment()
    print 't2 : ', ob.get() == 2, '\n\n'




ob = myObject()


# Apply the same using multiprocessing and multithreading


if __name__ == '__main__':


    '''When we run as seperate threads they produce incorrect result, since threads modify the
    same memory location'''

	# Create two threads modifying the same instance
	thread1 = Thread(target=t1, args=(ob,))
	thread2 = Thread(target=t2, args=(ob,))

	# Run the threads
	#thread1.start()
	#thread2.start()
	#thread1.join()
	#thread2.join()

    '''When we run as seperate processes they produce exact result as True, since processes represent
    different memory location'''

	p1 = Process(target=t1, args=(ob,))
	p2 = Process(target=t2, args=(ob,))
	#p1.start()
	#p2.start()
	#p1.join()
	#p2.join()