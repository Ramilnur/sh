from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 36)
win = font1.render('You WIN!', True, (255, 255, 255))
lose = font1.render('You LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg') 

n0 = ['Ya balbes', 'ty tupoi oi', 'hahaahhahah', 'spaaaaaaaaaaaaam', 'agent007', 'higsos', 'sharavozz', 'igoooor', 'chel ty...', 'auffff']

n = randint(0, 9)
n1 = n0[n]
n = randint(0, 9)
n2 = n0[n]
n = randint(0, 9)
n3 = n0[n]
n = randint(0, 9)
n4 = n0[n]
n = randint(0, 9)
n5 = n0[n]
n = randint(0, 9)
n6 = n0[n]
n = randint(0, 9)
n7 = n0[n]
n= randint(0, 9)
n9 = n0[n]
n= randint(0, 9)
n10 = n0[n]

ochko1 = randint(1, 25)
ochko2 = randint(25, 40)
ochko3 = randint(40, 55)
ochko4 = randint(55, 75)
ochko5 = randint(75, 100)

img_3 = 'rock.png'
img_2 = 'bull.png'
img_back = 'galaxy.jpg'
img_hero = 'rocket.png'
img_mon = 'ufo.png'
img_atr = 'asteroid.png'
img_bullet = 'bullet.png'

lvl = 0
score = 0
lost = 0
goal = 100
max_lost = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_2, self.rect.centerx, self.rect.top, 50, 50, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()  

class Mon(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

win_width = 700
win_height = 500
display.set_caption('shooter')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
ship1 = Player1(img_3, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
astr = sprite.Group()
if lost < 5:
    for i in range(1, 6):
        monster = Enemy(img_mon, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
        atr = Mon(img_atr, randint(80, win_width - 80), -40, 80, 80, randint(1, 5))
        monsters.add(monster)
        astr.add(atr)

bullets = sprite.Group()

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship1.fire()
            elif e.key == K_UP:
                fire_sound.play()
                ship.fire()

    if not finish:
        window.blit(background,(0, 0))

        text = font1.render('Счет: ' + str(score), 1, (255, 225, 255))
        window.blit(text, (10, 20))

        text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        table = font1.render(n1 + ' 1 ' + str(ochko5), 1, (255, 255, 255))
        window.blit(table, (500, 200))

        table1 = font1.render(n2 + ' 2 ' + str(ochko4), 1, (255, 255, 255))
        window.blit(table1, (500, 250))

        tabl2e = font1.render(n3 + ' 3 ' + str(ochko3), 1, (255, 255, 255))
        window.blit(tabl2e, (500, 300))
 
        tabl3e = font1.render(n4 + ' 4 ' + str(ochko2), 1, (255, 255, 255))
        window.blit(tabl3e, (500, 350))

        table4 = font1.render(n5 + ' 5 ' + str(ochko1), 1, (255, 255, 255))
        window.blit(table4, (500, 400))

        ship.update()
        ship1.update()
        monsters.update()
        astr.update()

        ship.reset()
        ship1.reset()
        monsters.draw(window)
        astr.draw(window)
        bullets.update()
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        collides = sprite.groupcollide(astr, bullets, True, False)
        for c in collides:
            score = score + 1
            monster = Enemy(img_mon, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            atr = Mon(img_atr, randint(80, win_width - 80), -40, 80, 80, randint(1, 5))
            monsters.add(monster)
            astr.add(atr)  
            
        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship1, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

        if score == goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()

    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()

        n = randint(0, 9)
        n1 = n0[n]
        n = randint(0, 9)
        n2 = n0[n]
        n = randint(0, 9)
        n3 = n0[n]
        n = randint(0, 9)
        n4 = n0[n]
        n = randint(0, 9)
        n5 = n0[n]
        n = randint(0, 9)
        n6 = n0[n]
        n = randint(0, 9)
        n7 = n0[n]
        n= randint(0, 9)
        n9 = n0[n]
        n= randint(0, 9)
        n10 = n0[n]

        time.delay(3000)
        for i in range(1, 6):
            monster = Enemy(img_mon, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)    

    time.delay(50)