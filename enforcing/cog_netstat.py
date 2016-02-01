#!/usr/bin/python

import os
import subprocess

search_str = os.getenv("COG_ARGV_0")
opt_all = os.getenv("COG_OPT_ALL")
opt_stats = os.getenv("COG_OPT_STATS")
opt_numbers = os.getenv("COG_OPT_NUMBERS")

# Add options if they are set
netstat_cmd = ["/usr/sbin/netstat"]
if opt_all == "true":
    netstat_cmd.append("-a")
if opt_stats == "true":
    netstat_cmd.append("-m")
if opt_numbers == "true":
    netstat_cmd.append("-n")

# Search for the search string if it is set
if search_str:
    grep_cmd = ["/usr/bin/grep", search_str]
    cmd = netstat_cmd + ["|"] + grep_cmd
else:
    cmd = netstat_cmd

result = subprocess.check_output(cmd)
# Limit how many characters can be displayed in Cog
if len(result) > 16130:
    print result[:16130] + " ...truncated"
else:
    print result
