import colorsys
import random 

from .color_converter import xy_from_rgb
from phue import Bridge, PhueRegistrationException

class Hue:
    def __init__(self, bridge_ip, light_names=None):
        self.bridge_ip = bridge_ip
        self.bridge = self.setup()
        self.lights = self.get_lights(light_names)

    def setup(self):
        """ Setup the Hue bridge
        """
        try:
            return Bridge(self.bridge_ip)
        except PhueRegistrationException:
            raise Exception('Press the link button on your Hue bridge and then try again within 30 seconds.')
        except:
            raise Exception('Could not connect to the Hue bridge. Are you sure you have the correct IP address?')

    def get_lights(self, light_names):
        """ Get list of Hue light objects
            
        Parameters:
            light_names (str): Comma separated list of light names to use

        Returns:
            list: Hue light objects
        """
        name_light_dict = self.bridge.get_light_objects('name')

        if not light_names:
            color_types = ['Color light', 'Extended color light']
            return [light for light in name_light_dict.values() if light.type in color_types]
        else:
            names = light_names.split(',')
            return [light for name, light in name_light_dict.items() if name in names]

    def set_lights_xy(self, xy, brightness=254, transitiontime=10):
        """ Set all lights
    
        Parameters:
            xy (tuple): xy color to set all lights to
            brightness (int): brightness to set all lights to
            transitiontime (int): time for color transition in deci-seconds
        """
        for light in self.lights:
            # handle black
            if brightness == 0 and xy == (0,0):
                light.brightness = 0
                light.on = False
                continue

            if not light.on:
                light.on = True

            light.transitiontime = transitiontime
            light.xy = xy
            light.brightness = int(brightness)

    def set_lights_rgb(self, rgb_tuple):
        """ Set all lights to the rgb color provided.

        Parameters:
            rgb_tuple (tuple): Tuple of ints between [0-255] representing RGB values
        """
        r, g, b = rgb_tuple
        h, l, s = colorsys.rgb_to_hls(r, g, b)

        xy = xy_from_rgb(r, g, b)
        self.set_lights_xy(xy, int(l), 10)

    def set_lights_random(self):
        """ Set all lights to a random color.
        """
        xy = (random.random(), random.random())
        self.set_lights_xy(xy)
