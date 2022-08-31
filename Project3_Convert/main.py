def convert():
    unity_str = ""
    while not (unity_str == "INCH" or unity_str == "CM"):
        unity_str = input("Do u want to convert in INCH or CM ? : ")
    number_float = 0
    while number_float == 0 :
        number_str = input("Enter the value to convert : ")
        try:
            number_float = float(number_str)
        except ValueError:
            print("ERROR : you must enter a number !")
    if unity_str == "CM":
        answer = number_float * 2.54
        print(f"{number_float} INCHES = {answer} CM")
    elif unity_str == "INCH":
        answer = number_float * 0.394
        print(f"{number_float} CM = {answer} INCHES")
    
            
    
    
# -------------------------------
convert()