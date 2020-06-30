import random

def smth():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  for i in range(rnd):
    print(quotes[i], end=' ')

if __name__== "__main__":
  smth()
