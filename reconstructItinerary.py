from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key= lambda x: x[1])
        manifest = defaultdict(list) 
        self.trip = []
        for e in tickets:
            manifest[e[0]].append(e[1])
        self.dfs(manifest, 'JFK')
        self.trip.reverse()
        return self.trip
        
    def dfs(self, manifest, flight):
        other_flights = manifest[flight]
        while other_flights:
            next_flight = other_flights.pop(0)
            self.dfs(manifest, next_flight)
        self.trip.append(flight)
            
