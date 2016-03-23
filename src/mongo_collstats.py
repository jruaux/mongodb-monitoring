#!/usr/bin/env python
import sys, logging

from splunklib.modularinput import Scheme, Argument

from mongo_base import MongoScript


class MongoCollStatsScript(MongoScript):
        
    SOURCETYPE = "mongo:collstats"
    
    def create_scheme(self):
        scheme = Scheme("MongoDB Collection Stats")
        scheme.description = "Fetch collection statistics from MongoDB hosts"
        database_argument = Argument("database")
        database_argument.title = "Database"
        database_argument.data_type = Argument.data_type_string
        database_argument.description = "name of the MongoDB database to run commands against"
        database_argument.required_on_create = True
        scheme.add_argument(database_argument)
        collections_argument = Argument("collections")
        collections_argument.title = "Database collections"
        collections_argument.data_type = Argument.data_type_string
        collections_argument.description = "Space-separated names of the collections to fetch stats for"
        collections_argument.required_on_create = True
        scheme.add_argument(collections_argument)
        return scheme

    def validate_input(self, validation_definition):
        collections = validation_definition.parameters["collections"].split(" ")
        if not collections:
            raise ValueError("No collection name specified")
            
    def stream_events_mongo(self, input_name, input_item, client, ew):
        db = client[input_item["database"]]
        collections = input_item["collections"].split(" ")
        for collection in collections:
            try:
                result = db.command({"collStats": collection})
                event = self.create_event(input_name, MongoCollStatsScript.SOURCETYPE, result)
                ew.write_event(event)
            except Exception:
                logging.exception('Could not get stats for collection %s', collection)

if __name__ == "__main__":
    sys.exit(MongoCollStatsScript().run(sys.argv))
