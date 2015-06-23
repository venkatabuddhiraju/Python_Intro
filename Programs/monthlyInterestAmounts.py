balance = 4213
monthlyPaymentRate = 0.04
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0
for i in range(1,13):
    print 'Month: %d ' % i
    minMonthlyPayment = monthlyPaymentRate * balance
    print 'Minimum Monthly Payment: %.2f ' % minMonthlyPayment
    balance = balance - minMonthlyPayment
    print 'Remaining Balance: %.2f ' % balance
    balance = balance + (monthlyInterestRate * balance)
    totalPaid = totalPaid + minMonthlyPayment
print 'Total Paid: %.2f ' % totalPaid
print 'Remaining Balance: %.2f ' % balance
