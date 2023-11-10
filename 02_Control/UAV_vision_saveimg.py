# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os
import time
import numpy as np

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Drone takeoff
client.takeoffAsync().join()

responses = client.simGetImages([
    # png format
    airsim.ImageRequest(0, airsim.ImageType.Scene), 
    # uncompressed RGB array bytes
    airsim.ImageRequest(1, airsim.ImageType.Scene, False, False),
    # floating point uncompressed image
    airsim.ImageRequest(1, airsim.ImageType.DepthPlanar, True)])

responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])
response = responses[0]


# get numpy array
img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) 

# reshape array to 4 channel image array H X W X 4
img_rgb = img1d.reshape(response.height, response.width, 3)

# original image is fliped vertically
img_rgb = np.flipud(img_rgb)

# write to png 
airsim.write_png(os.path.normpath('testimg' + '.png'), img_rgb)

# Drone landing
client.landAsync().join()
