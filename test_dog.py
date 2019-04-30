from dog import *

ballan = Dog("Ballan", 6)


class TestDogDescription:
    def test_description(self):
        assert ballan.description() == 'Ballan is 6 years old'
