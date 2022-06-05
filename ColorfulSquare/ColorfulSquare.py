import turtle
colors = ['red', 
          'purple', 
          'blue', 
          'green', 
          'yellow', 
          'orange'
          ]
for x in range(300):
    pencolor(colors[x%6])
    width(x / 60)
    forward(x)
    left(90)