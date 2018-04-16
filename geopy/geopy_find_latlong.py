from geopy.geocoders import Nominatim
geolocator = Nominatim()
addressSearch = input("Enter address")
location = geolocator.geocode(addressSearch)
print(location.address)
print("latitude:",location.latitude)
print("longitude:",location.longitude)

