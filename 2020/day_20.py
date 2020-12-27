#coding=utf8

TILE_EACH_LINE = 12
#TILE_EACH_LINE = 3

class tileVariation():
    def __init__(self, tile, tile_id):
        self.tile_id = tile_id

        self.tile = tile
        self.tile_flips = [self.tile, self.flip_h(self.tile), self.flip_v(self.tile), self.flip_hv(self.tile)]
        self.edge_flips = [self.get_edge(tile) for tile in self.tile_flips]

        self.variation_tiles = []
        self.variation_edges = []

        self.corner_tile = False
        self.edge_tile = False

        self.tile_on_puzzle = None
        self.edge_on_puzzle = None
        
        self.get_all_variations()

    def get_edge(self, tile):
        up = int(tile[0], base=2)
        down = int(tile[-1], base=2)
        left = int(''.join([tile[i][0] for i in range(0, len(tile))]), base=2)
        right = int(''.join([tile[i][-1] for i in range(0, len(tile))]), base=2)
        return [up, right, down, left]

    def flip_h(self, tile):
        tile = [tile[i] for i in range(len(tile)-1, -1, -1)]
        return tile

    def flip_v(self, tile):
        def reverse_line(line):
            return ''.join([line[i] for i in range(len(line)-1, -1, -1)])
        tile = [reverse_line(tile[i]) for i in range(len(tile))]
        return tile

    def flip_hv(self, tile):
        tile = [tile[i] for i in range(len(tile)-1, -1, -1)]
        def reverse_line(line):
            return ''.join([line[i] for i in range(len(line)-1, -1, -1)])
        tile = [reverse_line(tile[i]) for i in range(len(tile))]
        return tile

    def turn_left_90(self, tile, edge):
        new_tile = []
        for i in range(len(tile[0])-1, -1, -1):
            new_tile.append(''.join([tile[j][i] for j in range(len(tile))]))
        new_edge = self.get_edge(new_tile)
        return new_tile, new_edge

    def turn_all_degree(self, new_tile, new_edge):
        for i in range(4):
            self.variation_tiles.append(new_tile)
            self.variation_edges.append(new_edge)
            new_tile, new_edge = self.turn_left_90(new_tile, new_edge)
        
    def get_all_variations(self):
        for i in range(len(self.tile_flips)):
            self.turn_all_degree(self.tile_flips[i], self.edge_flips[i])

    def is_corner(self, edge_set):
        for i, edge in enumerate(self.variation_edges):
            is_c, available_edge = self.variation_is_corner(edge, edge_set)
            if is_c:
                self.variation_edges[i] = np.array(edge) * available_edge
                self.corner_tile = True
        return
        
    def variation_is_corner(self, tile, edge_set):
        if len(edge_set[tile[0]]) == 1 and len(edge_set[tile[1]]) == 1:
            return True, np.array([0, 0, 1, 1])
        if len(edge_set[tile[1]]) == 1 and len(edge_set[tile[2]]) == 1:
            return True, np.array([1, 0, 0, 1])
        if len(edge_set[tile[2]]) == 1 and len(edge_set[tile[3]]) == 1:
            return True, np.array([1, 1, 0, 0])
        if len(edge_set[tile[0]]) == 1 and len(edge_set[tile[3]]) == 1:
            return True, np.array([0, 1, 1, 0])
        return False, np.array([1, 1, 1, 1])

    def is_edge(self, edge_set):
        for i, edge in enumerate(self.variation_edges):
            is_e, available_edge = self.variation_is_edge(edge, edge_set)
            if is_e:
                self.variation_edges[i] = np.array(edge) * available_edge
                self.edge_tile = True
        return 
        
    def variation_is_edge(self, tile, edge_set):
        for i in range(4):
            if len(edge_set[tile[i]]) == 1:
                available = [1] * 4
                available[i] = 0
                return True, np.array(available)
        return False, np.array([1, 1, 1, 1])

    def find_variation(self, requirement):
        mask = np.array([requirement[i] != -1 for i in range(len(requirement))], dtype=int)
        requirement = np.array(requirement)
        for i, edge in enumerate(self.variation_edges):
            if (np.absolute(edge-requirement)*mask).sum() == 0:
                self.tile_on_puzzle = self.variation_tiles[i]
                self.edge_on_puzzle = edge
                return True
        return False

def load_data(filename):
    tiles = {}; edge_set = {}
    with open(filename, 'r') as f:
        tile_strs = f.read().strip().replace('#', '1').replace('.', '0')
    for tile in tile_strs.split('\n\n'):
        tlines = tile.split('\n')
        tile_id = int(tlines[0][5:9])
        tile_variation = tileVariation(tlines[1:], tile_id)
        tiles[tile_id] = (tile_variation)
        for edge in tile_variation.variation_edges:
            for dim in edge:
                if dim not in edge_set:
                    edge_set[dim] = set()
                edge_set[dim].add(tile_id)
    return tiles, edge_set

def onerow(corners, edges, others, tiles, edge_set, row_id, choosed, positions):
    ids = []
    edges = corners | edges
    for i in range(0, TILE_EACH_LINE):
        if row_id == 0 or row_id == TILE_EACH_LINE-1 or i == 0 or i == TILE_EACH_LINE-1:
            cands = edges - choosed
        else:
            cands = others

        if row_id == 0:
            up = 0
            down = -1
        else:
            up = tiles[positions[-1][len(ids)]].edge_on_puzzle[2]
            down = -1
        if row_id == TILE_EACH_LINE-1:
            down = 0
            
        if i == 0:
            left = 0
            right = -1
        else:
            left = tiles[ids[-1]].edge_on_puzzle[1]
            right = -1
        if i == TILE_EACH_LINE-1:
            right = 0

        for cand_id in cands:
            if tiles[cand_id].find_variation([up, right, down, left]):
                ids.append(cand_id)
                choosed.add(cand_id)
                break
    return ids, choosed

def merge_image(tiles, positions):
    rows = []
    for pos in positions:
        for i in range(len(pos)):
            tile_id = pos[i]
            tile = tiles[tile_id].tile_on_puzzle
            tile = [t[1:-1] for t in tile[1:-1]]
            if i == 0:
                pieces = tile
            else:
                for j in range(len(pieces)):
                    pieces[j] += tile[j]
        rows.extend(pieces)
    return rows

def load_nessie(nessie_str):
    nessie_corrdination = []
    for i, line in enumerate(nessie_str):
        for j in range(len(line)):
            if nessie_str[i][j] == '#':
                nessie_corrdination.append((i, j))
    target = (1, 0)
    nessie_corrdination = [(x-target[0], y-target[1]) for (x,y) in nessie_corrdination]
    return nessie_corrdination

def load_image(img):
    image_corrdination = {}
    cands_list = []
    for i, line in enumerate(img):
        for j in range(len(line)):
            if img[i][j] == '1':
                if i not in image_corrdination:
                    image_corrdination[i] = {}
                image_corrdination[i][j] = 0
                cands_list.append((i, j))
    return cands_list, image_corrdination

def check_nessie_tail(tail, image_corrdination, nessie):
    checked_cells = []
    for cell in nessie:
        x = tail[0]+cell[0]
        y = tail[1]+cell[1]
        if x in image_corrdination:
            if y in image_corrdination[x]:
                checked_cells.append((x, y))
            else:
                del checked_cells[:]
                break
        else:
            del checked_cells[:]
            break
    for cell in checked_cells:
        image_corrdination[cell[0]][cell[1]] = 1
    return len(checked_cells) > 0, image_corrdination

def find_nessie(images):
    nessie = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    nessie = load_nessie(nessie)
    has_nessie = False
    for img in images:
        cands_list, image_corrdination = load_image(img)
        for point in cands_list:
            find_nessie, image_corrdination = check_nessie_tail(point, image_corrdination, nessie)
            has_nessie = (has_nessie | find_nessie)
        if has_nessie:
            print ('has_nessie')
            water = 0
            for x in image_corrdination:
                for y in image_corrdination[x]:
                    water += (1-image_corrdination[x][y])
            return water
    return 0

def do_puzzle(corners, edges, others, tiles, edge_set):
    for tile_id in tiles:
        tile = tiles[tile_id]
    choosed = set(); positions = []
    for i in range(TILE_EACH_LINE):
        ids, choosed = onerow(corners, edges, others, tiles, edge_set, i, choosed, positions)
        positions.append(ids)
    image = merge_image(tiles, positions)
    image_obj = tileVariation(image, 0)
    return find_nessie(image_obj.variation_tiles)

def quiz_two(tiles, edge_set):
    corners = set(); edges = set(); others = set()
    for tile_id in tiles:
        tile = tiles[tile_id]
        tile.is_corner(edge_set)
        if tile.corner_tile:
            corners.add(tile_id)
        else:
            tile.is_edge(edge_set)
            if tile.edge_tile:
                edges.add(tile_id)
            else:
                others.add(tile_id)
    return do_puzzle(corners, edges, others, tiles, edge_set)

def quiz_one(tiles, edge_set):
    corners = []
    for tile_id in tiles:
        tile = tiles[tile_id]
        tile.is_corner(edge_set)
        if tile.corner_tile:
            corners.append(tile_id)
    return corners

if __name__ == '__main__':
    import numpy as np
    tiles, edge_set = load_data('day_20.txt')
    corners = quiz_one(tiles, edge_set)
    mlp = 1
    for c in corners:
        mlp *= c
    print (mlp)

    tiles, edge_set = load_data('day_20.txt')
    water = quiz_two(tiles, edge_set)
    print (water)
