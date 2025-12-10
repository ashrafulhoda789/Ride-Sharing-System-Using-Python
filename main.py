from ride import RideSharing, Ride, RideRequest, RideMatching
from users import Rider, Driver
from vehicle import Car, Bike

pathao = RideSharing("Pathao")
rahim = Rider("Rahim", "rahim@gmail.com", 1234, "Bodo Guarage", 1200)
pathao.add_rider(rahim)
karim = Driver("Karim", "karim@gmail.com", 1256, "Boddarhat")
pathao.add_driver(karim)

rahim.request_ride(pathao, "New Market", "car")
rahim.show_current_ride()
karim.reach_destination(rahim.current_ride)
print(pathao)