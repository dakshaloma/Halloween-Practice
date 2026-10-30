pumpkin = 0
x = 1
while x==1:
user_ans = input("Do you want to add a pumpkin to your cart?(Yes/No): ")
if user_ans == "Yes":
pumpkin+= 1
else:
  x = 0
if pumpkin >= 5 and pumpkin <= 10:
  cost = (pumpkin*4)*0.90
elif pumpkin >= 10: 
  cost = (pumpkin*4)*0.80
else:
  cost = (pumpkin*4)

print(cost)




