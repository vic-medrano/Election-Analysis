print("Hello World")
print("Hello world")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1]) 
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not the list of counties")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")
if "Arapahoe" in counties or "El Paso" in counties:
     print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El paso is not in the list of counties")
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)  
for num in range(5):
    print(num)  
counties_dict = {"Arapahoe", 422829, "Denver": 463353, "Jefferson", 432438}
for i in range(len(counties)):
    print(counties[i])
for county in counties_dict:
    print(county)   
for county in counties_dict.keys():
    print(county)

