# Created by: Zack Isingoma
# Created on: 19th Jan 2022.
# converts ºC of ºF
def calculate_farenheigt():
    user_degrees = input("Enter degrees in celcius: ")
    try:
        user_degrees_float = float(user_degrees)
        degrees_farenheight = (9.0/5.0)*user_degrees_float+32
        print("{}ºC is equal to {}ºF ".
              format(user_degrees_float, degrees_farenheight))
    except Exception:
        print("Invalid input")


calculate_farenheigt()
