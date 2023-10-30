from owlready2 import *

namespace = 'http://test.org/auto.owl'

onto = get_ontology(namespace)

with onto:

    class Car(Thing):
        def tip(self):
            print('This is a general tip for this type of car.')

        def price_range(self):
            print('The price range for this car is undefined.')

    class has_manufacturer(Car >> str, FunctionalProperty):
        pass

    class has_model(Car >> str, FunctionalProperty):
        pass

    class has_year(Car >> int, FunctionalProperty):
        pass

    class has_mileage(Car >> int, FunctionalProperty):
        pass

    class has_color(Car >> str, FunctionalProperty):
        pass

    class has_price(Car >> float, FunctionalProperty):
        pass
    
    class has_weight(Car >> int, FunctionalProperty):
        pass

    class MiniCar(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, max_inclusive=10000))
        ]

        def tip(self):
            print('This is a mini car. Ideal for city driving!')

        def price_range(self):
            print('The price range for this mini car is up to $10,000.')

    class SmallCar(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=10000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=17000))
        ]

        def tip(self):
            print('This is a small car. Efficient and practical!')

        def price_range(self):
            print('The price range for this small car is $10,000 to $17,000.')

    class MidsizeCar(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=17000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=23000))
        ]

        def tip(self):
            print('This is a midsize car')

        def price_range(self):
            print('The price range for this midsize car is $17,000 to $23,000')

    class FullSizeCar(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=23000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=27000))
        ]

        def tip(self):
            print('This is a full-size car.')

        def price_range(self):
            print('The price range for this full-size car is $23,000 to $27,000.')

    class BusinessCar(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=27000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=35000))
        ]

        def tip(self):
            print('This is a business car.')

        def price_range(self):
            print('The price range for this business car is $27,000 to $35,000.')


    class SportsCoupe(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=35000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=40000))
        ]

        def tip(self):
            print('This is a sports coupe.')

        def price_range(self):
            print('The price range for this sports coupe is $35,000 to $40,000.')

    class Minivan(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=40000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=50000))
        ]

        def tip(self):
            print('This is a minivan.')

        def price_range(self):
            print('The price range for this minivan is $40,000 to $50,000.')

    class Van(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=50000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=60000))
        ]

        def tip(self):
            print('This is a van. Perfect for commercial use!')

        def price_range(self):
            print('The price range for this van is $50,000 to $60,000.')

    class OffRoadCar(Car):
        equivalent_to = [
            Car
            & has_price.some(ConstrainedDatatype(float, min_inclusive=60000))
            & has_price.some(ConstrainedDatatype(float, max_inclusive=68000))
        ]

        def tip(self):
            print('This is an off-road car. Ready for any terrain!')

        def price_range(self):
            print('The price range for this off-road car is $60,000 to $68,000.')


print('Before:')

car1 = Car('car1')
print(car1.name)
car1.tip()
car1.has_manufacturer = "Toyota"
car1.has_model = "Corolla"
car1.has_year = 2020
car1.has_mileage = 20000
car1.has_color = "Red"
car1.has_price = 25000
car1.has_weight = 1600
print()

car2 = Car('car2')
print(car2.name)
car2.tip()
car2.has_manufacturer = "Mercedes"
car2.has_model = "S-Class"
car2.has_year = 2023
car2.has_mileage = 5000
car2.has_color = "Black"
car2.has_price = 36000
car2.has_weight = 2190
print()

car3 = Car('car3')
print(car3.name)
car3.tip()
car3.has_manufacturer = "Honda"
car3.has_model = "Civic"
car3.has_year = 2018
car3.has_mileage = 35000
car3.has_color = "Blue"
car3.has_price = 18000
car3.has_weight = 1450
print()

car4 = Car('car4')
print(car4.name)
car4.tip()
car4.has_manufacturer = "BMW"
car4.has_model = "320i"
car4.has_year = 2006
car4.has_mileage = 1000000
car4.has_color = "White"
car4.has_price = 29000
car4.has_weight = 1800
print()

sync_reasoner()

print('After:')

print(car1.name)
print(car1.has_manufacturer)
print(car1.has_model)
car1.tip()
car1.price_range()
print()

print(car2.name)
print(car2.has_manufacturer)
print(car2.has_model)
car2.tip()
car2.price_range()
print()

print(car3.name)
print(car3.has_manufacturer)
print(car3.has_model)
car3.tip()
car3.price_range()
print()

print(car4.name)
print(car4.has_manufacturer)
print(car4.has_model)
car4.tip()
car4.price_range()
print()

onto.save(file='auto.owl', format="rdfxml")