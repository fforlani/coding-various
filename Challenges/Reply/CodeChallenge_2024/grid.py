from typing import List
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations, combinations
from collections import Counter
import random

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"

class Gold(Point):
    def __init__(self,line) -> None:
        if line[-1] == "\n": line = line[:-1]
        x,y = line.split(" ")
        super().__init__(int(x), int(y))
    def __repr__(self): return f"[{self.__str__()}]"

class Silv(Point):
    def __init__(self,line) -> None:
        if line[-1] == "\n": line = line[:-1]
        x,y,v = line.split(" ")
        super().__init__(int(x), int(y))
        self.v = int(v)
        self.goodnes = None
        self.gold_id = None
    def __repr__(self): return f"[{self.__str__()}, {self.v}]"


class Tile:
    
    def __init__(self, line):
        if line[-1] == "\n": line = line[:-1]
        t,c,n = line.split(" ")
        
        self.c = int(c)
        self.n = int(n)
        
        self.t = t
        self.dir = [False, False, False, False] #brtl

    def __repr__(self): return f"[{self.t}, {self.c}, {self.n}]"
    
    def get_type(self):
        match self.t:
            case "3": self.dir[1]= True; self.dir[3]= True 
            case "C": self.dir[0]= True; self.dir[2]= True 
            case "5": self.dir[0]= True; self.dir[1]= True 
            case "6": self.dir[0]= True; self.dir[3]= True 
            case "9": self.dir[1]= True; self.dir[2]= True 
            case "A": self.dir[2]= True; self.dir[3]= True
            case _: self.dir = [True, True, True, True]
        match self.t:
            case "7": self.dir[2]= False 
            case "B": self.dir[0]= False 
            case "D": self.dir[3]= False 
            case "E": self.dir[1]= False 
        
class Slot(Point):
    def __init__(self,t,x,y) -> None:
        super().__init__(x,y)
        self.t = t
    def __repr__(self): return f"[{self.__str__()}, {self.t}]"


filenames = ["00-trailer.txt",
            "01-comedy.txt",
            "02-sentimental.txt",
            "03-adventure.txt",
            "04-drama.txt",
            "05-horror.txt"]
    
class Grid:
    
    def __init__(self, filename=None, idx=0) -> None:
        self.filename = filename if filename is not None else filenames[idx]
        with open("input/" + self.filename, "r") as f: 
            self.lines = f.readlines()

        self.dims = self.get_dims()
        self.grid = None

        self.golds = self.get_golds(self.dims[2], 1)
        self.silvs = self.get_silvs(self.dims[3], self.dims[2]+1)
        self.tiles = self.get_tiles(self.dims[4], self.dims[3]+self.dims[2]+1)

        self.shapes = {t.t for t in self.tiles}

    def get_dims(self):

        dims = self.lines[0].split(" ")
        dims[-1] = dims[-1][:-1] 

        X, Y = int(dims[0]), int(dims[1])
        G, S, T = int(dims[2]), int(dims[3]), int(dims[4])
        return [X,Y,G,S,T]

    
    def get_golds(self,n,s): return [Gold(l) for l in self.lines[s:s+n]]
    def get_silvs(self,n,s): return [Silv(l) for l in self.lines[s:s+n]]
    def get_tiles(self,n,s): return [Tile(l) for l in self.lines[s:s+n]]
    def get_slots(self): return self.slots


class Solution:
    def __init__(self, i) -> None:
        self.g = Grid(idx=i)
        self.slots = []

    @property
    def tiles(self): return self.g.tiles

    @property
    def golds(self): return self.g.golds

    @property
    def silvs(self): return self.g.silvs
    
    def print_output(self):
        with open("output/" + self.filename, "r") as f: 
            for s in self.slots:
                line = f'{s.t} {s.x} {s.y}'
                f.write(line)
                print(line)
    
    """ The solution is valid if:
         - the path connect all Golden Points
         - the number of tiles used is at most equals to the given number (for each type) and tiles are correctly placed
         - there is at most one tiles in each point of the grid (and no tiles on Golden Points)
    """
    def is_valid_solution(self) -> bool:
        raise NotImplementedError()
    
    def calculate_score(self):
        score = 0
        # score earned of the path
        """ for g1, g2 in combinations(self.golds, 2):
            paths = {}
            cur_cost, cur_score = 0
            for slot in self.slots:
                if  """
        for slot in self.slots:
            for silv in self.silvs:
                if slot.x == silv.x and slot.y == silv.y:
                    score += silv.v

        # cost of the path
        for slot in self.slots:
            for tile in self.tiles:
                if slot.t == tile.t:
                    score -= tile.c
        return max(score, 0)
    
    @staticmethod
    def are_point_close(p1: Point, p2: Point) -> bool:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y) == 1

    @staticmethod
    def dist(p1: Point, p2: Point):
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
    
    @staticmethod
    def middle(p1: Point, p2: Point) -> Point:
        return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    def exact_shortest_path(self, points: List[Point]):
        shortest_distance = float('inf')
        shortest_path = None
        for permutation in permutations(points):
            total_distance = 0
            for i in range(len(permutation) - 1):
                total_distance += self.dist(permutation[i], permutation[i+1])
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = permutation
        return shortest_path
    
    def get_silv_goodness(self, silv: Silv) -> int:
        mid = self.middle(self.golds[silv.gold_id], self.golds[silv.gold_id])
        return (silv.v ** 2) / self.dist(silv, mid)
    
    def get_steps(self, silv_num = 5):
        self.g.golds = np.array(self.exact_shortest_path(self.golds))

        for silv in self.silvs:
            min_dist = float('inf')
            for i in range(len(self.golds) - 1):
                mid = self.middle(self.golds[i], self.golds[i + 1])
                if min_dist > self.dist(silv, mid):
                    min_dist = self.dist(silv, mid)
                    silv.gold_id = i

        for silv in self.silvs:
            silv.goodnes = self.get_silv_goodness(silv)

        step = []
        for i in range(len(self.golds) - 1):
            step += [self.golds[i]] + sorted(filter(lambda x: x.gold_id == i,self.silvs), key=lambda x: -x.goodnes)
            if len(step) > silv_num:
                step = step[:silv_num]
        step += [self.golds[-1]]
        return step
    
    def is_golden_point(self, p: Point) -> bool:
        for g in self.golds:
            if g.x == p.x and g.y == p.y:
                return True
        return False
    
    def solve(self):
        steps = self.get_steps()
        print(steps)
        for i in range(len(steps) - 1):
            path = Path(steps[i], steps[i + 1], 5, self)
            self.slots += path.get_path()
            if self.is_golden_point(i): 
                self.slots.pop(-1)
        self.slots += [steps[-1]]
        self.print_output()

    def get_tile_cost(self, t: str) -> int:
        for tile in self.tiles:
            if t == tile.t:
                return tile.c
        raise RuntimeError(f'Tile {t} not defines')

class Path:
    def __init__(self, p1, p2, N, sol: Solution) -> None: # N numero di cammini random
        self.sol = sol
        self.p1 = p1
        self.p2 = p2
        self.a = self.connect(p1, p2, N) # possibilit spostamenti (es: destra sinistra sopra sotto)
        self.b = list(map(self.to_directions, self.a)) # associa agli spostamenti a (tuple) una lettera identificativa
        self.c = list(map(self.to_tiles, self.b))  # tiles usabili per ogni spostamento
        self.d = list(map(self.to_coords, self.a)) #possibili percorsi: insieme dei punti per cui passare
        self.choice_quad(p1, p2)

    def get_path(self) -> List[Slot]:
        paths = list(range(len(self.c)))
        paths = filter(lambda i: self.is_valid_path(self.c[i]), paths)
        sorted(paths, cmp = lambda i: -sum([self.sol.get_tile_cost(t) for t in self.c[i]]))
        chosen_path = paths[0]
        slots = []
        for i in range(len(self.c[0])):
            slots += Slot(self.c[chosen_path], self.p1.x + self.d[chosen_path][0], self.p1.y + self.d[chosen_path][1])
        return slots
    
    def is_valid_path(self, tiles: List[tuple[int, int]]) -> bool:
        count = Counter(self.c)
        for t, c in count.items():
            if c > self.sol.get_tile_cost(t): return False
        return True

    def choice_quad(self, p1, p2):
        if p2.x >= p1.x and p2.y < p1.y:
            self.c = list(map(self.rot90anti, self.c))      
            self.d = list(map(self.inv_v, self.d))
        if p2.x  < p1.x and p2.y < p1.y:
            self.c = list(map(self.rot90anti, self.c))      
            self.c = list(map(self.rot90anti, self.c))      
            self.d = list(map(self.inv_v, self.d))
            self.d = list(map(self.inv_h, self.d))
        if p2.x < p1.x and p2.y >= p1.y:
            self.c = list(map(self.rot90anti, self.c))      
            self.c = list(map(self.rot90anti, self.c))      
            self.c = list(map(self.rot90anti, self.c))      
            self.d = list(map(self.inv_h, self.d))

        
    def inv_h(self, tuples): return self.invert_coord(tuples, "h")
    def inv_v(self, tuples): return self.invert_coord(tuples, "v")

    def invert_coord(self, tuples, di):
        if di=="v": return [(self.p1.x+a,self.p1.y-b) for a,b in tuples]                
        if di=="h": return [(self.p1.x-a,self.p1.y+b) for a,b in tuples]                

    def rot90anti(self, tiles):
        def mt(tup):
            if tup == '9': return '5'
            if tup == '5': return '6'
            if tup == '6': return 'A'
            if tup == 'A': return '9'
            return None

        return [mt(a) for a in tiles]        

    def to_coords(self, perm):
        x, y = 0, 0
        res = [(0,0)]
        for p in perm:
            if p == 1: y += 1
            if p == 0: x += 1
            res.append((x, y))
        return res

    def to_directions(self, perm):
        def mt(tup):
            if tup == (0,0): return 'H'
            if tup == (0,1): return 'N'
            if tup == (1,0): return 'P'
            if tup == (1,1): return 'V'
            return None

        return [mt((a, b)) for a, b in zip(perm[:-1], perm[1:])]

    def to_tiles(self, di):
        def mt(t):
            if t == 'H': return '3'
            if t == 'N': return 'A'
            if t == 'P': return '5'
            if t == 'V': return 'C'
            return None
        return [mt(ti) for ti in di]

    def connect(self, p1, p2, N=10):
        w = abs(p1.x - p2.x)
        l = abs(p1.y - p2.y)
        v = [0] * w + [1] * l
        return [random.sample(v, w + l) for i in range(N)]

s = Solution(1)
s.solve()
print(s.calculate_score())

""" p = Path(Point(0,0), Point(-5,3))
print(p.a)
print(p.b)
print(p.c)
print(p.d) """

def read_solution(idx: int) -> Solution:
    tmp = Solution(idx)
    filename = filenames[idx]
    with open("output/" + filename, "r") as f: 
        lines = f.readlines()
    slots = []
    for line in lines:
        t, x, y = line.replace('\n', '').split(" ")
        slots.append(Slot(t, int(x), int(y)))
    tmp.slots = slots
    return tmp

def print_grid(g: Grid) -> None:
    grid = np.zeros((g.dims[0], g.dims[1]))
    plt.figure(figsize=(10, 10))
    silvs = np.array([(silv.x, silv.y) for silv in g.silvs])
    golds = np.array([[gold.x, gold.y] for gold in g.golds])
    plt.scatter(silvs[:, 1], silvs[:, 0], s=20, c=[silv.v for silv in g.silvs], marker='o', alpha=0.5)
    plt.scatter(golds[:, 1], golds[:, 0], s=20, c='red', marker='x', alpha=0.5)

    plt.imshow(grid, cmap='hot_r', interpolation='nearest')
    plt.show()
    
test = read_solution(0)
print(test.calculate_score())