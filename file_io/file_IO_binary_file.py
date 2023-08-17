# HardvardX Cs50P Introduction to Programming with Python
# Lecture 6: FileI/O: Binary Files and PIL

"""
    1. A binary file is simply a collection of ones and zeros. This type of file can store anything including, music and image data.
    2. There is a popular Python library called PIL that works well with image files.

Note to self: Error while trying to install pip pip3 install PIL
"""

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(f"gif/{arg}")
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)