from moduleA import Nothing

print("About to instantiate Nothing")
n = Nothing() # Its __name__ is: moduleA
print("We have a Nothing")

# Run moduleB and watch how the print statements
# in moduleA are printed to the terminal

