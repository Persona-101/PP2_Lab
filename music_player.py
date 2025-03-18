import pygame
import os


pygame.init()
pygame.mixer.init()


playlist = ["Wii.mp3", "Sonic.mp3", "Pokemon.mp3"]  
current_song_index = 0  


pygame.mixer.music.load(playlist[current_song_index])
pygame.mixer.music.play()


screen = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Pygame Music Player")


font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (x, y))

def play_song(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()


running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen
    draw_text(f"Now Playing: {os.path.basename(playlist[current_song_index])}", 50, 100)
    draw_text("Press P = Pause | R = Resume | N = Next | B = Previous", 50, 200)
    
    pygame.display.update()  # Refresh screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                pygame.mixer.music.pause()
            elif event.key == pygame.K_r:  
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_n:  
                current_song_index = (current_song_index + 1) % len(playlist)
                play_song(current_song_index)
            elif event.key == pygame.K_b:  
                current_song_index = (current_song_index - 1) % len(playlist)
                play_song(current_song_index)

pygame.quit()
