# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# Enable api control and arm Drones 1,2,3 and 4
client.enableApiControl(True, 'Drone1')
client.enableApiControl(True, 'Drone2')
client.enableApiControl(True, 'Drone3')
client.enableApiControl(True, 'Drone4')
client.armDisarm(True, 'Drone1')
client.armDisarm(True, 'Drone2')
client.armDisarm(True, 'Drone3')
client.armDisarm(True, 'Drone4')

# Drone1 takeoff
client.takeoffAsync(vehicle_name='Drone1').join()
time.sleep(3)

# Drone2 takeoff
client.takeoffAsync(vehicle_name='Drone2').join()
time.sleep(3)

# Drone3 takeoff
client.takeoffAsync(vehicle_name='Drone3').join()
time.sleep(3)

# Drone4 takeoff
client.takeoffAsync(vehicle_name='Drone4').join()
time.sleep(3)

time.sleep(10)

# Drone4 landing
client.landAsync(vehicle_name='Drone4').join()
time.sleep(3)

# Drone3 landing
client.landAsync(vehicle_name='Drone3').join()
time.sleep(3)

# Drone2 landing
client.landAsync(vehicle_name='Drone2').join()
time.sleep(3)

# Drone1 landing
client.landAsync(vehicle_name='Drone1').join()
time.sleep(3)


