# EMI calculator
print("=========EMI Calculator========")
on_road_price = 1271695
down_payment = 100000
P =  on_road_price-down_payment # P is Principal amount for EMI
interest_rate = 10
r = interest_rate/100/12 #yearly interest is 10%, divided by 12 to find monthly interest(r)
no_of_years = 5 #no_of_years indicates no of years of the loan
n = no_of_years*12 #converting in to months

E = P*r*((1+r)**n/(((1+r)**n)-1))
print("EMI = ",round(E))

print("=========EMI Calculator========")


on_road_price = int(input("On Road Price = "))
down_payment = int(input("Down payment = "))
P =  on_road_price-down_payment # P is Principal amount for EMI
interest_rate = float(input("Interest rate = "))
r = interest_rate/100/12 #yearly interest is 10%, divided by 12 to find monthly interest(r)
no_of_years = int(input("No of years = ")) #no_of_years indicates no of years of the loan
n = no_of_years*12 #converting in to months

E = P*r*((1+r)**n/(((1+r)**n)-1))
print("EMI = ",round(E))
