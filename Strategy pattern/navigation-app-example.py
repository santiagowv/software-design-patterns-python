from abc import ABC, abstractmethod
from math import sin, cos, sqrt, atan2, radians

def distance_km(coordinates_A:tuple, coordinates_B:tuple) -> float:
    R = 6373.0

    lat1 = radians(coordinates_A[0])
    lon1 = radians(coordinates_A[1])
    lat2 = radians(coordinates_B[0])
    lon2 = radians(coordinates_B[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

class RouteStrategy(ABC):
    @abstractmethod
    def generate_route(self, distnace:float) -> float:
        pass

class RoadStrategy(RouteStrategy):
    avg_1km_time = 35 / 60
    def generate_route(self, distance:float) -> float:
        return int(distance * self.avg_1km_time)

class WalkingStrategy(RouteStrategy):
    avg_1km_time = 12
    def generate_route(self, distance:float) -> float:
        return int(distance * self.avg_1km_time)

class PublicTransportStrategy(RouteStrategy):
    avg_1km_time = 3
    def generate_route(self, distance:float) -> float:
        return int(distance * self.avg_1km_time)

class CityRoute:
    def __init__(self, name:str, x_coordinate:float, y_coordinate:float):
        self.name = name
        self.x_coordinate_B = x_coordinate
        self.y_coordinate_B = y_coordinate
        
class CityRoutes:
    def __init__(self):
        self.routes = {}

    def add_route(self, name:str, x_coordinate:float, y_coordinate:float) -> None:
        self.routes[name] = CityRoute(name, x_coordinate, y_coordinate)

    def show_route_information(self, name:str) -> None:
        route = self.routes[name]
        print("Name:", route.name)
        print("Coordinates:", (route.x_coordinate_B, route.y_coordinate_B))
    
    def get_route_coordinates(self, name:str) -> tuple:
        route = self.routes[name]
        return (route.x_coordinate_B, route.y_coordinate_B)

    def get_distance(self, name:str, x_coordinate_A:float, y_coordinate_A:float) -> float:
        coordinates_A = (x_coordinate_A, y_coordinate_A)
        coordiantes_B = self.get_route_coordinates(name)
        return distance_km(coordinates_A, coordiantes_B)

class Navigator:
    def __init__(self, route_strategy:RouteStrategy, x_coordinate:float, y_coordinate:float):
        self.routes = CityRoutes()
        self.route_strategy = route_strategy
        self.x_coordiante_A = x_coordinate
        self.y_coordinate_A = y_coordinate

    def add_new_route(self, name:str, x_coordinate:float, y_coordinate:float) -> None:
        self.routes.add_route(name, x_coordinate, y_coordinate)

    def show_all_routes(self) -> None:
        all_routes = [{"Yame":x.name, "Coodinate X:":x.x_coordinate_B, "Coordinate Y":x.y_coordinate_B} for x in self.routes.routes.values()]
        print(all_routes)

    def show_specific_route(self, name:str) -> None:
        self.routes.show_route_information(name)

    def create_route(self, name:str) -> None:
        print("Your destination information is:")
        self.show_specific_route(name)
        distance = self.routes.get_distance(name, self.x_coordiante_A, self.y_coordinate_A)
        print(f"It will take you {self.route_strategy.generate_route(distance)} minutes to get there.")


if __name__ == "__main__":
    strategy = RoadStrategy()
    nav = Navigator(strategy, x_coordinate = 52.22, y_coordinate = 21.01)
    
    nav.add_new_route("Downtown", x_coordinate = 52.02, y_coordinate = 19.02)
    nav.add_new_route("Mall", x_coordinate = 51, y_coordinate = 20.2)
    nav.add_new_route("Cinema", x_coordinate = 49.8, y_coordinate = 21.2)

    nav.show_all_routes()
    nav.show_specific_route("Downtown")

    nav.create_route("Downtown")
    
        

        