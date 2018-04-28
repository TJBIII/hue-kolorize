from hue import Hue
import settings

def main():
    light_names = settings.LIGHT_NAMES
    bridge_ip = settings.BRIDGE_IP

    hue = Hue(bridge_ip, light_names)
    hue.set_lights_random()

if __name__ == '__main__':
    main()
