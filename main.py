import pandas as pd
import turtle

FONT = ("Bold", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

states_df = pd.read_csv("50_states.csv")

states = states_df['state']

guessed = set()

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        new_data = pd.DataFrame(set(states) - guessed)
        new_data.to_csv('missed_states.csv')
        break
    for state in states:
        if answer_state == state:
            guessed.add(state)
            x = float(states_df[states_df.state == state]['x'])
            y = float(states_df[states_df.state == state]['y'])
            writer.goto(x, y)
            writer.write(state, align="center", font=FONT)


turtle.mainloop()

