#Python Banking Program
def show_balance(balance):
  print("*******************")
  print(f"Your balance is: ${balance:}")
def deposit():
  print("*******************")
  amount = float(input("Enter amount to deposit: $"))
  if amount < 0:
    print("Not a valid amount")
    return 0
  else:
    return amount

def withdraw(balance):
  print("*******************")
  amount = float(input("Enter amount to withdraw: $"))
  if amount < 0:
    print("*******************")
    print("Amount Should be greater than 0")
    return 0
  elif amount > balance:
    print("*******************")
    print("Insufficient Funds")
    return 0
  else:
    return amount

def main():
  balance = 0
  is_running = True

  while is_running:
    print("*******************")
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*******************")
    choice = input("Enter your choice: ")

    if choice == "1":
      show_balance(balance)
    elif choice == "2":
      balance += deposit()
    elif choice == "3":
      balance -= withdraw(balance)
    elif choice == "4":
      is_running = False
    else:
      print("Invalid choice")
  print("*******************")
  print("Thank You! Have a nice day")

if __name__=='__main__':
  main()