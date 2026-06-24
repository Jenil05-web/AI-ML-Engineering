# PYTHON (OOP)

# object = A BUndle of related attributes (variables) and methods (functions)
 # ex . phone , book , cup
# You need a "class" to create many objects

# class = (blueprint) used to design the structre and layout of an object

class Car :
    Car_name = "ABC car" # Class attribute

    def __init__(self , model , year , color,for_sale): # Parameterised Constructor ( because we passed values in it )
       self.model = model
       self.year = year
       self.color = color
       self.for_sale = for_sale

       car1 = Car("BMW" , "2024" , "red" , False)
       car2 = Car("mustang" , "2000" , "red" , True)

       print(Car.Car_name) # we used the attribute 

       print(car1.model)
       print(car2.year)
       print(car1.color)

       
        
        # Methods : methods are functions that belongs to objects




        
