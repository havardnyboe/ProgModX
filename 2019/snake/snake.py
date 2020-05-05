import pygame, sys, random
pygame.init()

win_bredde = 500
win_hoyde = 500

win = pygame.display.set_mode((win_bredde, win_hoyde))
fps = pygame.time.Clock()
block = 10
score = 0
wall_pwrup_teller = 0

# Snake class #
class Snake():

    def __init__(self):
        self.posisjon = [100, 100]
        self.kropp = [[100, 100], [90, 100], [80, 100]]
        self.retning = "R"

    def bytt_retning(self, retning):
        if retning == "R" and not self.retning == "L":
            self.retning = "R"
        if retning == "L" and not self.retning == "R":
            self.retning = "L"
        if retning == "U" and not self.retning == "D":
            self.retning = "U"
        if retning == "D" and not self.retning == "U":
            self.retning = "D"
    
    def beveg(self, food_pos):
        if self.retning == "R":
            self.posisjon[0] += block
        if self.retning == "L":
            self.posisjon[0] -= block
        if self.retning == "U":
            self.posisjon[1] -= block
        if self.retning == "D":
            self.posisjon[1] += block
        self.kropp.insert(0,list(self.posisjon))
        if self.posisjon == food_pos:
            return 1
        if self.posisjon == superfood_pos:
            superfood.superfood_paa_skjerm = False
        else:
            self.kropp.pop()
            return 0

    def get_kropp(self):
        return self.kropp

    def sjekk_kollisjon(self):
        if wall_pwrup_teller == 0:
            if self.posisjon[0] > win_bredde - block or self.posisjon[0] < 0 or self.posisjon[1] > win_hoyde - block or self.posisjon[1] < 0:
                return True
            for i in self.get_kropp()[1:]:
                if self.posisjon == i:
                    return True
            return False
        if wall_pwrup_teller > 0:
            if self.posisjon[0] > win_bredde - block:
                self.posisjon[0] = 0
            if self.posisjon[0] < 0:
                self.posisjon[0] = win_bredde - block
            if self.posisjon[1] > win_hoyde - block:
                self.posisjon[1] = 0
            if self.posisjon[1] < 0:
                self.posisjon[1] = win_hoyde - block
                return False

class FoodSpawner():

    def __init__(self):
        self.posisjon = [random.randrange(block, win_bredde, block), random.randrange(block, win_hoyde, block)]
        self.food_paa_skjerm = True

    def spawn_food(self):
        if self.food_paa_skjerm == False:
            self.posisjon[0] = random.randrange(block, win_bredde, block)
            self.posisjon[1] = random.randrange(block, win_hoyde, block)
            self.food_paa_skjerm = True
        return self.posisjon

    def putt_food_paa_skjerm(self, boolean):
        self.food_paa_skjerm = boolean

class SuperFood():

    def __init__(self):
        self.posisjon = [random.randrange(block, win_bredde, block), random.randrange(block, win_hoyde, block)]
        self.superfood_paa_skjerm = True
    
    def spawn_superfood(self):
        if self.superfood_paa_skjerm == False:
            self.posisjon[0] = random.randrange(block, win_bredde, block)
            self.posisjon[1] = random.randrange(block, win_hoyde, block)
            self.superfood_paa_skjerm = True
        return self.posisjon

    def putt_superfood_paa_skjerm(self, boolean):
        self.superfood_paa_skjerm = boolean


snake = Snake()
food = FoodSpawner()
superfood = SuperFood()
food_pos = food.spawn_food()
superfood_pos = superfood.spawn_superfood()
fart = 15
fart_teller = 0

def game_over():
    pygame.quit()
    sys.exit()
print("Starter om 3 sekunder")
pygame.time.delay(3000)
while True:
    # Tittel #
    pygame.display.set_caption("Snake | Score {} | Fart {}".format(score, fart))
    # Event lytter #
    for event in pygame.event.get():
        # Avslutt spillen når du trykker på det røde krysset #
        if event.type == pygame.QUIT:
            game_over()
        # Beveg med piltastene #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.bytt_retning("R")
            if event.key == pygame.K_LEFT:
                snake.bytt_retning("L")
            if event.key == pygame.K_UP:
                snake.bytt_retning("U")
            if event.key == pygame.K_DOWN:
                snake.bytt_retning("D")
        
    # Spawn Food #
    food.spawn_food()
    # Spawn Wall Pwrup #
    superfood.spawn_superfood()
    # Fyll skjermen sort #
    win.fill(pygame.Color(0,0,0))
    # Tegn slangen #
    for pos in snake.get_kropp():
        pygame.draw.rect(win,pygame.Color(255,255,255),pygame.Rect(pos[0],pos[1],block,block))
    # Beveg slangen #
    if snake.beveg(food_pos) == 1:
        score+=1
        fart_teller += 1
        food.putt_food_paa_skjerm(False)
    if fart_teller % 5 == 0 and fart_teller != 0:
        fart +=1
        fart_teller = 0
    # Tegn maten #
    pygame.draw.rect(win, pygame.Color(255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], block, block))
    # Tegn Superfood #
    # pygame.draw.rect(win, pygame.Color(0, 255, 0), pygame.Rect(superfood_pos[0], superfood_pos[1], block, block))
    # Oppdater skjermen #
    pygame.display.flip()
    # Sjekk for kollisjon #
    if snake.sjekk_kollisjon():
        game_over()
    # Bestem hastigheten #
    fps.tick(fart)