from rich import print
from .utils import read_expenses, write__to_expenses
from datetime import datetime


def add_to_expenses(description, amount, category):

    #error checks
    if amount <= 0:
        print("Amount must be greater than [bold green]0[bold green]")
        return
    
    try:
        amount = float(amount)
        if round(amount, 2) != amount:
            raise ValueError("[bold red]Amount can only have at most two decimal places.[bold red]")
    except ValueError as e:
        print(f"[bold red]{e}[bold red]")
        return
    
    expenses = read_expenses()

    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]['id'] + 1
    
    expenses.append({
        'id':  expense_id,
        'date': datetime.now().isoformat(),
        'description': description,
        'amount': amount,
        'category': category if category else ""
    })

    write__to_expenses(expenses)
    print(f"New expense [bold green]added[/bold green] with ID [bold magenta]{expense_id}[bold magenta]")

