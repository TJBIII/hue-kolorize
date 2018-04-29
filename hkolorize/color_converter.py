def xy_from_rgb(r, g, b):
    """ Convert rgb color to xy format for Hue.
        The colorsys module is used for other conversions but does not support xy. 
    """

    # apply a gamma correction to the r,g,b values
    red = ((r + 0.055) / (1.0 + 0.055)) ** 2.4 if (r > 0.04045) else (r / 12.92);
    green = ((g + 0.055) / (1.0 + 0.055)) ** 2.4 if (g > 0.04045) else  (g / 12.92);
    blue = ((b + 0.055) / (1.0 + 0.055)) ** 2.4 if (b > 0.04045) else (b / 12.92); 

    # convert the RGB values to XYZ using the Wide RGB D65 conversion formula 
    X = red * 0.664511 + green * 0.154324 + blue * 0.162028;
    Y = red * 0.283881 + green * 0.668433 + blue * 0.047685;
    Z = red * 0.000088 + green * 0.072310 + blue * 0.986039;

    # calculate the xy values from the XYZ values
    if sum([X, Y, Z]) == 0:
        x = y = 0
    else:
        x = X / (X + Y + Z);
        y = Y / (X + Y + Z);

    return (x, y)
