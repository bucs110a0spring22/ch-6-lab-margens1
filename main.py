import turtle

def seq3np1(n):
    """
    takes a number and reduces it to one by either applying        3n+1 or dividing by two
    args: n - the starting value for the sequence
    return: The number of iterations
    """
    count = 0
    while(n != 1):
        count = count+1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
            count = count+1
    return count


def graphIterations(upperBound=0):
  """
  draws a line graph with the number of iterations and their     values after applying the 3n+1 sequence
  args: the upperbound value of the sequence
  return: a line graph of the number of iterations
  """
  drawGraph = turtle.Turtle()      
  drawGraph.penup()
  drawGraph.goto(0,0)
  drawGraph.pendown()
  writer = turtle.Turtle()
  window = turtle.Screen()          
  window.setworldcoordinates(0,0,10,10)
  max_so_far = 0
  for i in range(1, upperBound+1):
    value = seq3np1(i)
    print(i, "iterations for value of", value)
    if value > max_so_far:
      max_so_far = value
      writer.clear()
      writer.up()
      writer.goto(i,value)
      writer.write("Maximum so far:"+str(max_so_far))
    window.setworldcoordinates(0,0,i+10,max_so_far+10)
    drawGraph.goto(i,value)
  window.exitonclick()

def main():
  value = int(input("Enter a number: "))
  if value > 0:
    for start in range(1, value+1):
      iteration = seq3np1(start)
  else:
    quit()
    print(iteration, "iterations for value of", value)

  graphIterations(value)
    
main()
