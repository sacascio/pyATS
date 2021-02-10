#!/usr/bin/env python3

from genie.testbed import load
import json

# Step 0: load the testbed
#testbed = loader.load(f'./tb.yaml')
testbed = load(f'./linux.yaml')

# Step 1: testbed is a dictionary. Extract the device iosxr1
linux = testbed.devices["vader"]

# Step 2: Connect to the device

linux.connect(log_stdout=False)

# Step 3: saving the `show ip interface brief` output in a variable
ps_ef = linux.parse('ps -ef')

# Step 4: print ps -ef
print(json.dumps(ps_ef))

# Step 5: disconnect from the device
linux.disconnect()