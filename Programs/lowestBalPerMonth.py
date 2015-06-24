balance = 3068
monthlyPaymentRate = 0.06
annualInterestRate =  0.22
monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0
minMonthlyPayment = 0
tempBalance = balance
while tempBalance > 0:
    minMonthlyPayment += 10
    tempBalance = balance
    for i in range(1,13):
        tempBalance = tempBalance - minMonthlyPayment
        tempBalance = tempBalance + (monthlyInterestRate * tempBalance)
print 'Lowest Payment: %.2f ' % minMonthlyPayment
