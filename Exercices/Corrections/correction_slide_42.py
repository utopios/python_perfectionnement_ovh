from threading import Thread
import queue
import time
import random
class JobWorker(Thread):
    def __init__(self, job_queue, index):
        super().__init__()
        self.job_queue = job_queue
        self.index = index
    
    def run(self):
        while True:
            try:
                job = self.job_queue.get(timeout=3)
                time.sleep(job)
                print(f"{job}, {self.index}")
                self.job_queue.task_done()
            except queue.Empty:
                break


def main():
    job_queue = queue.Queue()
    jobs = [random.randint(0,5) for _ in range(20)]
    for job in jobs:
        job_queue.put(job)
    
    workers = [JobWorker(job_queue,i) for i in range(5)]
    for worker in workers:
        worker.start()
    
    for worker in workers:
        worker.join()

if __name__ == "__main__":
    main()