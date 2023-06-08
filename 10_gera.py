class MealyError(Exception):
    pass


class Mealy:
    st = "A"

    def tag(this):
        if this.st == "A":
            this.st = "B"
            return 0
        elif this.st == "C":
            this.st = "D"
            return 2
        elif this.st == "E":
            this.st = "F"
            return 6
        elif this.st == "F":
            this.st = "F"
            return 7
        else:
            raise MealyError("tag")

    def trash(this):
        if this.st == "B":
            this.st = "C"
            return 1
        elif this.st == "C":
            this.st = "C"
            return 3
        elif this.st == "D":
            this.st = "B"
            return 5
        elif this.st == "F":
            this.st = "D"
            return 8
        else:
            raise MealyError("trash")

    def slog(this):
        if this.st == "D":
            this.st = "E"
            return 4
        else:
            raise MealyError("slog")


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
    raises(lambda: o.trash(), MealyError)
    assert o.tag() == 0
    assert o.st == "B"
    raises(lambda: o.tag(), MealyError)
    raises(lambda: o.slog(), MealyError)
    assert o.trash() == 1
    assert o.st == "C"
    assert o.trash() == 3
    assert o.st == "C"
    assert o.tag() == 2
    assert o.st == "D"
    assert o.slog() == 4
    assert o.st == "E"
    assert o.tag() == 6
    assert o.st == "F"
    assert o.tag() == 7
    assert o.st == "F"
    assert o.trash() == 8
    assert o.st == "D"
    assert o.trash() == 5
    assert o.st == "B"
