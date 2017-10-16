#import make_car
#from make_car import make_car
#from make_car import make_car as mc
#import make_car as mc
from make_car import *

#car = make_car.make_car(' subaru', 'outback', color =' blue', tow_package = True)
#car = make_car(' subaru', 'outback', color =' blue', tow_package = True)
#car = mc(' subaru', 'outback', color =' blue', tow_package = True)
#car = mc.make_car(' subaru', 'outback', color =' blue', tow_package = True)
car = make_car(' subaru', 'outback', color =' blue', tow_package = True)

print(str(car))