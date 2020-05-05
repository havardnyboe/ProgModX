import pygame, sys, random 
from tkinter import* 
from tkinter import messagebox

# SNAKE CLASS #
class Snake():

    win_width = 400
    win_hight = 400

    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"

    # CHANGE DIRECTION #
    def change_dir_to(self,dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    # MOVE #
    def move(self,food_pos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0,list(self.position))
        if self.position == food_pos:
            return 1
        else:
            self.body.pop()
            return 0
            
    # CHECK FOR COLLISION #
    def check_collision(self):
        if self.position[0] > Snake.win_width-10 or self.position[0] < 0:
            return 1
        if self.position[1] > Snake.win_hight-10 or self.position[1] < 0:
            return 1
        for body_part in self.body[1:]:
            if self.position == body_part:
                return 1
        return 0

    def get_head_pos(self):
        return self.position

    def get_body(self):
        return self.body

# FOOD CLASS #
class FoodSpawner():

    def __init__(self):
        self.position = [random.randrange(1,Snake.win_width/10)*10,random.randrange(1,Snake.win_hight/10)*10]
        self.is_food_on_screen = True
    def spawn_food(self):
        if self.is_food_on_screen == False:
            self.position = [random.randrange(1,Snake.win_width/10)*10,random.randrange(1,Snake.win_hight/10)*10]
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self,b):
        self.is_food_on_screen = b

pygame.init()

win = pygame.display.set_mode((Snake.win_width,Snake.win_hight))
fps = pygame.time.Clock()
tick = 15
score = 0

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo('Hvordan spille', 'Bruk piltastene eller wasd til å bevege slangen.\nUngå å krasje i kanten av banen og kroppen til slangen. \nSpis epler for å gjøre slangen større.')
window.deiconify()
window.destroy()
window.quit()

snake = Snake()
foodSpawner = FoodSpawner()

def game_over():
    messagebox.showinfo('GAME OVER', 'Score: {}'.format(score))
    window.deiconify()
    window.destroy()
    window.quit()
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake.change_dir_to("RIGHT")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake.change_dir_to("LEFT")
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake.change_dir_to("UP")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake.change_dir_to("DOWN")
            if event.key == pygame.K_x:
                tick+=1
            if event.key == pygame.K_z:
                tick-=1
            if event.key == pygame.K_i:
                snake.body.insert(0,list(snake.position))
                score+=1
            if event.key == pygame.K_o:
                snake.body.pop()
                score-=1
    food_pos = foodSpawner.spawn_food()
    if snake.move(food_pos)==1:
        score+=1
        foodSpawner.set_food_on_screen(False)

    win.fill(pygame.Color(0,0,0))
    for pos in snake.get_body():
        pygame.draw.rect(win,pygame.Color(255,255,255),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(win,pygame.Color(255,0,0),pygame.Rect(food_pos[0],food_pos[1],10,10))
    if snake.check_collision()==1:
        game_over()
    pygame.display.set_caption("Snake | Score: {} | FPS: {}".format(score, tick))
    pygame.display.flip()
    fps.tick(tick)