from concurrent.futures import ThreadPoolExecutor
import time


def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page

with ThreadPoolExecutor(max_workers=5) as t: 
    task1 = t.submit(spider, 1)
    task2 = t.submit(spider, 2) 
    task3 = t.submit(spider, 3)

    print(f"task1: {task1.done()}") 
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")

    time.sleep(4)
    print(f"task1: {task1.done()}")
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")
    print(task1.result())  # get result