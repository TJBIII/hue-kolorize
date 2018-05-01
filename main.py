import io
import time
import argparse

from hkolorize.hue import Hue
from hkolorize import settings
from hkolorize import process_img
from PIL import Image, ImageGrab

def main(source, path=None):
    light_names = settings.LIGHT_NAMES
    bridge_ip = settings.BRIDGE_IP

    hue = Hue(bridge_ip, light_names)

    if source == 'screenshot':
        while(True):
            # ImageGrab returns RGBA image on Windows so we will convert to RGB
            img =  ImageGrab.grab().convert('RGB')

            _, dominant_color = process_img.get_colors(img, 3)
            hue.set_lights_rgb(dominant_color)
            time.sleep(1)
    elif source == 'image':
        img = Image.open(path)
        _, dominant_color = process_img.get_colors(img, 3)
        hue.set_lights_rgb(dominant_color)
    elif source == 'rpi':
        # only available on rpi
        import picamera

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

                time.sleep(3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Set Hue lights with dominate color from an image source.')
    parser.add_argument('source', choices=['screenshot', 'image', 'rpi'], help='the source to extract from')
    parser.add_argument('--path', type=str, help='the image file path')

    args = parser.parse_args()

    if args.source == 'image' and args.path is None:
        parser.error("image source requires --path")

    main(args.source, args.path)
