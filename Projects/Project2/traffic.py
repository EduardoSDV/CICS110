# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477



def stop(traffic_light, pedestrian):
    if (traffic_light == 'Red') or (pedestrian == True):
        return True
    else:
        return False

print(stop('Red', False))
print(stop('Green', False))

def move_forward(traffic_light, pedestrian):
    if traffic_light == 'Red':
        return False
    elif (traffic_light == 'Green' or 'Yellow') and pedestrian == True:
        return False
    else:
        return True


print(move_forward('Green', False))
print(move_forward('Red', False))
print(move_forward('Yellow', False))
print(move_forward('Yellow', True))


def turn_left(traffic_light, pedestrian, cars_opposite):
    if (traffic_light == 'Green') and (pedestrian == False) and (cars_opposite == False) :
        return True
    else:
        return False

print(turn_left('Green',False,False))




