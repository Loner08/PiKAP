import contextlib
import time
import sys
class cm_timer_1(object):
 def __enter__(self):
    self.t = time.perf_counter()
    return self
 def __exit__(self, type, value, traceback):
    self.e = time.perf_counter()
 def __float__(self):
    return float(self.e - self.t)
 def __str__(self):
    return f"{self.e - self.t:.4f}"
@contextlib.contextmanager
def cm_timer_2():
 start_time = time.perf_counter()
 yield
 end_time = time.perf_counter()
 print(f"{end_time - start_time:.4f}")

def main():
 with cm_timer_1() as t1:
    time.sleep(5.5)
 print(t1)

 with cm_timer_2() as t2:
    time.sleep(5.5)
 print(t2)
if __name__ == "__main__":
 main()
