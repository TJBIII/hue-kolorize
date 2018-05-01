from hkolorize.hue import Hue

import pytest

def test_hue_constructor(mocker):
    lights = [mocker.MagicMock() for _ in range(3)]
    mocker.patch('hkolorize.hue.Hue.get_lights', return_value=lights)
    mocker.patch('hkolorize.hue.Hue.setup', return_value='Bridge')

    # Given
    ip_address = '127.0.0.1'

    # When
    h = Hue(ip_address)

    # Then
    assert h.bridge_ip == ip_address
    assert h.bridge == 'Bridge'
    assert h.lights == lights


def test_hue_no_bridge(mocker):
    with pytest.raises(Exception) as e_info:
        # Given
        ip_address = '0.0.0.0'

        # When
        h = Hue(ip_address)

        # Then
        assert e_info == 'Press the link button on your Hue bridge and' \
                         'then try again within 30 seconds.'


def test_hue_set_lights_xy(mocker):
    lights = [mocker.MagicMock() for _ in range(2)]
    mocker.patch('hkolorize.hue.Hue.get_lights', return_value=lights)
    mocker.patch('hkolorize.hue.Hue.setup', return_value='Bridge')

    # Given
    ip_address = '127.0.0.1'

    # When
    h = Hue(ip_address)
    xy = (0.4, 0.6)
    brightness = 212
    transitiontime = 30

    h.set_lights_xy(xy, brightness, transitiontime)

    # Then
    for light in h.lights:
        assert light.xy == xy
        assert light.brightness == brightness
        assert light.transitiontime == transitiontime
        assert light.on


def test_hue_set_lights_rgb_black(mocker):
    lights = [mocker.MagicMock() for _ in range(2)]
    mocker.patch('hkolorize.hue.Hue.get_lights', return_value=lights)
    mocker.patch('hkolorize.hue.Hue.setup', return_value='Bridge')

    # Given
    ip_address = '127.0.0.1'

    # When
    h = Hue(ip_address)
    rgb = (0, 0, 0)

    h.set_lights_rgb(rgb)

    # Then
    for light in h.lights:
        assert light.brightness == 0
        assert light.on == False


def test_hue_set_lights_random(mocker):
    mocker.patch('hkolorize.hue.Hue.get_lights', return_value=[mocker.MagicMock()])
    mocker.patch('hkolorize.hue.Hue.setup', return_value='Bridge')

    # Given
    ip_address = '127.0.0.1'

    # When
    h = Hue(ip_address)
    h.set_lights_random()

    # Then
    light = h.lights[0]

    assert 0 <= light.xy[0] <= 1
    assert 0 <= light.xy[1] <= 1
    assert light.on
