class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(User):
    def __init__(self, name, age, grade):
        supep().__init__(name, age)
        self.grade = grade
