# concept of variable update or reassignment
marry_salary = 2000
jhon_salary  = 2000
balance = marry_salary + jhon_salary

# the company will promote one of them
bonus = 200

marry_promotion = False

if marry_promotion:
    marry_salary = marry_salary + bonus
else:
    jhon_salary = jhon_salary + bonus

# update balance
balance = marry_salary + jhon_salary

# Question: What is the current bank balance
print(balance)
