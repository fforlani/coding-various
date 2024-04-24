from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stops = set()
        for route in routes:
            stops.update(route)

        min_dist = {stop : float('inf') for stop in stops}
        min_dist[source] = 0
        updated = True
        while updated:
            updated = False
            for route in routes:
                mini = min([min_dist[stop] for stop in route])
                if mini != float('inf'):
                    for stop in route:
                        if min_dist[stop] > mini + 1:
                            min_dist[stop] = mini + 1
                            updated = True
        return min_dist[target] if target in min_dist and min_dist[target] != float('inf') else -1