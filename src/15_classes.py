# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
print('\n *** LatLon *** \n')
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def coords(self):
        return(self.lat, self.lon)
new_latLon = LatLon(2, 4)
print(new_latLon.coords())



# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
print('\n *** Waypoint *** \n')
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def display_all(self):
        return(self.name, self.lat, self.lon)
    def __str__(self):
        return 'Name: {self.name} lat: {self.lat}, lon: {self.lon}'.format(self=self)

    

new_waypoint = Waypoint('home', 22, 42)
print(new_waypoint.display_all())

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
print('\n *** GeoCache *** \n ')
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

geocache = Geocache('home', 'hard', '13km', 13.2, 351.2)
print(geocache.display_all())

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
print('\n *** Catacomb Waypoint *** \n')
catacomb_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(catacomb_waypoint.display_all())

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint('Grand Canyon', 12,13)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache)

# Print it--also make this print more nicely
print(geocache)
