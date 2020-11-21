price=1000000
good_credit=True
High_salary= False

if price>100000:
    print('amount is too big ')
    down_payment= price*0.1
elif good_credit and High_salary:
    down_payment = 0.05 * float(price)
else:
    down_payment= 0.2*float(price)

print(f'{down_payment} is the amount of downpayment')