class MealyError(Exception):
    pass


class Mealy:
    st = "A"

    def spawn(this):
        if this.st == "A":
            this.st = "B"
            return 0
        elif this.st == "D":
            this.st = "E"
            return 3
        elif this.st == "F":
            this.st = "B"
            return 7
        else:
            raise MealyError("spawn")

    def jump(this):
        if this.st == "B":
            this.st = "C"
            return 1
        elif this.st == "E":
            this.st = "F"
            return 5
        elif this.st == "F":
            this.st = "A"
            return 6
        else:
            raise MealyError("jump")

    def pan(this):
        if this.st == "C":
            this.st = "D"
            return 2
        elif this.st == "D":
            this.st = "B"
            return 4
        elif this.st == "F":
            this.st = "D"
            return 8
        else:
            raise MealyError("pan")


def main():
    return Mealy()


def raises(func, error):
    try:
        func()
    except Exception as e:
        assert type(e) == error


def test():
    o = main()
    assert o.st == "A"
    assert o.spawn() == 0
    assert o.st == "B"
    raises(lambda: o.spawn(), MealyError)
    assert o.jump() == 1
    assert o.st == "C"
    assert o.pan() == 2
    assert o.st == "D"
    assert o.pan() == 4
    assert o.st == "B"
    assert o.jump() == 1
    assert o.st == "C"
    assert o.pan() == 2
    assert o.st == "D"
    raises(lambda: o.jump(), MealyError)
    assert o.spawn() == 3
    assert o.st == "E"
    assert o.jump() == 5
    assert o.st == "F"
    assert o.spawn() == 7
    assert o.st == "B"
    assert o.jump() == 1
    assert o.st == "C"
    assert o.pan() == 2
    assert o.st == "D"
    assert o.spawn() == 3
    assert o.st == "E"
    assert o.jump() == 5
    assert o.st == "F"
    assert o.pan() == 8
    assert o.st == "D"
    assert o.spawn() == 3
    assert o.st == "E"
    assert o.jump() == 5
    assert o.st == "F"
    assert o.jump() == 6
    raises(lambda: o.pan(), MealyError)
    
    


print(test())
