#creating super class pizza
class Pizza:
    def __init__ (self,description,cost):
        self.cost= cost
        self.description=description
        pass
    def get_description(self):
        return self.description
        
    def get_cost(self):
        return self.cost
#creatinga sub class  of pizza  
class ClassicPizza(Pizza):
    def __init__(self):
        description = "Classic Pizza: tomato sauce and mozzarella cheese"
        cost = 27.9
        super().__init__(description, cost)
        

class MargheritaPizza(Pizza):
    def __init__(self):
        description = "Margherita Pizza: tomato sauce, fresh mozzarella cheese, and basil"
        cost = 25.9
        super().__init__(description, cost)
        

class TurkPizza(Pizza):
    def __init__(self):
        description = "Turk Pizza: tomato sauce, Turkish sausage, green peppers, onions, and mozzarella cheese"
        cost = 20.9
        super().__init__(description, cost)
        

class DominosPizza(Pizza):
    def __init__(self):
        description = "Dominos Pizza: tomato sauce, pepperoni, sausage, mushrooms, onions, and mozzarella cheese"
        cost = 37.9
        super().__init__(description, cost)
#creating decorator class        
class Decorator():
    def __init__(self, component):
        self.component = component
    

    def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)


    def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)
#creating subclass of decorator
   
class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 5.0
        self.description = 'with Olives'
class Mushrooms(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 5.0
        self.description = 'with Mushrooms'
class Goat_cheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 15.0
        self.description = 'with GOAT CHEESE'
class Meat(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 15.0
        self.description = 'with MEAT'
class Onions(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 3.0
        self.description = 'with ONİONS'
class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.cost = 6.0
        self.description = 'with CORNS'