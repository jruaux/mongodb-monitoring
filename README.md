# Installation

Install this add-on the same way you would install any Splunk app:
- automatically from [SplunkBase](https://splunkbase.splunk.com/app/2957) through *Browse more apps*
- manually: download the *mongodb.spl* file and install it in your instance

# Configuration

## MongoDB Admin

To receive administrative events from MongoDB hosts, enable a *mongo_admin* data input under *Settings > Data Inputs > MongoDB Admin*

## MongoDB Collection Stats

To fetch collection statistics from MongoDB hosts, enable a *mongo_collstats* data input under *Settings > Data Inputs > MongoDB Collection Stats*

## MongoDB Database Stats

To fetch database statistics from MongoDB hosts, enable a *mongo_db* data input under *Settings > Data Inputs > MongoDB Database Stats*

## MongoDB Logs

There are 3 ways to get MongoDB logs into Splunk:
- set up a file monitor on the Splunk Universal Forwarder to tail *mongod.log* on all MongoDB hosts
- configure *mongod* to send logs to Splunk via *syslog*
- configure the MongoDB Monitoring app to collect logs via the MongoDB Client API by adding a data input under *Settings > Data Inputs > MongoDB Logs*

The MongoDB Monitoring app applies field extractions to the *mongod* sourcetype. By default the dashboards expect MongoDB logs to reside in the *mongodb* index with sourcetype *mongod*. You can change this by modifying the *mongo_index* and *mongo_sourcetype* macros under *Settings > Advanced search > Search macros*.

# Questions
View and submit questions on [SplunkAnswers](http://answers.splunk.com/answers/app/2957)

# Developers

To build the MongoDB Monitoring app from source, clone the [git repository](https://jruaux@git.splunk.com/scm/\~jruaux/mongodb-monitoring.git) and run this command from the top-level folder:
```python setup.py dist```