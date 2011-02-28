
def center(str, width):
    """ Centers a string for the given width """
    if len(str) >= width:
        return str[0:width]

    return ( " " * int( (width -len(str) -0.5) /2) ) + str
