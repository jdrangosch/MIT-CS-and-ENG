## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = 65000 #int(input('Enter initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_home = 800000
portion_down_payment = 0.25*cost_of_dream_home
ri = 0.0
rf = 1.0
r = (ri + rf) / 2
steps = 1
amount_error = 100

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while True:
    amount_saved = initial_deposit * (1 + (r/12)) ** 36
    if abs(amount_saved -portion_down_payment) <= amount_error:
        print(amount_saved)
        print(steps)
        break
    elif amount_saved > portion_down_payment + amount_error:
        rf = r
    elif amount_saved < portion_down_payment - amount_error:
        ri = r
    r = (ri + rf) / 2
    steps += 1