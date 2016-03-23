#!/usr/bin/env python
import sys, logging

from splunklib.modularinput import Scheme, Argument

from mongo_base import MongoScript


class MongoDBScript(MongoScript):
        
    COMMANDS = ["serverStatus", "connPoolStats", "shardConnPoolStats", "dbHash", "dbStats", "hostInfo", "buildInfo", "features"]
    
    def create_scheme(self):
        scheme = Scheme("MongoDB Database Stats")
        scheme.description = "Collect database statistics from MongoDB hosts"
        database_argument = Argument("database")
        database_argument.title = "Database"
        database_argument.data_type = Argument.data_type_string
        database_argument.description = "name of the MongoDB database to run commands against"
        database_argument.required_on_create = True
        scheme.add_argument(database_argument)
        commands_argument = Argument("commands")
        commands_argument.title = "Database commands"
        commands_argument.data_type = Argument.data_type_string
        commands_argument.description = "Space-separated names of the database commands to run"
        commands_argument.required_on_create = True
        scheme.add_argument(commands_argument)
        return scheme

    def validate_input(self, validation_definition):
        commands = validation_definition.parameters["commands"].split(" ")
        for command in commands:
            if not command in MongoDBScript.COMMANDS:
                raise ValueError("'" + command + "' command not supported. Valid commands : " + MongoDBScript.COMMANDS)
            
    def stream_events_mongo(self, input_name, input_item, client, ew):
        db = client[input_item["database"]]
        commands = input_item["commands"].split(" ")
        for command in commands:
            sourcetype = 'mongo:db:' + command.lower()
            try:
                result = db.command(command)
                event = self.create_event(input_name, sourcetype, result)
                ew.write_event(event)
            except Exception:
                logging.exception('Could not execute database command %s', command)

if __name__ == "__main__":
    sys.exit(MongoDBScript().run(sys.argv))
