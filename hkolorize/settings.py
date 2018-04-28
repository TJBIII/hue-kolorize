import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

BRIDGE_IP = os.getenv('BRIDGE_IP')
LIGHT_NAMES = os.getenv('LIGHT_NAMES', None)
