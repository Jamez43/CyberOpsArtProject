import pygame
import random
import math

class circle:
    pygame.mixer.init()
    pygame.mixer.set_num_channels(100)
    collision_sound = pygame.mixer.Sound("audiomass-output.wav")
    balls = []
    colors = ["red", "orange", "yellow" ,"green", "blue", "purple", "pink"]
    
    def get_random_color():
        return circle.colors[random.randint(0,6)]
    def __init__(self, screen: pygame.Surface, color: pygame.Color, center: tuple[int, int], radius: int, speed: int):
        self.screen = screen
        self.color = color
        self.center = center
        self.radius = radius
        self.speed = speed
        self.dy = random.uniform(-1,1)
        self.dx = random.uniform(-1,1)
        self.vx = self.dx * self.speed
        self.vy = self.dy * self.speed       
        self.count = 0 

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)
        
    
    def move(self):
        if self.check_y_collision():
            circle.collision_sound.play()
            self.vy *= -1
            self.center = (self.center[0], self.center[1] + self.vy)
        elif self.check_x_collision():
            circle.collision_sound.play()
            self.vx *= -1
            self.center = (self.center[0] + self.vx, self.center[1])
        else:
            self.center = (self.center[0] + self.vx, self.center[1] + self.vy)
            
        self.check_ball_collision()
        self.stuck()
    
    
    def check_y_collision(self):
        if self.center[1] - self.radius <= 0 or self.center[1] + self.radius >= self.screen.get_height():
            return True
        
    def check_x_collision(self):
        if self.center[0] - self.radius <= 0 or self.center[0] + self.radius >= self.screen.get_width():
            return True
    
    def check_ball_collision(self):
        for ball in circle.balls.copy():
            if ball is not self:
                dx = self.center[0] - ball.get_center()[0]
                dy = self.center[1] - ball.get_center()[1]
                distance = (dx**2 + dy**2)**0.5
                angle = math.atan2(dy, dx)
                if distance <= self.radius + ball.get_radius():
                    circle.collision_sound.play()
                    self.vx = self.speed * math.cos(angle)
                    self.vy = self.speed * math.sin(angle)
                    ball.vx = ball.speed * math.cos(angle + math.pi)
                    ball.vy = ball.speed * math.sin(angle + math.pi)
                    self.count += 1
                    ball.count += 1
                    
                    if self.count >= 8:
                        
                        
                        # Calculate the minimum and maximum x and y coordinates for the new balls
                        min_x = self.radius
                        max_x = self.screen.get_width() - self.radius
                        min_y = self.radius
                        max_y = self.screen.get_height() - self.radius
                        
                        
                        new_pos1 = (self.center[0] - self.radius//1.5, self.center[1] - self.radius//1.5)
                        new_pos2 = (self.center[0] + self.radius//1.5, self.center[1] + self.radius//1.5)
                        
                        new_pos1 = max(min_x, min(max_x, new_pos1[0])), max(min_y, min(max_y, new_pos1[1]))
                        new_pos2 = max(min_x, min(max_x, new_pos2[0])), max(min_y, min(max_y, new_pos2[1]))
                        
                        new_ball1 = circle(self.screen, circle.get_random_color(),new_pos1 , self.radius //1.5, self.speed)  
                        new_ball2 = circle(self.screen, circle.get_random_color(), new_pos2, self.radius//1.5, self.speed)

                        # Ensure the new balls are created within these bounds
                        
                        ball_pos1 = (ball.center[0] - ball.radius//1.5, ball.center[1] - ball.radius//1.5)
                        ball_pos2 = (ball.center[0] + ball.radius//1.5, ball.center[1] + ball.radius//1.5)
                        
                        ball_pos1 = max(min_x, min(max_x, ball_pos1[0])), max(min_y, min(max_y, ball_pos1[1]))
                        ball_pos2 = max(min_x, min(max_x, ball_pos2[0])), max(min_y, min(max_y, ball_pos2[1]))

                        ball_ball1 = circle(ball.screen, circle.get_random_color(), ball_pos1, ball.radius //1.5, ball.speed)  
                        ball_ball2 = circle(ball.screen, circle.get_random_color(), ball_pos2, ball.radius//1.5, ball.speed)
                        ball_ball1 = circle(ball.screen, circle.get_random_color(), ball_pos1, ball.radius //1.5, ball.speed)  
                        ball_ball2 = circle(ball.screen, circle.get_random_color(), ball_pos2, ball.radius//1.5, ball.speed)
                        circle.balls.append(new_ball1)
                        circle.balls.append(new_ball2)
                        circle.balls.append(ball_ball1)
                        circle.balls.append(ball_ball2)
                        circle.balls.remove(self)   
                        circle.balls.remove(ball)  
                        break               
    
    def stuck(self):
        if self.center[1] - self.radius <= 0 or self.center[1] + self.radius >= self.screen.get_height():
            self.center = (self.center[0], self.center[1] + self.vy)
        elif self.center[0] - self.radius <= 0 or self.center[0] + self.radius >= self.screen.get_width():
            self.center = (self.center[0] + self.vx, self.center[1])

    
    def get_screen(self) -> pygame.Surface:
        return self.screen

    def set_screen(self, screen: pygame.Surface):
        self.screen = screen

    def get_color(self) -> pygame.Color:
        return self.color

    def set_color(self, color: pygame.Color):
        self.color = color

    def get_center(self) -> tuple[int, int]:
        return self.center

    def set_center(self, center: tuple[int, int]):
        self.center = center

    def get_radius(self) -> int:
        return self.radius

    def set_radius(self, radius: int):
        self.radius = radius