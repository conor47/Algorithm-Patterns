# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flightMap = collections.defaultdict(list)
        
        for ticket in tickets:
            origin = ticket[0]
            destination = ticket[1]
            self.flightMap[origin].append(destination)
            
        self.visitBitmap = {}
        
        for origin,itinerary in self.flightMap.items():
            itinerary.sort()
            self.visitBitmap[origin] = [False] * len(itinerary)
        
        self.result = []
        self.flights = len(tickets)
        route = ['JFK']
        self.DFS('JFK', route)
        
        return self.result
    
    def DFS(self, origin,route):
        if len(route) == self.flights + 1:
            self.result = route
            return True
        
        for i,nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                self.visitBitmap[origin][i] = True
                ret = self.DFS(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True
        return False