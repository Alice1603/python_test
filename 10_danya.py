class MealyError(Exception):
    pass


class Mealy:
    st = "A"

    def stand(this):
        if this.st == "A":
            this.st = "B"
            return 0
        elif this.st == "E":
            this.st = "C"
            return 5
        elif this.st == "F":
            this.st = "A"
            return 9
        else:
            raise MealyError("stand")

    def bend(this):
        if this.st == "B":
            this.st = "C"
            return 1
        elif this.st == "D":
            this.st = "E"
            return 3
        elif this.st == "E":
            this.st = "G"
            return 7
        else:
            raise MealyError("bend")

    def peep(this):
        if this.st == "C":
            this.st = "D"
            return 2
        elif this.st == "E":
            this.st = "F"
            return 4
        elif this.st == "F":
            this.st = "G"
            return 8
        else:
            raise MealyError("peep")
    
    def melt(this):
        if this.st == "E":
            this.st = "A"
            return 6
        else:
            raise MealyError("melt")


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
    raises(lambda: o.bend(), MealyError)
    assert o.stand() == 0
    assert o.st == "B"
    raises(lambda: o.melt(), MealyError)
    raises(lambda: o.stand(), MealyError)
    raises(lambda: o.peep(), MealyError)
    assert o.bend() == 1
    assert o.st == "C"
    assert o.peep() == 2
    assert o.st == "D"
    assert o.bend() == 3
    assert o.st == "E"
    assert o.peep() == 4
    assert o.st == "F"
    assert o.peep() == 8
    assert o.st == "G"
    o.st = "E"
    assert o.stand() == 5
    assert o.st == "C"
    o.st = "E"
    assert o.melt() == 6
    assert o.st == "A"
    o.st = "E"
    assert o.bend() == 7
    assert o.st == "G"
    o.st = "F"
    assert o.stand() == 9
    assert o.st == "A"
