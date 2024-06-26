import pygame as pg 
import pymunk.pygame_util 
from random import*

def create_square(space,pos): 
    square_mass, square_size=1,[randrange(50,100)for i in range(2)] 
    square_moment=pymunk.moment_for_box(square_mass,square_size) 
    square_body=pymunk.Body(square_mass,square_moment) 
    square_body.position=pos 
    square_shape=pymunk.Poly.create_box(square_body,square_size)
    square_shape.elasticity=0.8 
    square_shape.friction=1.0 
    square_shape.color=[randrange(256) for i in range(4)]
    space.add(square_body,square_shape)
pymunk.pygame_util.positive_y_is_up=False 
RES=WIDTH, HEIGHT=900,500
FPS=60 
pg.init()
surface=pg.display.set_mode(RES) 
clock=pg.time.Clock() 
draw_options=pymunk.pygame_util.DrawOptions(surface) 
space=pymunk.Space() 
space.gravity=0,8000
segment_shape=pymunk.Segment(space.static_body,(1, HEIGHT),(WIDTH,HEIGHT),26) 
space.add(segment_shape) 
segment_shape.elasticity=1.5
segment_shape.friction=0
segment_shape2=pymunk.Segment(space.static_body,(1, HEIGHT),(0,0),26) 
space.add(segment_shape2) 
segment_shape2.elasticity=1.2
segment_shape2.friction=1.0
segment_shape3=pymunk.Segment(space.static_body,(900, HEIGHT),(900,0),26) 
space.add(segment_shape3) 
segment_shape3.elasticity=1.2
segment_shape3.friction=1.0
segment_shape4=pymunk.Segment(space.static_body,(0,0),(40000,500),26) 
space.add(segment_shape4) 
segment_shape4.elasticity=1.2
segment_shape4.friction=1.0
while True:
    surface.fill(pg.Color('black')) 
    for i in pg.event.get(): 
        if i.type==pg.QUIT: 
            exit() 
        if i.type==pg.MOUSEBUTTONDOWN: 
            if i.button==1:
                create_square(space,i.pos)
                print(i.pos)
    space.step(1/FPS) 
    space.debug_draw(draw_options)
    pg.display.flip() 
    clock.tick(FPS)  