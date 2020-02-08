from ground_station import start_ground_station
from flight_software import start_flight_software

from sys import argv

if __name__ == '__main__':
    if 'ground_station' in ''.join(argv) or 'ground' in ''.join(argv):
        start_ground_station()
    elif 'flight_software' in ''.join(argv) or 'flight' in ''.join(argv):
        start_flight_software()
    elif input("Run ground Station [Y]/n ? ").lower() != 'n':
        start_ground_station()
    else:
        start_flight_software()
