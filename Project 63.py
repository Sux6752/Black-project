# import pygame module in this program 
import pygame

colour = [[255, 0, 0], [255, 69, 0], [255, 165, 0], [255, 215, 0], [255, 255, 0], [173, 255, 47], [0, 255, 0], [0, 128, 128], [0, 191, 255], [123, 104, 238], [128, 0, 128], [148, 0, 211]]
  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()
  
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode((1200, 600))
  
# set the pygame window name 
pygame.display.set_caption("Проект <<pygame>>")
  
# object current co-ordinates

x_rs = 0
y_rs = 0

x_r = 550
y_r = 550

x_p = 625
y_p = 500
  
move = x_rs
d = 1
# dimensions of the object 
width = 150
height = 20

variable = 0
  
# velocity / speed of movement
vel = 10
# V = 3
V_y_p = 3
V_x_p = 3
V_x_x_p = (V_y_p, V_x_p)
  
# Indicates pygame is running
run = True
blocks = []
for i in range(12):
    blocks.append([])
    for j in range(45):
        blocks[i].append(pygame.Rect(move, y_rs, 25,25))
        move += 28
    move = 0
    y_rs += 27
print(blocks[0][0], blocks[1][0], blocks[2][0])

# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(15)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x_r>50:
          
        # decrement in x co-ordinate
        x_r -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x_r<1150-width:
          
        # increment in x co-ordinate
        x_r += vel
         
    # if left arrow key is pressed   
#     if keys[pygame.K_UP] and y>0:
#           
#         # decrement in y co-ordinate
#         y -= vel
#           
#     # if left arrow key is pressed   
#     if keys[pygame.K_DOWN] and y<500-height:
#         # increment in y co-ordinate
#         y += vel
         
              
    # completely fill the surface object  
    # with black colour  
    win.fill((0, 0, 0))
      
    # drawing object on screen which is rectangle here 
    rect = pygame.draw.rect(win, (255, 255, 255), (x_r, y_r, width, height))
    point = pygame.draw.rect(win, (255, 255, 255), (x_p, y_p, 7,7))
    move = x_rs
    d = 1
    for i in range(12):
        for j in range(len(blocks[i])):
            pygame.draw.rect(win, colour[i], blocks[i][j])
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[0]), (move, 0, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[1]), (move, 27, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[2]), (move, 54, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[3]), (move, 81, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[4]), (move, 108, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[5]), (move, 135, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[6]), (move, 162, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[7]), (move, 189, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[8]), (move, 216, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[9]), (move, 243, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[10]), (move, 270, 25,25)))
#         move+=27 + d
#     move = x_rs
#     for i in range (1, 46):
#         blocks.append(pygame.draw.rect(win, (colour[11]), (move, 296, 25,25)))
#         move+=27 + d  
    if rect.colliderect(point):
        V_x_p=-V_x_p
        V_y_p=-V_y_p
    for n in range(12):
        for m in blocks[n]:
            if m.colliderect(point):
                if x_p < m.center[0]:
                    V_x_p = -V_x_p
                if y_p > m.center[1]:
                    V_y_p = -V_y_p
                blocks[n].remove(m)
    if rect.colliderect(point):
        if x_p < rect.center[0]:
            V_x_p = -V_x_p
        if y_p > rect.center[1]:
            V_y_p = -V_y_p
        variable+=1
    y_p -= V_y_p;
    x_p -= 2 * V_x_p;
    if y_p < 0:
        V_y_p = -V_y_p;
    if x_p < 0 or x_p > 1200:
        V_x_p = -V_x_p
    
    if x_p < rect.center[0] and rect.colliderect(point):
        V_x_p = V_x_p
    if x_p > rect.center[1] and rect.colliderect(point):
        V_y_p = V_y_p
        
    if y_p > 600:
        pygame.init()
        sc = pygame.display.set_mode((1200, 600))
        sc.fill((0, 0, 0))
 
        font = pygame.font.Font(None, 72)
        text = font.render('''You're died. Please press space''', True, (150, 0, 0))
        place = text.get_rect(
            center=(600, 150))
        sc.blit(text, place)
 
        pygame.display.update()
 
#         while 1:
#             for i in pygame.event.get():
#                 if i.type == pygame.QUIT:
#                     sys.exit()
        
        pressed = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = False
            
#         elif pressed[pygame.K_RIGHT]:
#             place.x += 1
 
        sc.fill((200, 255, 200))
        sc.blit(text, place)


    
      
    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()