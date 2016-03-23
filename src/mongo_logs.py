#!/usr/bin/env python
import sys, time, thread

from splunklib.modularinput import Scheme, Event

from mongo_base import MongoScript
from taillog import LineTailer

def stream_logs(lt, input_name, ew):
    while True:
        n = lt.get_next_lines()
        for x in n:
            event = Event()
            event.stanza = input_name
            event.data = x
            event.sourceType = "mongod"
            ew.write_event(event)
        time.sleep(1)


class MongoLogsScript(MongoScript):
        
    def create_scheme(self):
        scheme = Scheme("MongoDB Logs")
        scheme.description = "Collect logs from MongoDB hosts"
        scheme.use_single_instance = True
        return scheme

    def stream_events_mongo(self, input_name, input_item, client, ew):
        lt = LineTailer(client.admin)
        try:
            thread.start_new_thread( stream_logs, (lt, input_name, ew) )
        except:
            print "Error: unable to start thread"

if __name__ == "__main__":
    sys.exit(MongoLogsScript().run(sys.argv))
