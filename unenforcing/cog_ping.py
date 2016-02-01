#!/usr/bin/python

import os
import subprocess

argv = os.getenv("COG_ARGV_0")

#Currently, Slack formats urls into links. We need to remove this formatting
slack_translated = argv.split("|")
host = slack_translated[1].strip(">")

print subprocess.check_output(["/sbin/ping", "-c", "3", host])
