# FREEZE CODE BEGIN
from car_utils import create_car_from_input, display_cars
from car import *

def create_car_from_input():
    car_id = input("Enter car ID (e.g., CAR001):\n")
    brand = input("Enter car brand:\n")
    year = int(input("Enter car year:\n"))
    color = input("Enter car color:\n")
    mileage = float(input("Enter mileage:\n"))
    return Car(car_id, brand, year, color, mileage)

def display_cars(car_dict):
  for car in car_dict.values():
     print(car)
# FREEZE CODE END
cars = {}
while True:
    opcion = input("""
                  1. Add car
                  2. View cars
                  3. Drive car
                  4. Paint car
                  5. Exit""")
    if opcion == "1":
           car = create_car_from_input()
           cars[car.car_id] = car
           print(car)
           print("Car added.")
   
    elif opcion == "2":
           display_cars(cars)
   
    elif opcion == "3":
           car_id = input()
           miles = float(input())
   
           if car_id in cars:
               cars[car_id].drive(miles)
               print("Mileage updated.")
               print(cars[car_id])
   
    elif opcion == "4":
           car_id = input()
           new_color = input()
   
           if car_id in cars:
               cars[car_id].change_color(new_color)
               print("Color updated.")
               print(cars[car_id])
   
    elif opcion == "5":
           print("Goodbye!")
           break