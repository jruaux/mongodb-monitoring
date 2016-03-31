# MongoDB Monitoring App

## Installation

Install this app the same way you would install any Splunk app:
- automatically from [SplunkBase](https://splunkbase.splunk.com/app/2957) through *Browse more apps*
- manually: download the *mongodb-monitoring.spl* file and install it in your instance

## Configuration

### MongoDB Admin

To receive administrative events from MongoDB hosts, enable a *mongo_admin* data input under *Settings > Data Inputs > MongoDB Admin*

### MongoDB Collection Stats

To fetch collection statistics from MongoDB hosts, enable a *mongo_collstats* data input under *Settings > Data Inputs > MongoDB Collection Stats*

### MongoDB Database Stats

To fetch database statistics from MongoDB hosts, enable a *mongo_db* data input under *Settings > Data Inputs > MongoDB Database Stats*

### MongoDB Logs

There are 3 ways to get MongoDB logs into Splunk:
- set up a file monitor on the Splunk Universal Forwarder to tail *mongod.log* on all MongoDB hosts
- configure *mongod* to send logs to Splunk via *syslog*
- configure the MongoDB Monitoring app to collect logs via the MongoDB Client API by adding a data input under *Settings > Data Inputs > MongoDB Logs*

The MongoDB Monitoring app applies field extractions to the *mongod* sourcetype. By default the dashboards expect MongoDB logs to reside in the *mongodb* index with sourcetype *mongod*. You can change this by modifying the *mongo_index* and *mongo_sourcetype* macros under *Settings > Advanced search > Search macros*.

## Alerts

The MongoDB Monitoring app includes a sample alert that triggers when the number of connections to a MongoDB cluster reaches 10,000. You can modify this alert by editing the `# Connections > 10,000` stanza in [savedsearches.conf](https://raw.githubusercontent.com/jruaux/mongodb-monitoring/master/default/savedsearches.conf).

## Questions
View and submit questions on [SplunkAnswers](http://answers.splunk.com/answers/app/2957)

## Developers

To build the MongoDB Monitoring app from source, clone the Github repository:
```git clone https://github.com/jruaux/mongodb-monitoring.git```
 and run this command from the top-level folder:
```python setup.py dist```

## License

The MongoDB Monitoring app is licensed under the Apache License 2.0. Details can be found in the file LICENSE.

For compatibility with Python 2.6, The Splunk Software Development Kit
for Python ships with ordereddict.py from the ordereddict package on
[PyPI](http://pypi.python.org/pypi/ordereddict/1.1), which is licensed
under the MIT license (see the top of splunklib/ordereddict.py).

## Third-Party Software

The MongoDB Monitoring app uses the following open-source components:

### BSON

BSON (Binary JSON) encoding and decoding

```
# Copyright 2009-2015 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

### PyMongo

Python driver for MongoDB

```
# Copyright 2009-2015 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

*Disclaimer*: PyMongo uses cryptographic algorithms no longer considered sufficiently secure, even for general use. The vulnerability is described [here](https://bugzilla.redhat.com/show_bug.cgi?id=1064849) 

### Python library for Splunk

```
# Copyright 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
```