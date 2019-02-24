def get_coords_from_planet_name(planet_name):
    """
    Extract coordinates from a given planet name. (Example 'Becks[1:15:11]')
    :param planet_name:
    :return:
    """
    splitted = "".join([i for i in planet_name if i.isdigit() or i == ':']).split(":")
    return splitted[0], splitted[1], splitted[2]
