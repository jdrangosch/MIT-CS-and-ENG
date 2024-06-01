## 6.100A PSet 1: Part A
## Name: Julian Drangosch
## Time Spent: 
## Collaborators: ---
import math

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = int(input('Enter yearly salary: '))
portion_saved = float(input('Enter portion saved: '))
cost_of_dream_home = int(input('Enter cost of dream home: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

months = 1
portion_down_payment = 0.25*cost_of_dream_home
amount_saved = 0
r = 0.05
monthly_salary = yearly_salary/12
r_12 = r/12

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < portion_down_payment:
    amount_saved += monthly_salary * portion_saved
    amount_saved += amount_saved * r_12
    months = months + 1
print(months)
######
# Just Math
######
# months = math.log((portion_down_payment / monthly_salary) * r_12 + 1) / math.log(1 + r_12)
# print(months)