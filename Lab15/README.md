**CMSI 1010** Computer Programming & Laboratory, Fall 2023

# Lab 15 - Pygame
**Due 11:59pm PT 11/21**


Creating games through programming is both rewarding and educational. Game development involves logic, math, physics, AI, and more, all converging to form enjoyable experiences. In this lab, you will learn the basics of how PyGame works and get a basic implementation working. 


## Part One: Downloading and Installing Pygame

Pygame is a popular library for creating 2D games using Python. Follow these steps to download and install Pygame on your computer:


### Step 1: Open a Terminal or Command Prompt

On Windows, search for "Command Prompt" or press Win + R and type cmd then press Enter. On macOS, search for "Terminal" in Spotlight or find it in the Applications > Utilities folder.

### Step 2: Install Pygame

In the terminal or command prompt, type the following command and press Enter to install Pygame using pip (Python's package manager):

```
pip install pygame

```
### Step 3: Verify Installation

After the installation is complete, you can verify if Pygame has been installed successfully. In the terminal or command prompt, type the following Python code and press Enter:

```
import pygame
print(pygame.ver)
```

If Pygame is installed properly, it will display the version number of the installed Pygame library.

Congratulations! You have successfully downloaded and installed Pygame. Have fun with the next part of this lab!

Remember to refer to the official Pygame documentation (https://www.pygame.org/docs/) for detailed information on how to use Pygame's features and functions in your game projects.

## Part Two: A bit Racey!

In this part of the lab, we will create a basic "Racey" game using Pygame, where you control a car that moves horizontally to avoid obstacles. Let's get started!

### Step 1: Set Up Your Environment

Make sure you have Pygame installed. If not, follow the steps from the previous Part to install it.

### Step 2: Create the Game Window

Import the Pygame library and other necessary libraries and initialize it:

```
import pygame
import random
import time

pygame.init()
```
Then set up the display window:

```
display_width, display_height = 800, 600
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
```

### Step 3: Define the Car and Obstacles

Load the car image (you can find these images in the same directory or you can find other images to use online).

```
carImg = pygame.image.load('racecar.png')
```

Then initialize car and obstacle positions:

```
car_x = display_width  * 0.45
car_y = display_height * 0.8

obstacle_startx = random.randrange(0,display_width)
obstacle_starty = -600
```

### Step 4: Main Game Loop

Create a game loop to keep the game running

```
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)
```

### Step 5: Run the Game

Make sure you have the car image in the same directory as your code.

Run the code, and you should see the game window with a car and an obstacle moving down the screen.

### Step 6: Enhance the Game

Follow the TODO comments in racey.py to display the score (i.e., the number of obstacles dodged) and a crash screen. You may optionally implement multiple difficulty levels.

From here, you can enhance the game by adding customized colors and designs for the car and the obstacles, multiple obstacles, other background music, and more. Experiment and have fun exploring different ways to make your "Racey" game even more engaging!
