# Author: JD 01/13/2021

print('Enter the net sales for')

try:
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)

except ValueError:
    print("Invalid input. Please enter numerical values for both prior period and current period")

except ZeroDivisionError:
    print("The previous period can not be zero. Please enter a different value that is not zero.")

finally:
    print("Thank you for using this program, have a great day.")
