# magic methods or dunders have specialised use and are represented using double unders.


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Hi, I am a vector !"

    def __call__(self) -> str:
        print(f"Yes, i am called, x:{self.x} !")


hitesh = Vector(2, 5)
print(hitesh)  # representing using the __repr__ method
hitesh()  # calling the vector using __call__


### Comparison Magic Methods like eq,ge,le etc


class Word:
    def __init__(self, word: str) -> None:
        word.strip()
        self.word = word

    def __gt__(self, other):
        return len(self.word) > len(other.word)

    def __lt__(self, other):
        return len(self.word) < len(other.word)

    def __ge__(self, other):
        return len(self.word) >= len(other.word)

    def __le__(self, other):
        return len(self.word) <= len(other.word)


str1 = Word("Hitesh")
str2 = Word("Tanya")
