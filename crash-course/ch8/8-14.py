def make_car(manufacturer, model_name, **args):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    for k, v in args.items():
        car[k] = v
    return car


car = make_car(' subaru', 'outback', color =' blue', tow_package = True)

print(str(car))