import pygame as pg
import sys  

# Satranç taşları için bir sınıf
class ChessPiece:
    
    def __init__(self, name, image_path, tile_size):

        self.name = name
        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (tile_size, tile_size))

    def draw(self, sc, x, y, tile_size):

        sc.blit(self.image, (x * tile_size, y * tile_size))

# Satranç tahtası için bir sınıf
class ChessBoard:

    def __init__(self, cols, rows, tile_size, bg_image_path):
        
        self.cols = cols
        self.rows = rows
        self.tile_size = tile_size
        self.bg = pg.image.load(bg_image_path).convert_alpha()
        self.bg = pg.transform.scale(self.bg, (cols * tile_size, rows * tile_size))

    def draw(self, sc):
    
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pg.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                sc.blit(self.bg, rect, rect)  # Resmi her hücreye uygun şekilde çiz


# Satranç oyununu yöneten sınıf
class ChessGame:
    
    def __init__(self, cols, rows, tile_size):
    
        self.board = ChessBoard(cols, rows, tile_size, './img/cb.png')
        self.pieces = {}
        self.selected_piece = None
        self.tile_size = tile_size
        self.turn = True 

        # Siyah taşlar
        self.load_pieces()

    def load_pieces(self):
    
        # Siyah taşlar yükleniyor
        self.pieces = {
    
            #Siyah taşlar 
            (0, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (1, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (2, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (3, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (4, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (5, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (6, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (7, 6): ChessPiece("bp", "./img/bp.png", self.tile_size),
            (0, 7): ChessPiece("bR", "./img/bR.png", self.tile_size),
            (1, 7): ChessPiece("bN", "./img/bN.png", self.tile_size),
            (2, 7): ChessPiece("bB", "./img/bB.png", self.tile_size),
            (3, 7): ChessPiece("bK", "./img/bK.png", self.tile_size),
            (4, 7): ChessPiece("bQ", "./img/bQ.png", self.tile_size),
            (5, 7): ChessPiece("bB", "./img/bB.png", self.tile_size),
            (6, 7): ChessPiece("bN", "./img/bN.png", self.tile_size),
            (7, 7): ChessPiece("bR", "./img/bR.png", self.tile_size),
        
            # Beyaz taşlar
            (0, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (1, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (2, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (3, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (4, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (5, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (6, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (7, 1): ChessPiece("wp", "./img/wp.png", self.tile_size),
            (0, 0): ChessPiece("wR", "./img/wR.png", self.tile_size),
            (1, 0): ChessPiece("wN", "./img/wN.png", self.tile_size),
            (2, 0): ChessPiece("wB", "./img/wB.png", self.tile_size),
            (3, 0): ChessPiece("wQ", "./img/wQ.png", self.tile_size),
            (4, 0): ChessPiece("wK", "./img/wK.png", self.tile_size),
            (5, 0): ChessPiece("wB", "./img/wB.png", self.tile_size),
            (6, 0): ChessPiece("wN", "./img/wN.png", self.tile_size),
            (7, 0): ChessPiece("wR", "./img/wR.png", self.tile_size),}

    def draw(self, sc):

        self.board.draw(sc)
        for (x, y), piece in self.pieces.items():
            piece.draw(sc, x, y, self.tile_size)

    def get_click_mouse_pos(self, events):

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Sol tık kontrolü
                x, y = pg.mouse.get_pos()
                grid_x, grid_y = x // self.tile_size, y // self.tile_size
                return grid_x, grid_y

        return None

    def hareketler(self, kordinat, isim):

        renk = (255, 0, 0)
        yeşil = (0,255,0)
    
        if isim == "bp":
            if ((kordinat[0],kordinat[1]-1) in self.pieces) and (self.pieces[(kordinat[0],kordinat[1]-1)].name[0] != isim[0]):
                red_rect_1 = pg.Rect((kordinat[0] - 1)  * self.tile_size, (kordinat[1] - 1) * self.tile_size, self.tile_size, self.tile_size)
                red_rect_2 = pg.Rect((kordinat[0] + 1) * self.tile_size, (kordinat[1] - 1) * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, yeşil, red_rect_1, 3)
                pg.draw.rect(sc, yeşil, red_rect_2, 3)
            else:
                red_rect = pg.Rect(kordinat[0] * self.tile_size, (kordinat[1] - 1) * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, red_rect, 3)

        elif isim == "wp":
            if ((kordinat[0],kordinat[1]+1) in self.pieces) and (self.pieces[(kordinat[0],kordinat[1]+1)].name[0]  != isim[0]):
                red_rect_1 = pg.Rect((kordinat[0] - 1)  * self.tile_size, (kordinat[1] + 1) * self.tile_size, self.tile_size, self.tile_size)
                red_rect_2 = pg.Rect((kordinat[0] + 1) * self.tile_size, (kordinat[1] + 1) * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, yeşil, red_rect_1, 3)
                pg.draw.rect(sc, yeşil, red_rect_2, 3)
            else:
                red_rect = pg.Rect(kordinat[0] * self.tile_size, (kordinat[1] + 1) * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, red_rect, 3)

        if isim == "bR" or isim == "wR" :
            # Sağ yöne doğru hareket et
            for i in range(kordinat[0] + 1, self.board.cols):
                if (i, kordinat[1]) in self.pieces:  # Eğer bu karede bir taş varsa hareket durur
                    if self.pieces[(i, kordinat[1])].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  # Karşı takımın taşıysa oraya kadar gidebilir
                        rect = pg.Rect(i * self.tile_size, kordinat[1] * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(i * self.tile_size, kordinat[1] * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

            # Sol yöne doğru hareket et
            for i in range(kordinat[0] - 1, -1, -1):
                if (i, kordinat[1]) in self.pieces:  # Eğer bu karede bir taş varsa hareket durur
                    if self.pieces[(i, kordinat[1])].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  # Karşı takımın taşıysa oraya kadar gidebilir
                        rect = pg.Rect(i * self.tile_size, kordinat[1] * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(i * self.tile_size, kordinat[1] * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

            # Yukarı yöne doğru hareket et
            for i in range(kordinat[1] - 1, -1, -1):
                if (kordinat[0], i) in self.pieces:  # Eğer bu karede bir taş varsa hareket durur
                    if self.pieces[(kordinat[0], i)].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  # Karşı takımın taşıysa oraya kadar gidebilir
                        rect = pg.Rect(kordinat[0] * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(kordinat[0] * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

            # Aşağı yöne doğru hareket et
            for i in range(kordinat[1] + 1, self.board.rows):
                if (kordinat[0], i) in self.pieces:  # Eğer bu karede bir taş varsa hareket durur
                    if self.pieces[(kordinat[0], i)].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  # Karşı takımın taşıysa oraya kadar gidebilir
                        rect = pg.Rect(kordinat[0] * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(kordinat[0] * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

        if isim == "bN" or isim == "wN":
            
            yerler = [(kordinat[0]-1 , kordinat[1]+2), (kordinat[0]+1 , kordinat[1]+2,),
                      (kordinat[0]-1 , kordinat[1]-2,),(kordinat[0]+1 , kordinat[1]-2,),
                      (kordinat[0]-2 , kordinat[1]+1), (kordinat[0]+2 , kordinat[1]+1,),
                      (kordinat[0]-2 , kordinat[1]-1,),(kordinat[0]+2 , kordinat[1]-1,)]
            
            for i in yerler:

                if (i in self.pieces) and (self.pieces[i].name[0] != isim[0]):
                    red_rect = pg.Rect(i[0]  * self.tile_size, i[1] * self.tile_size, self.tile_size, self.tile_size)
                    pg.draw.rect(sc, yeşil, red_rect, 3)

                elif (i in self.pieces) and (self.pieces[i].name[0] == isim[0]):
                    continue
                else:
                    red_rect = pg.Rect(i[0]  * self.tile_size, i[1] * self.tile_size, self.tile_size, self.tile_size)
                    pg.draw.rect(sc, renk, red_rect, 3)

        if isim == "bB" or isim == "wB":  # Fil için
 
            tile_size = self.tile_size
            
            # Yukarı sağ
            for i in range(1, min(self.board.cols - kordinat[0], self.board.rows -  kordinat[1])):
                new_x, new_y =  kordinat[0] + i,  kordinat[1] + i
                if (new_x, new_y) in self.pieces:  # Eğer bu karede bir taş varsa hareket durur
                    if self.pieces[(new_x, new_y)].name[0] != self.pieces[( kordinat[0],  kordinat[1])].name[0]:  # Karşı takımın taşıysa oraya kadar gidebilir
                        rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

            # Yukarı sol
            for i in range(1, min( kordinat[0] + 1, self.board.rows -  kordinat[1])):
                new_x, new_y =  kordinat[0] - i,  kordinat[1] + i
                if (new_x, new_y) in self.pieces:  
                    if self.pieces[(new_x, new_y)].name[0] != self.pieces[(kordinat[0],  kordinat[1])].name[0]:  
                        rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

            # Aşağı sağ
            for i in range(1, min(self.board.cols -  kordinat[0],  kordinat[1] + 1)):
                new_x, new_y =  kordinat[0] + i, kordinat[1] - i
                if (new_x, new_y) in self.pieces:  
                    if self.pieces[(new_x, new_y)].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]: 
                        rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

            # Aşağı sol
            for i in range(1, min(kordinat[0] + 1, kordinat[1] + 1)):
                new_x, new_y = kordinat[0] - i, kordinat[1] - i
                if (new_x, new_y) in self.pieces: 
                    if self.pieces[(new_x, new_y)].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  
                        rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, yeşil, rect, 3)
                    break
                rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(sc, renk, rect, 3)

        if isim == "bQ" or isim == "wQ":  # Vezir
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for i in range(1, max(self.board.cols, self.board.rows)):
                    new_x = kordinat[0] + dx * i
                    new_y = kordinat[1] + dy * i
                    if 0 <= new_x < self.board.cols and 0 <= new_y < self.board.rows:
                        if (new_x, new_y) in self.pieces:  # Eğer bu karede bir taş varsa hareket durur
                            if self.pieces[(new_x, new_y)].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  # Karşı takımın taşıysa
                                rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                                pg.draw.rect(sc, renk, rect, 3)
                            break
                        rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, renk, rect, 3)

        # Şah için hareket alanı
        elif isim == "bK" or isim == "wK":  # Şah
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_x = kordinat[0] + dx
                new_y = kordinat[1] + dy
                if 0 <= new_x < self.board.cols and 0 <= new_y < self.board.rows:
                    if (new_x, new_y) in self.pieces:  # Eğer bu karede bir taş varsa
                        if self.pieces[(new_x, new_y)].name[0] != self.pieces[(kordinat[0], kordinat[1])].name[0]:  # Karşı takımın taşıysa
                            rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                            pg.draw.rect(sc, renk, rect, 3)
                    else:
                        rect = pg.Rect(new_x * self.tile_size, new_y * self.tile_size, self.tile_size, self.tile_size)
                        pg.draw.rect(sc, renk, rect, 3)    

    def taş_al(self, pos):
        if pos in self.pieces:
            del self.pieces[pos]

    def is_path_clear(self, start_pos, end_pos):

        # Dikey hareket
        if start_pos[0] == end_pos[0]:
            if start_pos[1] < end_pos[1]:
                step = 1
            else:
                step = -1
            for y in range(start_pos[1] + step, end_pos[1], step):
                if (start_pos[0], y) in self.pieces:
                    return False
        # Yatay hareket
        elif start_pos[1] == end_pos[1]:
            if start_pos[0] < end_pos[0]:
                step = 1
            else:
                step = -1
            for x in range(start_pos[0] + step, end_pos[0], step):
                if (x, start_pos[1]) in self.pieces:
                    return False
                    
        # Çapraz hareket
        else:
            step_x = 1 if start_pos[0] < end_pos[0] else -1
            step_y = 1 if start_pos[1] < end_pos[1] else -1
            for i in range(1, abs(start_pos[0] - end_pos[0])):
                if (start_pos[0] + i * step_x, start_pos[1] + i * step_y) in self.pieces:
                    return False
        return True

    def move_piece(self, start_pos, end_pos):

        piece = self.pieces.get(start_pos)
        if piece and end_pos not in self.pieces:

            if self.turn and piece.name[0] != "b":  # Sıra siyahlarda ama beyaz taş seçildi
                return False
            if not self.turn and piece.name[0] != "w":  # Sıra beyazlarda ama siyah taş seçildi
                return False

            if piece.name == "bp" and (start_pos[1] - end_pos[1] == 1) and (start_pos[0] - end_pos[0] == 0):
                self.pieces[end_pos] = self.pieces.pop(start_pos)
                self.turn = not self.turn 
            
            elif piece.name == "wp" and (start_pos[1] - end_pos[1] == -1) and (start_pos[0] - end_pos[0] == 0):
                self.pieces[end_pos] = self.pieces.pop(start_pos)
                self.turn = not self.turn 
            
            elif (piece.name == "bR" or piece.name == "wR") and ((start_pos[0] - end_pos[0] == 0) or (start_pos[1] - end_pos[1] == 0)):
                if self.is_path_clear(start_pos, end_pos):
                    self.pieces[end_pos] = self.pieces.pop(start_pos)
                    self.turn = not self.turn 
            
            elif piece.name == "bN" or piece.name == "wN":
                dx = abs(start_pos[0] - end_pos[0])
                dy = abs(start_pos[1] - end_pos[1])
                if (dx, dy) in [(1, 2), (2, 1)]:
                    self.pieces[end_pos] = self.pieces.pop(start_pos)
                    self.turn = not self.turn 
            
            elif piece.name == "bB" or piece.name == "wB":
                dx = abs(start_pos[0] - end_pos[0])
                dy = abs(start_pos[1] - end_pos[1])
                if dx == dy and self.is_path_clear(start_pos, end_pos):
                    self.pieces[end_pos] = self.pieces.pop(start_pos)
                    self.turn = not self.turn 

            elif piece.name == "bQ" or piece.name == "wQ":
                dx = abs(start_pos[0] - end_pos[0])
                dy = abs(start_pos[1] - end_pos[1])
                if (dx == dy or (start_pos[0] - end_pos[0] == 0) or (start_pos[1] - end_pos[1] == 0)):
                    if self.is_path_clear(start_pos, end_pos):
                        self.pieces[end_pos] = self.pieces.pop(start_pos)
                        self.turn = not self.turn 

            elif piece.name == "bK" or piece.name == "wK":
                dx = abs(start_pos[0] - end_pos[0])
                dy = abs(start_pos[1] - end_pos[1])
                if (dx, dy) in [(1, 1), (0, 1), (1, 0)]:
                    self.pieces[end_pos] = self.pieces.pop(start_pos)
                    self.turn = not self.turn 

        elif end_pos == start_pos:
            return

        else:
            if self.pieces[start_pos].name[0] != self.pieces[end_pos].name[0]:
                if piece.name == "bp":
                    if (start_pos[1] - end_pos[1] == 1) and (abs(start_pos[0] - end_pos[0]) == 1):  # Çapraz yeme
                        if end_pos in self.pieces and self.pieces[end_pos].name[0] == 'w':  # Sadece çaprazdaki beyaz taşları ye
                            self.pieces[end_pos] = self.pieces.pop(start_pos)
                            self.turn = not self.turn 

                # Beyaz piyonun hareketi ve çapraz yeme
                elif piece.name == "wp":
                    if (end_pos[1] - start_pos[1] == 1) and (abs(start_pos[0] - end_pos[0]) == 1):  # Çapraz yeme
                        if end_pos in self.pieces and self.pieces[end_pos].name[0] == 'b':  # Sadece çaprazdaki siyah taşları ye
                            self.pieces[end_pos] = self.pieces.pop(start_pos)
                            self.turn = not self.turn 
                
                elif (piece.name == "bR" or piece.name == "wR") and ((start_pos[0] - end_pos[0] == 0) or (start_pos[1] - end_pos[1] == 0)):
                    if self.is_path_clear(start_pos, end_pos):
                        self.taş_al(end_pos)
                        self.pieces[end_pos] = self.pieces.pop(start_pos)
                        self.turn = not self.turn 
                
                elif piece.name == "bN" or piece.name == "wN":
                    dx = abs(start_pos[0] - end_pos[0])
                    dy = abs(start_pos[1] - end_pos[1])
                    if (dx, dy) in [(1, 2), (2, 1)]:
                        self.taş_al(end_pos)
                        self.pieces[end_pos] = self.pieces.pop(start_pos)
                        self.turn = not self.turn 
                
                elif piece.name == "bB" or piece.name == "wB":
                    dx = abs(start_pos[0] - end_pos[0])
                    dy = abs(start_pos[1] - end_pos[1])
                    if dx == dy and self.is_path_clear(start_pos, end_pos):
                        self.taş_al(end_pos)
                        self.pieces[end_pos] = self.pieces.pop(start_pos)
                        self.turn = not self.turn 

                elif piece.name == "bQ" or piece.name == "wQ":
                    dx = abs(start_pos[0] - end_pos[0])
                    dy = abs(start_pos[1] - end_pos[1])
                    if (dx == dy or (start_pos[0] - end_pos[0] == 0) or (start_pos[1] - end_pos[1] == 0)):
                        if self.is_path_clear(start_pos, end_pos):
                            self.taş_al(end_pos)
                            self.pieces[end_pos] = self.pieces.pop(start_pos)
                            self.turn = not self.turn 

                elif piece.name == "bK" or piece.name == "wK":
                    dx = abs(start_pos[0] - end_pos[0])
                    dy = abs(start_pos[1] - end_pos[1])
                    if (dx, dy) in [(1, 1), (0, 1), (1, 0)]:
                        self.taş_al(end_pos)
                        self.pieces[end_pos] = self.pieces.pop(start_pos)
                        self.turn = not self.turn 

# Pygame başlatma ve ekran ayarlama
pg.init()
cols, rows = 8, 8
TILE = 100
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()

# Oyun nesnesi oluşturma
game = ChessGame(cols, rows, TILE)

# Oyun döngüsü
while True:
    sc.fill((0, 0, 0))

    # Olayları al
    events = pg.event.get()

    # Oyunu kapatma kontrolü
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Tahta ve taşları çiz
    game.draw(sc)
    
    # Fare tıklanmışsa pozisyonu al
    mouse_pos = game.get_click_mouse_pos(events)
    if event.type == pg.MOUSEBUTTONDOWN:
        if mouse_pos:
            if game.selected_piece is None and mouse_pos in game.pieces:  # Eğer bir taş seçilmemişse ve tıklanan pozisyonda taş varsa
                game.selected_piece = mouse_pos
                selected_piece_image = game.pieces[game.selected_piece].name
                game.hareketler(game.selected_piece, selected_piece_image)

            elif game.selected_piece is not None:  # Eğer bir taş seçilmişse
                game.move_piece(game.selected_piece, mouse_pos)
                game.selected_piece = None  # Seçimi sıfırla
            pg.display.flip()
    else:
        pg.display.flip()
        clock.tick(30)
