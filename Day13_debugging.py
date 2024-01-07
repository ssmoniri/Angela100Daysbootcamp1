
#debugging

def my_function():
   for i in range(1, 20):
    if i == 20:   #assumtion is not correct because this never comes to 20 so we have to change (1, 21)
       print("You got it")
 my_function()

Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # opposite to range include the both ends and 6 is out of ragne so (0, 5)
print(dice_imgs[dice_num])


