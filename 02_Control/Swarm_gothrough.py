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

# Drones takeoff
client.takeoffAsync(vehicle_name='Drone1')
client.takeoffAsync(vehicle_name='Drone2')
client.takeoffAsync(vehicle_name='Drone3')
client.takeoffAsync(vehicle_name='Drone4').join()

client.moveToPositionAsync(0,0,-2,1,vehicle_name='Drone1')
client.moveToPositionAsync(0,0,-2,1,vehicle_name='Drone2')
client.moveToPositionAsync(0,0,-2,1,vehicle_name='Drone3')
client.moveToPositionAsync(0,0,-2,1,vehicle_name='Drone4').join()

client.moveToPositionAsync(0,-20,-2,1,vehicle_name='Drone1')
client.moveToPositionAsync(0,-20,-2,1,vehicle_name='Drone2')
client.moveToPositionAsync(0,-20,-2,1,vehicle_name='Drone3')
client.moveToPositionAsync(0,-20,-2,1,vehicle_name='Drone4').join()

client.moveToPositionAsync(2,-28,-2,1,vehicle_name='Drone3')
client.moveToPositionAsync(6,-26,-2,1,vehicle_name='Drone4')
client.moveToPositionAsync(2,-28,-2,1,vehicle_name='Drone1').join()
client.moveToPositionAsync(-2,-26,-2,1,vehicle_name='Drone2').join()

client.moveToPositionAsync(2,-30,-6,1,vehicle_name='Drone1')
client.moveToPositionAsync(-2,-26,-6,1,vehicle_name='Drone2')
client.moveToPositionAsync(2,-30,-6,1,vehicle_name='Drone3')
client.moveToPositionAsync(6,-26,-6,1,vehicle_name='Drone4').join()

time.sleep(1)

client.moveToPositionAsync(2,-160,-6,5,vehicle_name='Drone1')
client.moveToPositionAsync(-2,-155,-6,5,vehicle_name='Drone2')
client.moveToPositionAsync(2,-160,-6,5,vehicle_name='Drone3')
client.moveToPositionAsync(6,-155,-6,5,vehicle_name='Drone4').join()

time.sleep(5)

# Drones landing
client.landAsync(vehicle_name='Drone1')
client.landAsync(vehicle_name='Drone2')
client.landAsync(vehicle_name='Drone3')
client.landAsync(vehicle_name='Drone4').join()
