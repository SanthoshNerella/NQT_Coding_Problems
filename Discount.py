amount = int(input())
payable = 0
if amount < 1000 :
    payable = amount - ( (5 / 100) * amount) # payable = ( 95 / 100) * amount
elif amount >= 1000 and amount < 5000 :
    payable = amount - ((10 / 100) * amount) # payable = (90 / 100) * amount
elif amount >= 5000 :
    payable = amount - ((15 / 100) * amount) # payable = (85 / 100) * amount
# print(int(payable))
print(f"{payable:.2f}")

