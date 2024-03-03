def read_task(task_name):
    with open(task_name, 'r') as f:
        tasks = f.read().splitlines()
        for task in tasks:
            print(task)