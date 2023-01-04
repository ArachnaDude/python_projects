income = float(input("Enter the annual income: "))


threshold = 85528
tax_relief = 556.2

if income <= threshold:
  percentage_tax =  (18 * income) / 100
  tax = percentage_tax - tax_relief
  if tax < 0: tax = 0.0
else:
  surplus = income - threshold
  percentage_tax = (32 * surplus) / 100
  tax = 14839.2 + percentage_tax
  if tax < 0: tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
