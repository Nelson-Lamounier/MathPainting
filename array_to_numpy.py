import numpy as np
from PIL import Image

# Create 3D numpy array of zeros, then replace zeros (black pixels) with yellow pxls

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Make a vertical red patch
data[:, 1:3] = [255, 0, 0]

# Make a horizontal dark red patch
data[1:3] = [100, 0, 0]

# Make a black square on the middle
data[1:4, 1:3] = [20, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

