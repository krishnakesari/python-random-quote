def main():
  
  import random
  last = 13
  rnd = random.randint(0, last)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print("Just picked a random quote: " + quotes[rnd])
  print("This is the first quote: " + quotes[0])

if __name__== "__main__": main()
