import random
# count  = 0
def random_no():
  count  = 0
  while count <10:
    num =random.randint(1,100)
    print(num,end="")
    count+=1
random_no()
