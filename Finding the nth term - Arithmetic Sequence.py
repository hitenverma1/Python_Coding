#Number Sequence - Finding the nth term - (Arithmetic Sequence)

startingValue = int(input("Enter the starting value:"))
nextValue = int(input("Enter the next value:"))

n = int(input("Which term in the sequence would you like to find?"))

increment = nextValue - startingValue

if startingValue>=0:
  sequence = str(increment)+"n + "  + str(startingValue)
else:
  sequence = str(increment)+"n "  + str(startingValue)

nthTerm = increment*n+startingValue

print("Number Sequence: " + sequence)
print("The number in position " + str(n) + " is : " + str(nthTerm))
