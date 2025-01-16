import time
import threading


def process_work(work):
    print(f"Work processing: {work}")
    time.sleep(30)
    print(f"Work performed: {work}")


def update_work_status(work, new_status):
    with open('work.txt', 'r+') as work_file:
        lines = work_file.readlines()
        work_file.seek(0)
        for line in lines:
            if ',' in line:
                current_work, status = line.strip().split(',')
                if current_work == work:
                    line = line.replace(status, new_status)
            work_file.write(line)
        work_file.truncate()


def consume_work():
    while True:
        with open('work.txt', 'r+') as work_file:
            for line in work_file:
                if ',' in line:
                    work, status = line.strip().split(',')
                    if status == 'pending':
                        update_work_status(work, 'in_progress')
                        process_work(work)
                        update_work_status(work, 'done')
            time.sleep(5)


if __name__ == "__main__":
    consumer_thread = threading.Thread(target=consume_work)
    consumer_thread.start()
