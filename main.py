from random import randint

x= randint(1,100)
count=0

while True :
	y = int(input("Quale numero sara'?"))
	count+=1
	if x==y :
		print("Hai trovato il numero giusto")
		break
	elif x>y :
		print ("il numero e' maggiore di {}".format(y))
	else :
		print ("il numero e' minore di {}".format(y))
