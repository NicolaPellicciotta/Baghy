import tinytuya

DEVICE_ID_HERE = "bfc42a284525d9d92d6tx0"
#DEVICE_ID_HERE = "bfc42a284525d9d92d6rx5"
IP_ADDRESS = "192.168.0.144"
LOCAL_KEY = "8d3d84ef517b3338"
#LOCAL_KEY = "48893b254112483b"


d = tinytuya.OutletDevice(DEVICE_ID_HERE, IP_ADDRESS, LOCAL_KEY, 'device22')
d.set_version(3.3)
d.set_dpsUsed({"1": None})
data = d.status()  # NOTE this does NOT require a valid key vor version 3.1

# Show status of first controlled switch on device
print('Dictionary %r' % data)
print('State (bool, true is ON) %r' % data['dps']['1'])

# Toggle switch state
switch_state = data['dps']['1']
data = d.set_status(not switch_state)

data = d.status()
print('State (bool, true is ON) %r' % data['dps']['1'])
