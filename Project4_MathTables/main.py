# FUNCTIONS
def display_math_table(n, min=1, max=10):
    if min < max:
        for i in range(min, max+1):
            answer = i * n
            print(f"{i} x {n} = {answer}")
    else:
        print("ERROR : INCORRECT VALUES")
        
        


# ---------------------------------------------------------
# PROGRAM
min_numb = 1
max_numb = 10


print("PROGRAM START")
print()
display_math_table(12, min_numb, max_numb)
print()
print("PROGRAM END")