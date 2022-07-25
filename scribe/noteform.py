mystr = " Turtles are very cool. They come in all shapes and sizes. They have green shells that protect them from danger"

remlist = ["that ", "the ", "what ", "and ", "them ", "they ","have ", "an ", "to",  "I ", "my ", "has ", "They" ]

splist = mystr.split(".")



for i in range(len(splist)):
  for word in remlist:
    splist[i] = splist[i].replace(word, "")



for i in range(len(splist)):
  splist[i] = "-" + splist[i]



for i in splist:
  print(i)








    




  



