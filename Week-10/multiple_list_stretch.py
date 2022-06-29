
print("\nEnter the names and balances of bank accounts (type: quit when done)")

bank_accounts = []
balances = []

name_account = ''
update = "yes"

while name_account != "quit":
  name_account = input("What is the name of this account? ")
  if name_account == "quit":
    break
  amount_balance = float(input("What is the balance? "))
  bank_accounts.append(name_account)
  balances.append(amount_balance)



print("\nAccount Information:")

for i in range(len(bank_accounts)):
  print(f"{i}. {bank_accounts[i]}  - ${balances[i]:.2f}")

total = 0
highest_balance = 0
highest_balance_index = 0

for index, value in enumerate(balances):
  total += value
  if value > highest_balance:
    highest_balance = value
    highest_balance_index = index


print(f"\nTotal: ${total:.2f}")
print(f"Average: ${total / len(balances):.2f}")
print(f"Highest balance: {bank_accounts[highest_balance_index]} - ${balances[highest_balance_index]:.2f}")

while update == "yes":
  update = input("\nDo you want to update an account? ")
  if update != "yes":
    break
  account_index = int(input("What account index do you want to update? "))
  balances[account_index] = float(input("What is the new amount? "))
  print("\nAccount Information")
  for i in range(len(bank_accounts)):
    print(f"{i}. {bank_accounts[i]}  - ${balances[i]:.2f}")


print("\nAccount Information")
for i in range(len(bank_accounts)):
    print(f"{i}. {bank_accounts[i]}  - ${balances[i]:.2f}")