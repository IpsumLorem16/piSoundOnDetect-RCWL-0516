import pygame, random

pygame.mixer.init()

boo = pygame.mixer.Sound('/home/admin/sounds/boo.wav')
witch = pygame.mixer.Sound('/home/admin/sounds/witch_1.wav')
witch2 = pygame.mixer.Sound('/home/admin/sounds/witch2.wav')
wolf = pygame.mixer.Sound('/home/admin/sounds/wolf.wav')
snarl = pygame.mixer.Sound('/home/admin/sounds/snarl.wav')
zombie = pygame.mixer.Sound('/home/admin/sounds/zombie.wav')
monster1 = pygame.mixer.Sound('/home/admin/sounds/monster-roar.wav')

sounds = [boo, witch, witch2, wolf, snarl, monster1, zombie]

channel1 = pygame.mixer.Channel(1)

#Play random sound till finished.
def playRandomSound():
  channel1.play(random.choice(sounds))
  while channel1.get_busy():
    pygame.time.wait(100)
