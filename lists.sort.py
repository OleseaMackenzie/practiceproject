cars = ['tesla', 'bmw', 'moskovich','tesla',]
# Chapter 3 : Lists sort

cars = ['tesla','bmw','lexus','moskovich', ]
print("Permanent sorting _ sort().")
print("List before sorting: ", cars)
cars.sort()
print("list after sorting:", cars)

names = ['john','jane','mark']
print("List before sorting: ", names)
names.sort(reverse=True)
print("List after sorting: ", names)

print("Sorting temporarily - sorted()")
car_models = ['corolla', 'camry','model x','550 xi' ]
print("Car models before sorting: ", car_models)
sorted_car_models_asc = sorted(car_models)
sorted_car_models_desc = sorted(car_models, reverse=True)

print("Car models before sorting: ", car_models)
print("Car models after sorting in ascending order: ", sorted_car_models_asc)
print("Car models after sorting in descending order: ", sorted_car_models_desc)

print("reversing(permanent) the list without sorting: ")
nums = [6, 3, 9, 7, 10]
print("list before reversing: ", nums)
nums.reverse()
print("list after reversing: ", nums)