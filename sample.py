#!/usr/bin/env python3

# Feb 10
# V2
#from pyats.topology import loader
from genie.testbed import load

# Step 0: load the testbed
#testbed = loader.load(f'./tb.yaml')
testbed = load(f'./tb.yaml')

# Step 1: testbed is a dictionary. Extract the device iosxr1
nxosdev = testbed.devices["N7k-inner1"]

# Step 2: Connect to the device

#nxosdev.connect(init_exec_commands=[], init_config_commands=[], log_stdout=True)
nxosdev.connect(log_stdout=False)

# Step 2.5 create LO99
nxosdev.configure("interface lo99\r\r\n\rip address 99.99.99.1/30\r\r\n\rdescription done with pyATS\r\r\n\r")

# Step 3: saving the `show ip interface brief` output in a variable
show_interface = nxosdev.parse('show ip interface brief')

# Step 4: pritting the `show interface brief` output
#print(show_interface['interface']['Eth2/3']['ip_address'])
print(show_interface)

raw = nxosdev.execute("show ip int brief")
print(raw)

# Step 4.5 get BGP info
bgpdetails = nxosdev.learn('bgp')

print(bgpdetails)
# Step 5: disconnect from the device
nxosdev.disconnect()