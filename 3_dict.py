# Write a program to filter the keys from the dictionary.

age_dict = {'manoj':21, "akshay":22, "uday":21, "rishikesh":27, "kumar":22}

print(f'\n \n Original dictionaty : \n {str(age_dict)}')

# Filter all values 
val = [value for key, value in age_dict.items()]
print("\n All value of the dictionary ",val)

# Filter data using list method
age = age_dict["manoj"] 
print(f'\n Age of Manoj is : {age}')

# Filter values with dictionary comphrehension
vals = [value for key, value in age_dict.items() if value > 21]
print("\n Range values",vals)

