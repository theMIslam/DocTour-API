from api.common.services import Service
from api.cities.models import City

class CityService(Service):
    model = City
