# for conditional statement, declare the variable or fn first then run the cond statements on it:
age = 40
if age < 23:
    print("You are still young")
elif age >= 40:
    print("Haha grandpa")
else:
    print("You are getting old")

print(30 <= 40)


# nested conditions
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')  # You are eligible to vote
    else:
        print('Citizen but not eligible to vote')
else:
    print('You are not eligible to vote')

# false values(py)
print(bool(""))
print(bool(0))
print(bool(False))


# boolean operators in py: and (checks multiple conds if met), or (compare between 2 conds)), not (negate)
# uses
print(is_citizen and age)
