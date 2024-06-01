## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary = 110000 #int(input('Enter yearly salary: '))
portion_saved = 0.15 #float(input('Enter portion saved: '))
semi_annual_raise = 0.03 #float(input('Enter semi annual raise: '))
cost_of_dream_home = 750000 #int(input('Enter cost of dream home: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

months = 1
portion_down_payment = 0.25*cost_of_dream_home
amount_saved = 0
r = 0.05
monthly_salary = yearly_salary/12
monthly_rate = r/12

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < portion_down_payment:
    amount_saved += monthly_salary * portion_saved
    amount_saved += amount_saved * monthly_rate
    months += 1
    if months > 6 and (months -1) % 6 == 0:
        yearly_salary = yearly_salary * (1 + semi_annual_raise)
        monthly_salary = yearly_salary/12
print(months)