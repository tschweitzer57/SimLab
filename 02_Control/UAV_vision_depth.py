import airsim
import numpy as np
import cv2

# Constants for visualization
MIN_DEPTH_METERS = 0
MAX_DEPTH_METERS = 100

# Connect to running UE4 instance
client = airsim.VehicleClient(timeout_value = 7200)
client.confirmConnection()

# Request DepthPerspective image as uncompressed float
response = client.simGetImages(
    [
        airsim.ImageRequest("0", airsim.ImageType.DepthPerspective, True, False),
    ]
)

response = response[0]

# Reshape to a 2d array with correct width and height
depth_img_in_meters = airsim.list_to_2d_float_array(response.image_data_float, response.width, response.height)
depth_img_in_meters = depth_img_in_meters.reshape(response.height, response.width, 1)

# Lerp 0..100m to 0..255 gray values
depth_8bit_lerped = np.interp(depth_img_in_meters, (MIN_DEPTH_METERS, MAX_DEPTH_METERS), (0, 255))
cv2.imwrite("depth_visualization.png", depth_8bit_lerped.astype('uint8'))

# Convert depth_img to millimeters to fill out 16bit unsigned int space (0..65535). Also clamp large values (e.g. SkyDome) to 65535
depth_img_in_millimeters = depth_img_in_meters * 1000
depth_16bit = np.clip(depth_img_in_millimeters, 0, 65535)
cv2.imwrite("depth_16bit.png", depth_16bit.astype('uint16'))