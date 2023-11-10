# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Drone takeoff
client.takeoffAsync().join()

# Scenario
client.takeoffAsync().join()
client.moveToPositionAsync(0,0,-1.25,1).join()
print('step 1')
time.sleep(5)

client.moveToPositionAsync(2.5,0,-1.25,1).join()
print('step 2')
time.sleep(5)

client.moveByRollPitchYawZAsync(0,0,3*3.14/2,-1.25,10).join()
print('step 3')
time.sleep(5)

client.moveToPositionAsync(2.5,18,-1.25,2).join()
print('step 4')
time.sleep(5)

client.moveByRollPitchYawZAsync(0,0,0,-1.25,10).join()
print('step 5')
time.sleep(5)

client.moveToPositionAsync(5,18,-1.25,1).join()
print('step 6')
time.sleep(5)

client.moveToPositionAsync(50,18,-1.25,5).join()
print('step 6')
time.sleep(5)

client.moveToPositionAsync(100,18,-1.25,5).join()
print('step 7')
time.sleep(5)

client.moveToPositionAsync(110,18,-1.25,1).join()
print('step 8')
time.sleep(5)

client.moveByRollPitchYawZAsync(0,0,3.14/4,-1.25,10).join()
print('step 9')
time.sleep(5)

client.moveToPositionAsync(120,8,-1.25,1).join()
print('step 10')
time.sleep(5)

client.moveByRollPitchYawZAsync(0,0,3.14/2,-1.25,10).join()
print('step 11')
time.sleep(5)

client.moveToPositionAsync(120,0,-1.25,1).join()
print('step 12')
time.sleep(5)

client.moveByRollPitchYawZAsync(0,0,3.14,-1.25,10).join()
print('step 13')
time.sleep(5)

client.moveToPositionAsync(80,0,-1.25,3).join()
print('step 14')
time.sleep(5)

client.moveToPositionAsync(75,0,-1.25,1).join()
print('step 15')
time.sleep(5)

client.moveToPositionAsync(75,-1,-14,1).join()
print('step 16')
time.sleep(5)

client.moveToPositionAsync(0,-1,-14,5).join()
print('step 17')
time.sleep(5)

client.moveToPositionAsync(0,-1,-1,5).join()
print('step 18')
time.sleep(5)

# Drone landing
client.landAsync().join()
