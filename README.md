# hue-kolorize

### Setup
You will need a Raspberry Pi and a Raspberry Pi Camera Module v2.

1. Clone this repo onto your Raspberry Pi.
1. Run `cd hue-kolorize && pip install -r requirements.txt`
1. You will need the IP address of your Hue bridge which can be found [here](https://www.meethue.com/api/nupnp).
1. Create your .env file using the guide below:

Key|Info|Default|Required
---|---|---|---
`BRIDGE_IP`|The IP address of your Hue bridge|None|`True`
`LIGHT_NAMES`| Comma separated string of the lights you'd like to use|All lights|`False`
