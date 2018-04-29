from hue import Hue
from PIL import Image

import settings
import process_img

def main():
    light_names = settings.LIGHT_NAMES
    bridge_ip = settings.BRIDGE_IP

    # img = Image.open('/Users/gamewisp/Desktop/hue_test_images/trees.jpg')
    img = Image.open('/Users/gamewisp/Desktop/hue_test_images/beach.jpg')
    cluster_centers, dominant_color = process_img.get_colors(img, 3)
    print(cluster_centers)
    print(dominant_color)


    hue = Hue(bridge_ip, light_names)
    # hue.set_lights_random()
    hue.set_lights_rgb(dominant_color)

if __name__ == '__main__':
    main()
