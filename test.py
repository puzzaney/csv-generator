import csv
import random

# import json

transaction = ['Cash Deposited', 'Cheque Withdrawn']

field_names = ['transaction', 'debit', 'credit']

deposit_list = []
total = 0

cheque_no = 222
account_no = "NS00301"

for i in range(random.randint(70, 80)):

    transaction_type = random.choice(transaction)

    if (transaction_type == 'Cash Deposited'):
        transaction_amount = random.randint(1, 100) * 1000
        deposit_list.append(
            {"transaction": transaction_type, "debit": 0, "credit": transaction_amount})
        total = total + transaction_amount
    else:
        cheque_no = cheque_no + 1
        transaction_amount = random.randint(1, 50) * 1000
        deposit_list.append(
            {"transaction": f"{transaction_type} #{account_no}-00{cheque_no}", "debit": transaction_amount, "credit": 0, })
        total = total - transaction_amount


print(f"Total: {total}, No of Transactions: {len(deposit_list)}")


with open('transactions.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, field_names)
    writer.writeheader()
    writer.writerows(deposit_list)
