initial_amount = 50000
on_marketing = initial_amount * 25/100
on_operationnal = initial_amount * 50/100
on_customer = initial_amount * 25/100
number_of_customer = on_customer / 5

print(f"Ahmed 's initial amount is {initial_amount}\n He spends {on_marketing} on Marketing \n"
      f"He spends {on_operationnal} on Operationnal \n"
      f"He spends {on_customer} on Customers qnd acquires {number_of_customer} customers ")
