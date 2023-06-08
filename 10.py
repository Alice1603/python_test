class MealyError(Exception):
    pass


class Mealy:
    st = "A"

    def join(this):
        if this.st == "A":
            this.st = "B"
            return 0
        elif this.st == "B":
            this.st = "C"
            return 2
        elif this.st == "C":
            this.st = "D"
            return 4
        elif this.st == "D":
            this.st = "E"
            return 5
        else:
            raise MealyError("join")

    def mix(this):
        if this.st == "A":
            this.st = "E"
            return 1
        elif this.st == "E":
            this.st = "B"
            return 8
        else:
            raise MealyError("mix")

    def daub(this):
        if this.st == "B":
            return 3
        elif this.st == "D":
            this.st = "B"
            return 6
        elif this.st == "E":
            this.st = "F"
            return 7
        else:
            raise MealyError("daub")


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
    raises(lambda: o.daub(), MealyError)
    assert o.join() == 0
    assert o.st == "B"
    raises(lambda: o.mix(), MealyError)
    assert o.daub() == 3
    assert o.st == "B"
    assert o.join() == 2
    assert o.st == "C"
    assert o.join() == 4
    assert o.st == "D"
    assert o.daub() == 6
    assert o.st == "B"
    assert o.join() == 2
    assert o.st == "C"
    assert o.join() == 4
    assert o.st == "D"
    assert o.join() == 5
    assert o.st == "E"
    raises(lambda: o.join(), MealyError)
    assert o.daub() == 7
    assert o.st == "F"
    o = Mealy()
    assert o.st == "A"
    assert o.mix() == 1
    assert o.st == "E"
    assert o.mix() == 8
    assert o.st == "B"
    


print(test())
    
