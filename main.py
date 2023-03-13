from turtle import Screen, Turtle
import turtle
import pandas
data = pandas.read_csv("36_states.csv")
state_name = data.state.to_list()
score = 0
guess = []
screen = Screen()
screen.title("Nigeria State Game")
screen.setup(width=600, height=500)
screen.bgpic("image/map_of_Nigeria.gif")

while len(guess)<len(state_name):

    answer_text = screen.textinput(f"{score}/{len(state_name)}  State name","Enter the name of a state?")
    if answer_text.title() == "Exit":
        break
    elif answer_text != None:
        answer_text = answer_text.title()
        for state in state_name:
            if answer_text in guess:
                pass

            else:
                if answer_text == state:
                    guess.append(answer_text)
                    score += 1
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.goto(int(data[data.state == state].x), int(data[data.state == state].y))
                    turtle.write(f"{state}", font=("arial", 9, "normal"))


    else:
        break
print(len(state_name))
missing = [state for state in state_name if state not in guess]
print(len(missing))
pandas.DataFrame(missing).to_csv("missing_state.csv")