import itertools
import threading
import time
import sys

elapsedtime = 0
startTime = 0
done = False
mockData = []
thread = None


def start():
    global startTime
    print('Great! Lets start mocking!')
    thread = threading.Thread(target=__animate)
    startTime = time.time()
    thread.start()

def stop():
    global done
    global elapsedtime
    global startTime
    elapsedtime = time.time() - startTime
    elapsedtime = str(round(elapsedtime, 2))
    done = True

def __animate():
    global elapsedtime
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rGenerating mock data! ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rgenerating done! Total of {o} objects created in {t} seconds   '.format(
        o=len(mockData), t=elapsedtime))