import pygame

class Player():
    def __init__(self, x, y, img):
        self.flip = False
        self.image = self.image = pygame.transform.scale(img, (80, 180))
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_cooldown = 0
        self.attack_type = 0
        self.health = 100

    def move(self, screen_width, screen_height, surface, target, is_player_1):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Handle attack cooldown timer
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attacking = False

        #get key presses
        key = pygame.key.get_pressed()

        #other actions can only be done when not attacking
        if self.attacking == False:
            if is_player_1:
            #movement for player 1
                if key[pygame.K_a]:
                    dx = -SPEED
                if key[pygame.K_d]:
                    dx = SPEED

                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                #attack
                if (key[pygame.K_r] or key[pygame.K_t]) and self.attack_cooldown == 0:
                    self.attack(surface, target)
                    # check attack type
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
            else:
            #movement for player 2
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                
                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                    
                #attack
                if (key[pygame.K_p] or key[pygame.K_o]) and self.attack_cooldown == 0:
                    self.attack(surface, target)
                    # check attack type
                    if key[pygame.K_p]:
                        self.attack_type = 1
                    if key[pygame.K_o]:
                        self.attack_type = 2

        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #make player stay on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        # Ground collision
        if self.rect.bottom + dy > screen_height - 60:
            self.vel_y = 0
            self.jump = False
            dy = (screen_height - 60) - self.rect.bottom

        #make sure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        self.attack_cooldown = 30
        if self.flip:
            # looking left
            attacking_rect = pygame.Rect(self.rect.centerx - self.rect.width - 50, self.rect.y, self.rect.width + 50, self.rect.height)
        else:
            # looking right
            attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width + 50, self.rect.height)

        if attacking_rect.colliderect(target.rect):
            target.health -= 10
            if target.health < 0:
                target.health = 0
            


    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x, self.rect.y))