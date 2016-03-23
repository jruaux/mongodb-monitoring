#!/usr/bin/env python

from abc import abstractmethod
import pymongo, json

from bson import json_util
from splunklib.modularinput import Script, Argument
from splunklib.modularinput.event import Event


class MongoScript(Script):
        
    def to_json(self, obj):
        return json.dumps(obj, default=json_util.default)
    
    def create_event(self, input_name, sourcetype, obj):
        event = Event()
        event.stanza = input_name
        event.sourceType = sourcetype
        event.data = self.to_json(obj)
        return event
    
    def get_scheme(self):
        scheme = self.create_scheme()
        scheme.use_external_validation = True
        host_argument = Argument("server")
        host_argument.title = "Host"
        host_argument.data_type = Argument.data_type_string
        host_argument.description = "hostname or IP address of the instance to connect to, or a mongodb URI, or a list of hostnames/mongodb URIs"
        host_argument.required_on_create = True
        scheme.add_argument(host_argument)
        port_argument = Argument("port")
        port_argument.title = "Port"
        port_argument.data_type = Argument.data_type_string
        port_argument.description = "port number on which to connect"
        port_argument.required_on_create = True
        scheme.add_argument(port_argument)
        return scheme
    
    def validate_input(self, definition):
        try:
            int(definition.parameters["port"])
        except:
            raise ValueError("MongoDB port should be an integer")

    
    @abstractmethod
    def create_scheme(self):
        """ initialize the ```Scheme```
        :return:
        """
    
    @abstractmethod
    def stream_events_mongo(self, input_name, input_item, client, ew):
        """The method called to stream events into Splunk. It should do all of its output via
        EventWriter rather than assuming that there is a console attached.

        :param input_name: name of the data input stanza
        :param input_item: input configuration element
        :param ew: An object with methods to write events and log messages to Splunk.
        """
    
    def stream_events(self, inputs, ew):
        for input_name, input_item in inputs.inputs.iteritems():
            host = input_item["server"]
            port = input_item["port"]
            if not port is None:
                port = int(port)
            client = pymongo.MongoClient(host, port)
            self.stream_events_mongo(input_name, input_item, client, ew)