import  pandas

data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")

color = data["Primary Fur Color"].to_list()
gray = 0
cinnamon = 0
black = 0
for nb in color:
    if nb == "Gray":
        gray+=1
    elif nb == "Cinnamon":
        cinnamon+=1
    elif nb == "Black":
        black+=1

work_data = {"Fur Color": ["Gray","Cinnamon", "Black"],
             "count":[gray,cinnamon, black]

}
new_data = pandas.DataFrame(work_data)
new_data.to_csv("newnew_data.csv")