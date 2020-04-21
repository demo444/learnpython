# This is a comment.  Everything after the '#' is ignored by Python, it's just for documentation

# Assign 5000 to the variable 'alice_balance' to represent $5000 being in Alice's bank account
alice_balance = 5000

# print out the amount in Alice's bank account
print("Alice has")
print(alice_balance)

# print everything together using .format
# .format substitutes something for the {} symbols
print("Alice has ${}".format(alice_balance))

# print two different things together using .format
bob_balance = 10000
print("Alice has ${} and Bob has ${}".format(alice_balance, bob_balance))

# add the variable 'alice_balance' to the variable 'bob_balance' and put the result in the variable 'total'
total = alice_balance + bob_balance

# print out the balances and total
print("Alice has ${} and Bob has ${} for a total of ${}".format(alice_balance, bob_balance, total))

