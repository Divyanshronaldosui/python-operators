#taking total amount as input from user
amount=(int(input("pls enter amount for withrawal=")))

#calculating no. of notes of different denominations
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print("notes of hundred rupees=",note1)
print("notes of fifty rupees=",note2)
print("notes of ten rupees=",note3)