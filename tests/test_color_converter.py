from hkolorize import color_converter

from pytest import approx

def test_xy_from_rgb_red(mocker):
    # Given
    red = (255, 0, 0)

    # When
    xy = color_converter.xy_from_rgb(*red)

    # Then
    assert xy == approx((0.7006062, 0.2993009))


def test_xy_from_rgb_black(mocker):
    # Given
    black = (0, 0, 0)

    # When
    xy = color_converter.xy_from_rgb(*black)

    # Then
    assert xy == (0, 0)


def test_xy_from_rgb_white(mocker):
    # Given
    white = (255, 255, 255)

    # When
    xy = color_converter.xy_from_rgb(*white)

    # Then
    assert xy == approx((0.3227267, 0.3290229))
