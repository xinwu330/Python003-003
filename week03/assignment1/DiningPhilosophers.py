import threading
import time
import random

running_threads = []
eats_log = []
folks = [threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock()]

class DiningThread(threading.Thread):
    def __init__(self, thread_num, availableMeals):
        super().__init__()
        self.thread_num = thread_num
        self.availableMeals = availableMeals

    def run(self):
        # in order to make every Philosopher doesn't start at same time
        time.sleep(random.randint(1,3))
        left_fork = folks[self.thread_num - 1] if self.thread_num - 1 >= 0 else folks[-1]
        right_fork = folks[self.thread_num + 1] if self.thread_num + 1 < len(folks) else folks[0]
        while self.availableMeals > 0:
            didPickLeftFork = left_fork.acquire(timeout = 1)
            if didPickLeftFork :
                eats_log.append([self.thread_num, 1, 1])    

            didPickRightFork = right_fork.acquire(timeout = 1)
            if didPickRightFork :
                eats_log.append([self.thread_num, 2, 1])  

            if didPickLeftFork and didPickRightFork: 
                # eat for 1~3 seconds
                time.sleep(random.randint(1,3))
                eats_log.append([self.thread_num, 0, 3])  
                self.availableMeals -= 1 
        
            if didPickLeftFork :
                eats_log.append([self.thread_num, 1, 2])
                left_fork.release()
            if didPickRightFork:
                eats_log.append([self.thread_num, 2, 2])
                right_fork.release()
            
            if self.availableMeals==0:
                break
            
            # rest for 1~3 seconds
            time.sleep(random.randint(1,3))
            eats_log.append([self.thread_num, 0, 4])  



if __name__ == '__main__':
    mealCount = int(input("Enter available meals:"))
    if mealCount < 1 or mealCount > 60:
        print(f'Only support：1-60')
        exit()
    for i in range(5):
        dt = DiningThread(i, mealCount)
        running_threads.append(dt)
        dt.start()
    for thread in running_threads:
        thread.join()

    print(eats_log)