# Exercise

# Calculate the weight in kg or lbs

user_weight = float(input("Weight: "))
is_km_or_lb = input("type k if your number is in (K)g or l if your number is in (L)bs: ")
kg_to_lb = user_weight / 2.2046
lb_to_kg = user_weight * 2.2046

if is_km_or_lb == 'l':
    print("Your weight in Kgs is: " + str(kg_to_lb))
elif is_km_or_lb == 'k':
    print("Your weight in Lbs is: " + str(lb_to_kg))
else:
    print("Enter a valid letter 'k' or 'l'")
print("Thank you, goodbye!")
