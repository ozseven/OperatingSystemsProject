import threading
import time


class LocksManager:
    locks = set()
    lock = threading.Lock()

def threadLockMiddleware(func):
    def wrapper(*args):
        while True:
            if args in LocksManager.locks:
                print(f'Dosya Kilitli:{args}')
                time.sleep(0.1)
                continue
            else:
                print(f"Dosya kilit listesine ekelendi:{args}")
                LocksManager.locks.add(args)
                with LocksManager.lock:
                    try:
                        func(*args)
                    finally:
                        print(f'Lock silindi:{args}')
                        LocksManager.locks.remove(args)
            return func(*args)
    return wrapper


