'13.1'
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating  #13.3

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}/5")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлён до {self.rating}/5.")
        else:
            print("Ошибка: рейтинг должен быть от 0 до 5.")

newRestaurant = Restaurant("mamaro", "italian")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
'13.2'
restaurant1 = Restaurant("moresushi", "japan")
restaurant2 = Restaurant("texasbilli", "american")
restaurant3 = Restaurant("pelmeniidom", "russian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
'13.3'
restaurant1.update_rating(4.5)
restaurant2.update_rating(3.8)
restaurant3.update_rating(5)
newRestaurant.update_rating(4.2)

