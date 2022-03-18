# Private vs Public Variables _age equals private 
class PlayerCharacter:
    def _init_(self, name, age):
        self._name = name 
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('andrei', 100)
camera.takepicture()
# player1.name = '!!!'
# player1.speak = "BOOOOOO"

print(player1.speak())

[].__doc__= 5 
