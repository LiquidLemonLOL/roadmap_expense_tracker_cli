import json
import rich
from rich.console import Console
from rich.table import Table
import argparse
from ops import *

#init main parser + subparser
parser = argparse.ArgumentParser(description="Expense Tracker")
subparsers = parser.add_subparsers(dest= 'sub' help="Sub-commands")

#add each subparser (add, delete, update, list, summary)
subparser_add = subparsers.add_parser('add', help="Add a new expense")
subparser_add.add_argument('--description', required=True, type=str, help="Description of the expense")
subparser_add.add_argument('--category', required=True, type=str, help="Category of the expense")
subparser_add.add_argument('--amount', required=True, type=float, help="Amount of the expense")

subparser_delete = subparsers.add_parser('delete', help="Delete an existing expense based on ID")
subparser_delete.add_argument('--id', help="ID for the expense to delete")

subparser_update = subparsers.add_parser('update', help="Updates an existing expense")
subparser_update.add_argument('--id', required=True, help="ID of expense to update")
subparser_update.add_argument('--description', help="New description for expense")
subparser_update.add_argument('--amount', help="New amount for expense")

subparser_list = subparsers.add_parser('list', help="Displays list of all expenses")

subparser_summary = subparsers.add_parser('summary', help="Shows summary of total amount of expenses")
subparser_summary.add_argument('--month', type=int, help="Shows expense summary for month number")

#parse user args and match for function
args = parser.parse_args()

match args.sub:
    case 'add':
        #add function
    case 'delete':
        #add function
    case 'update':
        #add function
    case 'list':
        #add function
    case 'summary':
        #add function
