print("Welcome to the Daily Expense Tracker!\n")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
entrada_usuario = 0
despesas = []
despesa_num = 0
total_expense = 0
average_expense = 1
while (entrada_usuario != 5):
    entrada_usuario = int(input())
    if entrada_usuario == 1:
        entrada_despesa = float(input())
        despesas.append(entrada_despesa)
        print("Expense added successfully!")
    elif entrada_usuario == 2:
        if len(despesas) > 0:
            print("Your expenses:")
            despesa_num = 0
            for despesa in despesas:
                despesa_num += 1
                print(f"{despesa_num}. {despesa}")
        else:
            print("No expenses recorded yet.")
    elif entrada_usuario == 3:
        if len(despesas) > 0:
            total_expense = 0
            for despesa in despesas:
                total_expense = total_expense + despesa
            average_expense = total_expense / len(despesas)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")
        else:
            print("No expenses recorded yet.")
    elif entrada_usuario == 4:
        despesas.clear()
        print("All expenses cleared.")
        
print("Exiting the Daily Expense Tracker. Goodbye!")
