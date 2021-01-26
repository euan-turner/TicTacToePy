from dataclasses import dataclass
import pygame

##Token is a pre-drawn surface with a nought or cross
##val is 1 or -1, it also doubles as side from v1

@dataclass
class Player:
    name : str
    token : pygame.Surface
    val : int
    text_colour : (int,int,int)
    score : int = 0
