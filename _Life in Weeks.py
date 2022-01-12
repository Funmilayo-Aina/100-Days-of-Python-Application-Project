# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
Years_remaining = 90- age_as_int
day_remaining = Years_remaining*365
months_remaining = Years_remaining*12
weeks_remaining = Years_remaining*52

feedback = f"You have {day_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(feedback)




