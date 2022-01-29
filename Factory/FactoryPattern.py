class Pizza(object):
    def __init__(self):
        self.prepare_str = 'Pizza start prepare'
        self.bake_str = 'Pizza start bake'
        self.cut_str = 'Pizza start cut'
        self.box_str = 'Pizza in box'

    def prepare(self):
        prepare_ins = self.prepare_str
        return prepare_ins

    def bake(self):
        bake_ins = self.bake_str
        return bake_ins

    def cut(self):
        cut_str = self.cut_str
        return cut_str

    def box(self):
        box_str = self.box
        return box_str


class CheesePizza(Pizza):
    ...


class VegetablePizza(Pizza):
    ...


class SeafoodPizza(Pizza):
    ...


class SimplePizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        pizzas = dict(cheese=CheesePizza, vegetable=VegetablePizza, seafood=SeafoodPizza)
        return pizzas[pizza_type]()


class PizzaStore(object):
    def order_pizza(self, pizza_type):
        self.pizza = SimplePizzaFactory.create_pizza(pizza_type)

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        return self.pizza


new = PizzaStore()
obj = new.order_pizza('cheese')
print(obj.prepare())
