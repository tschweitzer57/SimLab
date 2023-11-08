# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()
client.landAsync().join()

# Reset to pose
client.reset()
client.enableApiControl(True)
client.armDisarm(True)

# take images (register images in responses)
responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis),
    airsim.ImageRequest("1", airsim.ImageType.DepthPlanar, True)])
print('Retrieved images: %d', len(responses))

# mettre la simu en pause
client.simPause(True)
client.simPause(False)

# get geo pose :
client.getHomeGeoPoint('Drone1')

# get cartesian pose : 
client.simGetVehiclePose('Drone1')

# Déplacement du drone :
# Translation
client.moveToPositionAsync(0,0,-1, 5).join()
# Rotation
client.moveByRollPitchYawZAsync(0,0,3.14,-10,5,'Drone1')

#Lister les noms de véhicules :
client.listVehicles()
client.takeoffAsync(vehicle_name="Drone1")

# Faire un scénario de mission

# meme chose avec plusieurs drones
 client.enableApiControl(True, vehicle_name="Drone2")

# obtenir les images : check image apis
client.simGetImage(self, camera_name, image_type, vehicle_name = '', external = False)


# SCENARIO
client.takeoffAsync().join()
client.moveToPositionAsync(0,0,-1.75,1).join()
client.moveToPositionAsync(2.5,0,-1.75,1).join()
client.moveByRollPitchYawZAsync(0,0,3*3.14/2,-1.75,10)
client.moveToPositionAsync(2.5,18,-1.75,2).join()
client.moveByRollPitchYawZAsync(0,0,0,-1.75,10)
client.moveToPositionAsync(50,18,-1.75,5).join()
client.moveToPositionAsync(100,18,-1.75,5).join()
client.moveToPositionAsync(110,18,-1.75,1).join()
client.moveByRollPitchYawZAsync(0,0,3.14/4,-1.75,10)
client.moveToPositionAsync(120,8,-1.75,1).join()


client.moveByRollPitchYawZAsync(0,0,3.14/2,-1.75,10)
client.moveToPositionAsync(120,0,-1.75,1).join()

client.moveByRollPitchYawZAsync(0,0,3.14,-1.75,10)
client.moveToPositionAsync(80,0,-1.75,3).join()
client.moveToPositionAsync(75,0,-1.75,1).join()
client.moveToPositionAsync(75,-1,-14,1).join()
client.moveToPositionAsync(0,-1,-14,5).join()
client.moveToPositionAsync(0,-1,-1,5).join()
client.landAsync().join()
