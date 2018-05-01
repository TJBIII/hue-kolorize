# Hue Kolorize

### About
Hue Kolorize allows you to set your Hue lights to a dominate color extracted from several different sources such as a Raspberry Pi camera or what is being displayed on your computer screen. Dominate colors are extracted using KMeans clustering.

### Setup

1. You will need the IP address of your Hue bridge which can be found [here](https://www.meethue.com/api/nupnp).
1. Create your `.env` file using the guide below. It should be placed in the root directory.

Key|Info|Default|Example|Required
---|---|---|---|---
`BRIDGE_IP`|The IP address of your Hue bridge|None|`127.0.0.1`|`True`
`LIGHT_NAMES`| Comma separated string of the lights you'd like to use|All lights connected to the bridge|`TV Lightstrip,Sidetable Bloom`|`False`


### Run
1. Install dependencies: `cd hue-kolorize && pip install -r requirements.txt`
1. Run the script using `python main.py [-h] [--path PATH] {screenshot,image,rpi}`. See below for more info on each source.

##### Source: screenshot
Takes a screenshot of your main monitor in-memory and extracts the dominant color in a loop. Use cases: full immersion by setting the color to the current scene in a PC game or as general bias lighting.

##### Source: rpi
Takes a screenshot in-memory using a Raspberry Pi camera and extracts the dominant color in a loop. Use cases: direct the camera module at the TV for matching the color of the current scene in a movie, TV show, or console game.

Tested with Raspberry Pi v3 Model B+ and Camera Module v2. Angle of view of the v2 camera is approximately 62 x 50 degrees.

##### Source: image
Extracts the dominate color from a JPG image. Use the `--path` argument to specify the image path.


### Tests
Run the tests

```bash
python -m pytest
```
