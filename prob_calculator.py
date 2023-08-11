import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += v * [k]
      print(self.contents)

      def draw(self, num):
        try:
          balls = random.sample(self.contents, num)
        except:
          balls = self.contents

        for ball in balls:
          self.contents.remove(ball)
          
        return balls 

hat = Hat(red=5, orange=4)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    balls = hat.draw(num_balls_drawn)
    # check if balls match expectation
  eb_list = []
  for k, v in expected_balls.items():
      eb_list += v * [k]
    if all(x in balls for x in eb_list): 
      M += 1
    
  probability = M / num_experiments
  return probablity
