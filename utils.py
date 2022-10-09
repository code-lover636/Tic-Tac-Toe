import pygame, sys

class Game:
    
    board = [
                [2, 3, 4],
                [5, 6, 7],
                [8, 9, 5],
            ]
    
    
    def __init__(self,screen, WIDTH, HEIGHT):
        self.screen = screen
        self.width, self.height =  WIDTH, HEIGHT
        self.BG = pygame.image.load('assets/background.png')
        self.CROSS = pygame.image.load('assets/cross.png')
        self.CIRCLE = pygame.image.load('assets/ellipse.png')
        self.STRIKE = pygame.image.load('assets/strike.png')
        self.tiles = {1:(55,55),2:(220,55),3:(385,55),4:(55,215),5:(220,215),6:(385,215),7:(55,385),8:(220,385),9:(385,385)}
        self.tile = 0
        self.mode = "playing"
        self.player = self.CROSS
        self.chkdtiles = dict()
        self.font = pygame.font.Font('freesansbold.ttf', 17)
        self.turn = self.font.render(f'Next turn: X', True, (255,0,0))
        self.winner = self.font.render("", True, (255,0,0))
        
        
    def draw_screen(self):
        self.screen.blit(self.BG, (0, 0))
        self.screen.blit(self.turn, (10, 497))
        self.screen.blit(self.winner, (400, 497))
        for tile,player in self.chkdtiles.items():  self.screen.blit(player,self.tiles[tile])
        
        if self.mode=="gameover":
            self.screen.blit(self.STRIKE,self.strikepos)
    
    
    def strike(self,orientation):
        if   orientation=="horizontal":
            if   1<=self.tile<=3: pos=(55,85)
            elif 4<=self.tile<=6: pos=(55,245)
            elif 7<=self.tile<=9: pos=(55,415)
        elif orientation=="vertical":
            self.STRIKE = pygame.transform.rotozoom(self.STRIKE,90,1)
            if   self.tile in (1,4,7): pos=(90,50)
            elif self.tile in (2,5,8): pos=(255,50)
            elif self.tile in (3,6,9): pos=(420,50)
        elif orientation=="Ldiagonal": 
            self.STRIKE = pygame.transform.scale(self.STRIKE, (470, 10))
            self.STRIKE = pygame.transform.rotozoom(self.STRIKE,360-45,1)
            pos=(85,90)
        elif orientation=="Rdiagonal": 
            self.STRIKE = pygame.transform.scale(self.STRIKE, (470, 10))
            self.STRIKE = pygame.transform.rotozoom(self.STRIKE,45,1)
            pos=(85,85)
        return pos
    
    
    def play(self,tile,player):
        player = 0 if player==self.CIRCLE else 1
        if   1<=tile<=3:    self.board[0][tile-1] = player
        elif 4<=tile<=6:    self.board[1][tile-4] = player
        elif 7<=tile<=9:    self.board[2][tile-7] = player
    
        if   self.board[0][0]==self.board[1][1]==self.board[2][2]: self.mode = "gameover"; self.strikepos = self.strike("Ldiagonal")
        elif self.board[0][2]==self.board[1][1]==self.board[2][0]: self.mode = "gameover"; self.strikepos = self.strike("Rdiagonal")
        else:
            for row in self.board:
                if row[0]==row[1]==row[2]: 
                    self.mode = "gameover"
                    self.strikepos = self.strike("horizontal")
                    
            for col in range(3):
                if self.board[0][col]==self.board[1][col]==self.board[2][col]: 
                    self.mode = "gameover"
                    self.strikepos = self.strike("vertical")
        
        if self.mode == "gameover":
            if player == 0: self.winner = self.font.render(f'Winner: O', True, (255,0,0))
            if player == 1: self.winner = self.font.render(f'Winner: X', True, (255,0,0))          
            
                  
    def trackpos(self, pos):
        if   0<pos[1]<157:
            if   0<pos[0]<167  :  self.tile = 1
            elif 177<pos[0]<333:  self.tile = 2
            elif 343<pos[0]<500:  self.tile = 3
            
        elif 167<pos[1]<323:
            if   0<pos[0]<167  :   self.tile = 4
            elif 177<pos[0]<333:   self.tile = 5
            elif 343<pos[0]<500:   self.tile = 6
            
        elif 333<pos[1]<500:
            if   0<pos[0]<167  :   self.tile = 7
            elif 177<pos[0]<333:   self.tile = 8
            elif 343<pos[0]<500:   self.tile = 9
                
        if self.tile not in self.chkdtiles and self.tile != 0 and self.mode=="playing":
            self.chkdtiles.update({self.tile: self.player})
            self.play(self.tile,self.player)
            
            if self.player == self.CIRCLE:
                self.player = self.CROSS
                self.turn = self.font.render(f'Next turn: X', True, (255,0,0))
            else:
                self.turn = self.font.render(f'Next turn: O', True, (255,0,0))
                self.player = self.CIRCLE
                