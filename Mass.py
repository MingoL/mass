#Color Setting
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

#The weight of the bag
def Mass():
	try:
		print(G+"MASS"+W)
		BagWidth    = int(input("Width mm:"))
		BagLength   = int(input("Length mm:"))
		Thickness   = int(input("Thickness micron:"))
		Density     = float(input("Density:"))
		sum         = BagLength*BagWidth*Thickness*Density/1000000
		print(G+"Weight of the Bag in Gramme is: "+W, sum)
	except ValueError:
		return

#Blow Up Ratio for the die
def BUR():
	try:
		print(G+"BUR"+W)
		DieSize		= int(input("Die Size mm:"))
		BagWidth    = int(input("Width mm:"))
		sum         = BagWidth/1.57/DieSize
		print(G+"BUR is: "+W, sum)
	except ValueError:
		return

#... ...
def main():
	exit = False
	while not exit:
		print("1 = Mass")
		print("2 = BUR")
		print("3 = Exit Program")
		C = int(input(O+"option ="+W))
		if C == 1:
			Mass()
		elif C == 2:
			BUR()
		elif C == 3:
			exit = True
			print("Exiting Program")
			#break
		print(R+"Enter a number"+W)
			#else:
			#	print("enter a number")
			#TEST1
		

if __name__ == "__main__":
    main()
