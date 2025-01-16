import time


def add_work_to_queue(work):
    with open('work.txt', 'a') as work_file:
        work_file.write(f"{work}, pending\n")
    work_file.close()


if __name__ == "__main__":
    while True:
        new_work = input("Specify the work to be done: ")
        add_work_to_queue(new_work)
        print("Work added to the queue.")
        time.sleep(2)
