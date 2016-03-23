import time, logging, thread

from pymongo.mongo_client import MongoClient


def stream_logs(name, lt):
    counter = 0
    while True:
        n = lt.get_next_lines()
        for x in n:
            logging.error(x)
        time.sleep(1)
        counter = counter + 1
        logging.error("Counter: "+str(counter))    

class LineTailer:
    
    def __init__(self, admin):
        self.admin = admin
        self.last = {}
        
    def _get_lines(self, log="global"):
        return self.admin.command("getLog" , log)
    
    def get_next_lines(self, log="global"):
        cur = self._get_lines(log)
        lines = cur["log"]
        if log in self.last:
            try:
                idx = lines.index(self.last[log])
                if idx == len(lines) - 1:
                    return []
                lines = lines[idx + 1:]
            except:
                logging.warn("****\nGAP GAP\n****")
        self.last[log] = lines[len(lines) - 1]
        return lines

if __name__ == '__main__':
    client = MongoClient()
    lt = LineTailer(client.admin)
    thread.start_new_thread(stream_logs, ("Thread", lt) )
    time.sleep(60)
