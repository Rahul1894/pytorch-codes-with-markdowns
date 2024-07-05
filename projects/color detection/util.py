# %%
import cv2
import numpy as np 

# %%
def get_limits(color):
    c=np.uint8([[color]]) # Convert color to a 1x1 pixel NumPy array of type uint8
    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lower_limit=hsvc[0][0][0]-10,100,100
    upper_limit=hsvc[0][0][0]+10,255,255

    lower_limit=np.array(lower_limit,dtype=np.uint8)
    upper_limit=np.array(upper_limit,dtype=np.uint8)
    return lower_limit,upper_limit

# %% [markdown]
# c = np.uint8([[color]]):
# 
# Converts the input color tuple to a NumPy array of shape (1,1,3) with data type uint8. This array format is required for certain operations in OpenCV.

# %% [markdown]
# HSV color space is often used in computer vision for easier color detection and segmentation.

# %% [markdown]
# lower_limit = hsvc[0][0][0] - 10, 100, 100:
# 
# Defines the lower limit of the HSV color range. HSV color space consists of:
# 
# Hue: Represents the color itself.
# 
# Saturation: Represents the purity of the color (depth of the color).
# 
# Value: Represents the brightness of the color.
# 
# The lower limit for Hue (H) is set to hsvc[0][0][0] - 10 (Hue value of the converted color minus 10).
# 
# Saturation (S) and Value (V) are set to 100 and 100, respectively. These values are typical starting points for saturation and value.
# 
# upper_limit = hsvc[0][0][0] + 10, 255, 255:
# 
# Defines the upper limit of the HSV color range:
# 
# Hue (H) is set to hsvc[0][0][0] + 10 (Hue value of the converted color plus 10).
# 
# Saturation (S) and Value (V) are set to 255 (maximum values for saturation and value).
# 


