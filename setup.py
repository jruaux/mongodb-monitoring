#!/usr/bin/env python

from setuptools import setup, Command
from contextlib import closing
from subprocess import check_call, STDOUT

import os
import sys
import shutil
import tarfile

import splunklib


class DistCommand(Command):
    """setup.py command to create .spl file for modular input"""
    description = "Build MongoDB Monitoring app tarball."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def get_python_files(files):
        """Utility function to get .py files from a list"""
        python_files = []
        for file_name in files:
            if file_name.endswith(".py"):
                python_files.append(file_name)
        return python_files

    def run(self):
        app = 'mongodb'
        splunklib_arcname = "splunklib"
        modinput_dir = os.path.join(splunklib_arcname, "modularinput")

        if not os.path.exists("build"):
            os.makedirs("build")

        with closing(tarfile.open(os.path.join("build", app + ".spl"), "w:gz")) as spl:
            spl.add(
                "src",
                arcname=os.path.join(app, "bin")
            )
            spl.add(
                "default",
                arcname=os.path.join(app, "default")
            )
            spl.add(
                "lookups",
                arcname=os.path.join(app, "lookups")
            )
            spl.add(
                "static",
                arcname=os.path.join(app, "static")
            )            
            spl.add(
                "README",
                arcname=os.path.join(app, "README")
            )
            spl.add(
                "README.MD",
                arcname=os.path.join(app, "README.MD"))
            spl.close()
        return

setup(
    author="Julien Ruaux",
    author_email="jruauxNOSPAM@splunk.com",
    cmdclass={ 'dist': DistCommand},
    description="Splunk App for MongoDB Monitoring",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    name="mongodb",
    url="https://github.com/jruaux/mongodb-monitoring",
    version=1.0,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Splunk Users",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
)
