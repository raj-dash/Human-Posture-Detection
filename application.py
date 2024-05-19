from customtkinter import *
from pyglet import font
# import master as m

# variables
HEIGHT = 800
WIDTH = 800
FRAME_WIDTH = 750
FRAME_HEIGHT = 400
TEXT_FRAME_HEIGHT = 300
LIGHT_BLUE = "#C6DEF2"
BLUE = "#92BEE3"
DARK_BLUE = "#6AABD2"
font.add_file("Fonts/Bebas_Neue/BebasNeue-Regular.ttf")

desc_text = """Master Yoga Poses: Get real-time feedback on your yoga form to ensure proper alignment and maximize your practice.
Maintain Perfect Posture: Our AI monitors your posture throughout the day, helping you stay upright and avoid slouching.
Level Up Your Gym Workouts: See your gym exercises graded in real-time, ensuring you perform them safely and effectively with proper form."""

# setting up the window

set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk(fg_color=BLUE)
app.geometry(f"{WIDTH}x{HEIGHT}")

# setting up the font
headerFont = CTkFont(family="Bebas Neue", size=50, weight="bold")
descFont = CTkFont(family="Bebas Neue", size=20)

# setting up the frame

textFrame = CTkFrame(master=app, width=FRAME_WIDTH, height=TEXT_FRAME_HEIGHT, fg_color=DARK_BLUE)
textFrame.pack(expand=True)
textFrame.place(relx=0.5, rely=0.225, anchor=CENTER)

btnFrame = CTkFrame(master=app, width=FRAME_WIDTH, height=FRAME_HEIGHT, fg_color=LIGHT_BLUE)
btnFrame.pack(expand=True)
btnFrame.place(relx=0.5, rely=0.7, anchor=CENTER)
# functions

def button_clicked(num):
    print(f"Button {num} clicked")


# adding the labels
heading = CTkLabel(master=textFrame, text="Human Posture Detection", font=headerFont)
heading.place(relx=0.5, rely=0.2, anchor=CENTER)

desc = CTkLabel(master=textFrame, text=desc_text, wraplength=600, font=descFont)
desc.place(relx=0.5, rely=0.6, anchor=CENTER)


# adding the buttons
button1 = CTkButton(master=btnFrame, text="Posture Detection", command=lambda: button_clicked(1))
button1.place(relx=0.5, rely=0.5, anchor=CENTER)

button2 = CTkButton(master=btnFrame, text="Yoga Pose Detection", command=lambda: button_clicked(2))
button2.place(relx=0.25, rely=0.5, anchor=CENTER)

button3 = CTkButton(master=btnFrame, text="Gym Pose Detection", command=lambda: button_clicked(3))
button3.place(relx=0.75, rely=0.5, anchor=CENTER)

if __name__ == "__main__":
    app.mainloop()