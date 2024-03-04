from random import sample

# Declare the function with one argument (password length)
def password_generator(length):
  
    # Define characters and symbols
    
    abc_lowercase = "abcdefghijklmnopqrstuvwxyz"
    
    # HACK: upper() transforms the letters in a string to uppercase
    abc_uppercase = abc_lowercase.upper() 
    
    numbers = "0123456789"
    symbols = "{}[]()*;/,_-"
    
    # Define the sequence
    sequence = abc_lowercase + abc_uppercase + numbers + symbols
    
    # Call the sample() function using the sequence and length
    password_union = sample(sequence, length)
    
    # Use join to insert elements of a list into a string
    password_result = "".join(password_union)
    
    # Return the variable "password_result"
    return password_result

# Call the function "password_generator" and pass the value "20"    
password = password_generator(20)

# Print the result
print("Password: ", password)
