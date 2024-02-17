from tkinter import *
from PIL import ImageTk, Image
import subprocess
import os

root = Tk()
root.title("Pybox")
root.iconbitmap('pygame_icon.ico')

# Initialize images for each game
snake_img = ImageTk.PhotoImage(Image.open('snake_game/snake_img.jpg').resize((720, 600), Image.LANCZOS))
flappy_img = ImageTk.PhotoImage(Image.open('flappy_game/gallery/sprites/flappybird.jpg').resize((720, 600), Image.LANCZOS))
ticktaktoe_img = ImageTk.PhotoImage(Image.open('tiktaktoe_image.jpg').resize((720, 600), Image.LANCZOS))
memory_img = ImageTk.PhotoImage(Image.open('memory_game_image.jpg').resize((720, 600), Image.LANCZOS))

# Create a list of all resized images
image_list = [snake_img, flappy_img, ticktaktoe_img, memory_img]

# Creating status bar
status = Label(root, text="Game 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

# Creating a list of all games
game_list = ['snake_game/snakenew.py', 'flappy_game/main.py', 'ticktaktoe_game.py', 'memory_game.py']

# Displaying the first game image
label_img = Label(image=snake_img)
label_img.grid(row=0, column=0, columnspan=3)

# Creating functions for the program
def forward(image_number):
    global label_img
    global forward_button
    global back_button

    label_img.grid_forget()
    label_img = Label(image=image_list[image_number - 1])

    forward_button = Button(root, text=">>", command=lambda: forward(image_number + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_number - 1))
    play_button = Button(root, text="Play", command=lambda: play(image_number))
    status.config(text="Game " + str(image_number) + " of " + str(len(image_list)))

    if image_number == len(image_list):
        forward_button = Button(root, text=">>", state=DISABLED)

    label_img.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    play_button.grid(row=1, column=1)
    forward_button.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

def back(image_number):
    global label_img
    global forward_button
    global back_button

    label_img.grid_forget()
    label_img = Label(image=image_list[image_number - 1])

    forward_button = Button(root, text=">>", command=lambda: forward(image_number + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_number - 1))
    play_button = Button(root, text="Play", command=lambda: play(image_number))
    status.config(text="Game " + str(image_number) + " of " + str(len(image_list)))

    if image_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    label_img.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    play_button.grid(row=1, column=1)
    forward_button.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

def play(image_number):
    if image_number==1:
            try:
                # Specify the path to the main folder
                main_directory = os.path.dirname(os.path.realpath("snake_game"))

                # Specify the path to the snake_game directory
                game_directory = os.path.join(main_directory, 'snake_game')

                # Change the working directory to the snake_game directory
                os.chdir(game_directory)

                # Execute the Python script using subprocess
                subprocess.call(["python", "snakenew.py"])

                # Change back to the original directory
                os.chdir(main_directory)

            except Exception as e:
                print(f"Error during subprocess call: {e}")

    subprocess.call(["python", game_list[image_number - 1]])
    
    if image_number==2:
            try:
                # Specify the path to the main folder
                main_directory = os.path.dirname(os.path.realpath("flappy_game"))

                # Specify the path to the snake_game directory
                game_directory = os.path.join(main_directory, 'flappy_game')

                # Change the working directory to the snake_game directory
                os.chdir(game_directory)

                # Execute the Python script using subprocess
                subprocess.call(["python", "main.py"])

                # Change back to the original directory
                os.chdir(main_directory)

            except Exception as e:
                print(f"Error during subprocess call: {e}")

    subprocess.call(["python", game_list[image_number - 1]])


# 

# Creating buttons
forward_button = Button(root, text=">>", command=lambda: forward(2))
back_button = Button(root, text="<<", command=lambda: back(1), state=DISABLED)
play_button = Button(root, text="Play", command=lambda: play(1))

# Placing buttons on display
back_button.grid(row=1, column=0)
play_button.grid(row=1, column=1, pady=10)
forward_button.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

root.mainloop()
