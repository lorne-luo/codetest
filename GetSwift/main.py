from model import DEPOT, Position, DEPOT_LONGITUDE, DEPOT_LATITUDE

if __name__ == "__main__":
    print DEPOT.get_delivery_time(Position(DEPOT_LONGITUDE, DEPOT_LATITUDE - 1))
    print DEPOT.get_delivery_time(Position(DEPOT_LONGITUDE - 1, DEPOT_LATITUDE))
