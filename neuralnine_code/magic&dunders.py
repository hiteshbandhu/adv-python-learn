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
