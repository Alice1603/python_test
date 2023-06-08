class MealyError(Exception):
    pass


class Mealy:
    st = "A"

    def turn(this):
        if this.st == "B":
            this.st = "C"
            return 1
        elif this.st == "C":
            this.st = "D"
            return 2
        elif this.st == "G":
            return 9
        else:
            raise MealyError("turn")

    def paste(this):
        if this.st == "C":
            this.st = "G"
            return 3
        elif this.st == "E":
            this.st = "F"
            return 6
        elif this.st == "F":
            this.st = "G"
            return 8
        else:
            raise MealyError("paste")

    def run(this):
        if this.st == "A":
            this.st = "B"
            return 0
        elif this.st == "C":
            this.st = "F"
            return 4
        elif this.st == "D":
            this.st = "E"
            return 5
        elif this.st == "E":
            this.st = "A"
            return 7
        else:
            raise MealyError("run")


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
    raises(lambda: o.paste(), MealyError)
    assert o.run() == 0
    assert o.st == "B"
    assert o.turn() == 1
    assert o.st == "C"
    assert o.turn() == 2
    assert o.st == "D"
    assert o.run() == 5
    assert o.st == "E"
    assert o.run() == 7
    assert o.st == "A"
    assert o.run() == 0
    assert o.st == "B"
    assert o.turn() == 1
    assert o.st == "C"
    assert o.turn() == 2
    assert o.st == "D"
    assert o.run() == 5
    assert o.st == "E"
    raises(lambda: o.turn(), MealyError)
    assert o.paste() == 6
    assert o.st == "F"
    assert o.paste() == 8
    assert o.st == "G"
    assert o.turn() == 9
    assert o.st == "G"
    o.st = "C"
    assert o.run() == 4
    assert o.st == "F"
    assert o.paste() == 8
    assert o.st == "G"
    o.st = "C"
    assert o.paste() == 3
    assert o.st == "G"
    raises(lambda: o.run(), MealyError)
    
    


print(test())
