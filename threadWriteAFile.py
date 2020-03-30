import threading, time, logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

class WriteFile(threading.Thread):

  def __init__(self, output, name):
    threading.Thread.__init__(self)
    self.output = output
    self.name = name

  def run(self):
    logging.debug("start time" + time.strftime('%H:%M:%S') + "\n")
    for index in range(0, 200000000):
        self.output.write("123456789012345678901234567890")
    logging.debug("end time" + time.strftime('%H:%M:%S') + "\n")

def main():
    f1 = open('output1.txt', 'w+')
    t1 = WriteFile(f1, name="thread1")
    t1.start()
    t1.join()
    f1.close()

main()