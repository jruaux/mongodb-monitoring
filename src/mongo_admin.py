#!/usr/bin/env python
import sys, logging

from splunklib.modularinput import Scheme, Argument
from mongo_base import MongoScript

class MongoAdminScript(MongoScript):
        
    COMMANDS = ["top", "ping", "listDatabases", "getCmdLineOpts"]
    
    def create_scheme(self):
        scheme = Scheme("MongoDB Admin")
        scheme.description = "Collect administrative events from MongoDB hosts"
        commands_argument = Argument("commands")
        commands_argument.title = "Admin commands"
        commands_argument.data_type = Argument.data_type_string
        commands_argument.description = "The admin commands to run"
        commands_argument.required_on_create = True
        scheme.add_argument(commands_argument)
        return scheme

    def validate_input(self, validation_definition):
        commands = validation_definition.parameters["commands"].split(" ")
        for command in commands:
            if not command in MongoAdminScript.COMMANDS:
                raise ValueError("'" + command + "' command not supported. Valid commands : " + MongoAdminScript.COMMANDS)
            
    def stream_events_mongo(self, input_name, input_item, client, ew):
            admin = client.admin
            commands = input_item["commands"].split(" ")
            for command in commands:
                sourcetype = 'mongo:admin:' + command.lower()
                try:
                    result = admin.command(command)
                    event = self.create_event(input_name, sourcetype, result)
                    ew.write_event(event)
                except Exception:
                    logging.exception('Could not execute database command %s', command)

if __name__ == "__main__":
    sys.exit(MongoAdminScript().run(sys.argv))
