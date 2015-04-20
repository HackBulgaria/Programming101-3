class Dungeon:
    OBSTACLE = "#"
    SPAWNING_POINT = "S"
    ENEMY = "E"
    EXIT = "G"
    TREASURE = "T"
    WALKABLE_PATH = "."
    HERO = "H"
    DIRECTIONS = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    @staticmethod
    def create_from_file(path):
        dungeon = []
        with open(path, "r") as f:
            contents = f.read().split("\n")
            dungeon = [list(line) for line in contents if line.strip() != ""]

        return Dungeon(dungeon)


    def __init__(self, dungeon_matrix):
        self.__map = dungeon_matrix
        self.__spawning_points = self.__find_spawning_points()
        self.__hero = None
        self.__hero_position = None

    def get_spawning_points(self):
        return self.__spawning_points

    def __find_spawning_points(self):
        spawning_points = []

        for row_index in range(0, len(self.__map)):
            for tile_index in range(0, len(self.__map[row_index
                ])):
                tile = self.__map[row_index][tile_index]
                if tile == Dungeon.SPAWNING_POINT:
                    spawning_points.append((row_index, tile_index))

        return spawning_points
   
    def __place_on_map(self, point, entity):
        self.__map[point[0]][point[1]] = entity
    
    def __can_make_move(self, point):
        x, y = point
        if x < 0 or x >= len(self.__map):
            return False

        if y < 0 or y >= len(self.__map[0]):
            return False

        if self.__map[x][y] == Dungeon.OBSTACLE:
            return False
        
        return True

    def __str__(self):
        return "\n".join(["".join(line) for line in self.__map])
    
    def spawn(self, hero):
        if len(self.__spawning_points) == 0:
            raise Exception("Cannot spawn hero.")
        
        self.__hero = hero
        self.__hero_position = self.__spawning_points.pop(0)

        self.__place_on_map(self.__hero_position, Dungeon.HERO)
    
    def __trigger_action_on_move(self, position):
        x, y = position
        entity = self.__map[x][y]
        if entity == Dungeon.TREASURE:
            print("Hero found treasure")
            return False
        
        if entity == Dungeon.ENEMY:
            print("A fight starts")
            print("Enemy wins")
            return True


    def move(self, direction):
        if direction not in Dungeon.DIRECTIONS:
            raise Exception("{} is not a valid direction".format(direction))

        dx, dy = Dungeon.DIRECTIONS[direction]
        hero_x, hero_y = self.__hero_position
        
        new_position = (hero_x + dx, hero_y + dy)
        
        if self.__can_make_move(new_position):
            self.__place_on_map((hero_x, hero_y), Dungeon.WALKABLE_PATH)
            is_dead = self.__trigger_action_on_move(new_position)
            
            if is_dead:
                self.spawn(self.__hero)
                return

            self.__hero_position = new_position
            self.__place_on_map(new_position, Dungeon.HERO)



class Hero:
    pass

def main():
    d = Dungeon.create_from_file("level1.txt")
    print(d)
    print(d.get_spawning_points())
    h = Hero()

    d.spawn(h)
    print(d)
    d.move("right")
    print(d)

if __name__ == "__main__":
    main()
