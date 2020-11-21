price=1000000
good_credit=True
High_salary= False

if good_credit or High_salary:

    down_payment= 0.1*float(price)
elif good_credit and High_salary:
    down_payment = 0.05 * float(price)
else:
    down_payment= 0.2*float(price)

print(f'{down_payment} is the amount of downpayment')