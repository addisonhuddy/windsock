"""Windsock."""
import random
import time
import threading
import json
import requests
import sys


def main():
    """Main Function."""
    if sys.argv[1] == 'help':
        print "python main.py threads host port"
        print "example: python main.py 2 http://localhost 8080"
        return

    thread_count = sys.argv[1]
    threads = []
    for i in range(int(thread_count)):
        t = threading.Thread(target=device)
        threads.append(t)
        t.start()


def device():
    """Creates a new windsock devices and sends output to url."""
    url = ("%s:%s" % (sys.argv[2], sys.argv[3]))
    data = {}
    print("Device started\n")

    device_id = str(random.randint(0, 1000)) + \
        (random.sample(['A', 'B', 'C', 'D', 'E'], 1))[0]

    # Device ID
    data['device id'] = device_id

    # Wind speed
    time.sleep(random.randint(0, 10))
    double_random = random.uniform(0.0, 50.0)
    start_ws = random.uniform(0.0, double_random)
    old_ws = start_ws

    # Wind direction
    time.sleep(random.randint(0, 10))
    start_wd = random.randint(0, 360)
    old_wd = start_wd

    while device_running():
        new_ws = random.uniform(old_ws - 5.0, old_ws + 5.0)
        if new_ws < 0:
            old_ws = 0
            continue
        data['wind speed'] = new_ws
        old_ws = new_ws

        new_wd = random.randint(old_wd - 2, old_wd + 2)
        if new_ws < 0:
            old_ws = 0
            continue
        data['wind direction'] = new_wd
        old_wd = new_wd

        json_msg = json.dumps(data)
        r = requests.post(url, data=json_msg)
        print(r.status_code, r.reason)
        time.sleep(random.randint(0, 1))


def device_running():
    """Device has a 1 in 1000 chance of failing on each run"""
    if random.randint(0, 10000) == 23:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
