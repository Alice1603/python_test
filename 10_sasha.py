class MealyError(Exception):
    pass


class Mealy:
    st = "A"

    def paste(this):
        if this.st == "A":
            this.st = "B"
            return 0
        elif this.st == "F":
            this.st = "G"
            return 8
        elif this.st == "G":
            this.st = "H"
            return 10
        else:
            raise MealyError("paste")
    
    def scan(this):
        if this.st == "B":
            this.st = "C"
            return 1
        elif this.st == "C":
            this.st = "D"
            return 3
        elif this.st == "D":
            this.st = "A"
            return 5
        elif this.st == "F":
            this.st = "B"
            return 9
        else:
            raise MealyError("scan")
        
    def start(this):
        if this.st == "B":
            this.st = "H"
            return 2
        elif this.st == "D":
            this.st = "F"
            return 6
        elif this.st == "H":
            this.st = "C"
            return 11
        else:
            raise MealyError("start")

    def swap(this):
        if this.st == "D":
            this.st = "E"
            return 4
        elif this.st == "E":
            this.st = "F"
            return 7
        else:
            raise MealyError("swap")


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
    raises(lambda: o.scan(), MealyError)
    raises(lambda: o.start(), MealyError)
    assert o.paste() == 0
    raises(lambda: o.paste(), MealyError)
    raises(lambda: o.swap(), MealyError)
    assert o.st == "B"
    assert o.scan() == 1
    assert o.st == "C"
    assert o.scan() == 3
    assert o.st == "D"
    assert o.swap() == 4
    assert o.st == "E"
    assert o.swap() == 7
    assert o.st == "F"
    assert o.paste() == 8
    assert o.st == "G"
    assert o.paste() == 10
    assert o.st == "H"
    assert o.start() == 11
    assert o.st == "C"
    o.st = "D"
    assert o.start() == 6
    assert o.st == "F"
    assert o.scan() == 9
    assert o.st == "B"
    assert o.start() == 2
    assert o.st == "H"
    o.st = "D"
    assert o.scan() == 5
    assert o.st == "A"



    
