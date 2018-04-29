import io
import time
import picamera

from hue import Hue
from PIL import Image

import settings
import process_img

def main():
    light_names = settings.LIGHT_NAMES
    bridge_ip = settings.BRIDGE_IP

    hue = Hue(bridge_ip, light_names)

    with picamera.PiCamera() as camera:
        while True:
            # create in-memory stream
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg')

            # "rewind" the stream to the beginning to read its content
            stream.seek(0)
            img = Image.open(stream)

            _, dominant_color = process_img.get_colors(img, 3)
            hue.set_lights_rgb(dominant_color)

            time.sleep(2)

if __name__ == '__main__':
    main()
