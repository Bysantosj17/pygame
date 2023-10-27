import pygame, sys
pygame.init()

#Colores
black = (  0,  0,  0)
white = (255,255,255)
player_width = 15
player_height = 90

screen = pygame.display.set_mode((1000, 700))
Clock = pygame.time.Clock()

#Cordenadas y velicidad del player 1
#Cordenadas
player1_x_coor = 100
player1_y_coor = 300
#Velecidad
player1_y_speed = 0

#Cordenadas y velicidad del player 2
#Cordenadas
player2_x_coor = 900
player2_y_coor = 300
#Velecidad
player2_y_speed = 0

#Cordenadas de la pelota
pelota_x = 500
pelota_y = 350
#Velocidad de la pelota
pelota_speed_x = 3
pelota_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            #Player 1
            if event.key == pygame.K_w:
                player1_y_speed = -6
            if event.key == pygame.K_s:
                player1_y_speed = 6
            #Player 2
            if event.key == pygame.K_UP:
                player2_y_speed = -6
            if event.key == pygame.K_DOWN:
                player2_y_speed = 6
                
                
                
        if event.type == pygame.KEYUP:
            #Player 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #Player 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
                
                
                
                
    #Modifica las cordenadas para darle movimiento a los jugadores:
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed           
    
    screen.fill(black)
    #Zona de dibujo
    player_1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    player_2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))

    pelota_1 = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
    
    pygame.display.flip()
    Clock.tick(60)
pygame.quit()