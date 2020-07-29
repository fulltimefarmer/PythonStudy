from concurrent.futures import ThreadPoolExecutor
import time

tasks=[]

def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page

with ThreadPoolExecutor(max_workers=5) as executor:
    tasks=[]
    for i in range(6,9):
        future = executor.submit(spider, i)
        tasks.append(future)

    while len(tasks) > 0:
        for task in tasks:
            #print(f"task: {task.done()}")
            if task.done():
                print(task.result())
                tasks.remove(task)
