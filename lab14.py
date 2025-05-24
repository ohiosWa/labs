'14.1'
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}/5")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
            print(f"Рейтинг обновлён до {self.rating}/5.")
        else:
            print("Ошибка: рейтинг должен быть от 0 до 5.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors  # Список сортов мороженого

    def show_flavors(self):
        print("Доступные вкусы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")
ice_cream_shop = IceCreamStand("Кафе-Мороженое", "Десерты", ["Ванильное", "Шоколадное", "Клубничное"])
ice_cream_shop.describe_restaurant()
ice_cream_shop.update_rating(4.7)
ice_cream_shop.show_flavors()
'14.2'
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.hours = hours
        self.types = {
            "палочка": [],
            "мягкое": [],
            "пломбир": []
        }

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Добавлен вкус: {flavor}")
        else:
            print(f"{flavor} уже есть в списке.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Удалён вкус: {flavor}")
        else:
            print(f"{flavor} не найден в списке.")

    def check_flavor(self, flavor):
        return flavor in self.flavors

    def add_ice_cream_type(self, type_name, flavor):
        if type_name in self.types:
            self.types[type_name].append(flavor)
        else:
            self.types[type_name] = [flavor]

    def show_ice_cream_types(self):
        print("Типы мороженого:")
        for type_name, flavor_list in self.types.items():
            print(f"{type_name.capitalize()}: {', '.join(flavor_list)}")
'14.3'
import tkinter as tk
from tkinter import messagebox
class IceCreamGUI:
    def __init__(self, stand):
        self.stand = stand
        self.root = tk.Tk()
        self.root.title("Кафе-мороженое")

        self.label = tk.Label(self.root, text="Доступные вкусы мороженого:")
        self.label.pack()

        self.flavor_listbox = tk.Listbox(self.root)
        self.update_flavor_list()
        self.flavor_listbox.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Добавить вкус", command=self.add_flavor)
        self.add_button.pack()

        self.remove_button = tk.Button(self.root, text="Удалить вкус", command=self.remove_flavor)
        self.remove_button.pack()

        self.check_button = tk.Button(self.root, text="Проверить наличие", command=self.check_flavor)
        self.check_button.pack()

        self.root.mainloop()

    def update_flavor_list(self):
        self.flavor_listbox.delete(0, tk.END)
        for flavor in self.stand.flavors:
            self.flavor_listbox.insert(tk.END, flavor)

    def add_flavor(self):
        flavor = self.entry.get()
        self.stand.add_flavor(flavor)
        self.update_flavor_list()

    def remove_flavor(self):
        flavor = self.entry.get()
        self.stand.remove_flavor(flavor)
        self.update_flavor_list()

    def check_flavor(self):
        flavor = self.entry.get()
        if self.stand.check_flavor(flavor):
            messagebox.showinfo("Результат", f"{flavor} доступен!")
        else:
            messagebox.showwarning("Результат", f"{flavor} не найден.")
flavors = ["Ваниль", "Шоколад", "Клубника"]
stand = IceCreamStand("эскимо.ру", "Десерты", flavors, "Центр города", "10:00–22:00")
gui = IceCreamGUI(stand)