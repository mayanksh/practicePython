def is_leap(year):
    leap = False
    if 1900 <= year <= 10**5:


        return (year % 400 == 0) or (( year % 100 != 0) and (year % 4 == 0))




    # Write your logic here

    return leap

year = int(input())
print(is_leap(year))
