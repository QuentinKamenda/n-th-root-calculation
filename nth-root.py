# Work Sample : n-th root calculation
# Using a derivattion from Newton's method
# by: Quentin KAMENDA
# for: ME Creative Studio
# 19/12/2017

# Input
a = float(input("Enter a number: "))
b = int(input("Enter an integer from 2 to 10: "))
#e = float(input("Enter the wanted precision: "))

# Function to calculate the n-th root of k with a precision e
# (u0 represents the starting point, some starting poitns are optimum for specific roots)
def nth_root(k, n, u0, e):
    # Initialisation
    u1 = (n-1)*u0 + k/power(u0, n-1)
    u1 = u1 / n
    if (u0-u1 < e) :
        # Breaking point of the recurrence
        return u1
    else :
        # Recurrence
        return nth_root(k, n, u1, e)

# Function to calculate a power b (a^b):
def power(a, b):
    s = a
    for i in range(1, b):
        s = s*a
    return s

# Result:
s = nth_root(a, b, a, 0.01)

print ("The ",b,"-th root of ",a," is: ",s)

# Verification:
#print (s)
#print (power(s, b))
