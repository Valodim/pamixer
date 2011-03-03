
def center(str, width):
    """ Centers a string for the given width """
    if len(str) >= width:
        return str[0:width]

    return ( " " * int( width/2 - len(str)/2 -1 ) ) + str
