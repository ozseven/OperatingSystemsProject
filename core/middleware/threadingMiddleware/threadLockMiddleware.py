import threading
import time


class LocksManager:
    locks = set()
    lock = threading.Lock()

def threadLockMiddleware(func):
    def wrapper(*args):
        while True:
            if args in LocksManager.locks:
                print('Dosya Kilitli')
                time.sleep(0.1)
                continue
            else:
                print("Dosya kilit listesine ekelendi")
                LocksManager.locks.add(args)
                with LocksManager.lock:
                    func(*args)
                print('Lock silindi')
                LocksManager.locks.remove(args)
            return func(*args)
    return wrapper


