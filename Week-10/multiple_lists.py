print("\nEnter the names and balances of bank accounts (type: quit when done)\n")


bank_accounts = []

balances = []

name_account = ""

while name_account != "quit":
  name_account = input("What is the name of this account? ")
  if name_account == "quit":
    break
  amount_balance = float(input("What is the balance? "))
  bank_accounts.append(name_account)
  balances.append(amount_balance)


print("\nAccount Information:")


for i in range(len(bank_accounts)):
  print(f"{bank_accounts[i]} - ${balances[i]:.2f}")

total = 0

for value in balances:
  total += value

print(f"\nTotal: ${total:.2f}")
print(f"Average: ${total / len(balances):.2f}")