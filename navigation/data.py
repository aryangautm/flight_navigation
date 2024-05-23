import csv


class Airport:
    def __init__(
        self,
        id,
        name,
        city,
        country,
        iata,
        icao,
        latitude,
        longitude,
        altitude,
        timezone,
        dst,
        database,
        type,
        source,
    ):
        self.id = int(id)
        self.name = name.strip('"')
        self.city = city.strip('"')
        self.country = country.strip('"')
        self.iata = iata.strip('"')
        self.icao = icao.strip('"')
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.altitude = int(altitude)
        self.timezone = float(timezone) if timezone != "\\N" else -100
        self.dst = dst.strip('"')
        self.database = database.strip('"')
        self.type = type.strip('"')
        self.source = source.strip('"')


class AirportData:
    def __init__(self, filename):
        self.airport_data = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                airport = Airport(*row)
                self.airport_data.append(airport)

    def getdata(self):
        return self.airport_data

    def getLatitude(self, id_or_name):
        for airport in self.airport_data:
            if airport.id == id_or_name or airport.name == id_or_name:
                return airport.latitude
        return 0

    def getLongitude(self, id_or_name):
        for airport in self.airport_data:
            if airport.id == id_or_name or airport.name == id_or_name:
                return airport.longitude
        return 0

    def getName(self, id):
        for airport in self.airport_data:
            if airport.id == id:
                return airport.name
        return ""

    def getNameLatLong(self, id):
        for airport in self.airport_data:
            if airport.id == id:
                return (airport.name, (airport.latitude, airport.longitude))
        return ("", (0, 0))


class Airline:
    def __init__(self, id, name, alias, iata, icao, callsign, country, active):
        self.id = int(id)
        self.name = name.strip('"')
        self.alias = alias.strip('"')
        self.iata = iata.strip('"') if iata else iata
        self.icao = icao.strip('"') if icao else icao
        self.callsign = callsign.strip('"') if callsign else callsign
        self.country = country.strip('"') if country else country
        self.active = active.strip('"')


class AirlineData:
    def __init__(self, filename):
        self.airline_data = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                airline = Airline(*row)
                self.airline_data.append(airline)

    def getdata(self):
        return self.airline_data


class Route:
    def __init__(
        self,
        airline_code,
        id,
        source_code,
        source_id,
        dest_code,
        dest_id,
        codeshare,
        stops,
        equipment,
    ):
        self.airline_code = airline_code
        self.id = int(id) if id != "\\N" else -100
        self.source_code = source_code
        self.source_id = int(source_id) if source_id != "\\N" else -100
        self.dest_code = dest_code
        self.dest_id = int(dest_id) if dest_id != "\\N" else -100
        self.codeshare = codeshare
        self.stops = int(stops)
        self.equipment = equipment


class RouteData:
    def __init__(self, filename):
        self.route_data = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                route = Route(*row)
                self.route_data.append(route)

    def getdata(self):
        return self.route_data
