# Author: JD 01/12/2022

def tem_conv():
    while True:
        try: 
            temp = float(input("Enter the temperature: "))
            type = input("Convert it into?(f/c)").upper()
            if type == "C":
                result = (temp - 32) * 5 / 9
                print("The temperature in celsius is {0}.".format(result))
            elif type == "F":
                result = temp / 5 * 9 + 32
                print("The temperature in celsius is {0}.".format(result))
            else:
                print("Invalid input, enter either f to transfer it into fahrenheir and c for celsius.")
        except ValueError:
            print("Invalid input, enter a numerical value for the temperature")


tem_conv()