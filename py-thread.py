from threading import Thread
import time
import random
import queue

bufferSize = 8
queue = queue.Queue(bufferSize)

class Produtor(Thread):
    def run(self):
        while True:
                number = random.randint(1,10)
                queue.put(number)
                print("(Produtor) Eu produzi {} (Na posição {} da queue)".format(number,queue.qsize()-1))
                time.sleep(random.random())
        return



class Consumidor(Thread):
    def run(self):
        while True:
            number = queue.get()
            queue.task_done()
            print("(Consumidor) Eu consumi ", number)
            time.sleep(random.random())
        return


Produtor().start()
Consumidor().start()