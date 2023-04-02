import sys
import re
import math

class Calculator:
    """A quadratic function calculator"""
    def __init__(self, file):
        with open(file) as file:
            self.expressions = [line.rstrip() for line in file]
        self.coefs = [self.retrieveCoefs(exp) for exp in self.expressions]
        self.extremes = [self.calculateExtreme(coefArr) for coefArr in self.coefs]

    def getExpressions(self):
        for line in self.expressions:
            print(line)

    def getCoefs(self):
        for coefs in self.coefs:
            print(coefs)

    def getExtremes(self):
        for extreme in self.extremes:
            print(extreme)

    def retrieveCoefs(self, exp):
        coef = [0, 0, 0]

        # find a
        expArr = re.split("x\^2", exp)
        coef[0] = self.retrieveLeadingCoef(expArr)

        # find b and c
        exp = expArr[-1]
        expArr = re.split("x", exp)
        if len(expArr) == 2:
            coef[1] = self.retrieveLeadingCoef(expArr)
        coef[2] = self.retrieveConstantCoef(expArr[-1])

        return coef

    def retrieveLeadingCoef(self, expArr):
        if expArr[0] == '' or expArr[0] == "+":
            return 1
        elif expArr[0] == '-':
            return -1
        else:
            return int(expArr[0])

    def retrieveConstantCoef(self, exp):
        return 0 if exp == '' else int(exp)

    def calculateExtreme(self, coefArr):
        [a, b, c] = coefArr
        numerator = 4 * a * c - b ** 2
        denominator = 4 * a
        extreme = self.fractionDivision(numerator, denominator)
        axisOfSymmetry = self.fractionDivision(-b, 2*a)
        return f"({axisOfSymmetry}, {extreme})"

    def fractionDivision(self, a, b):
        if a == 0:
            return "0"
        if b == 0:
            return "math error: denominator cannot be 0"

        gcd = math.gcd(a, b)
        sign = ""
        if a * b < 0:
            sign = "-"
        a = abs(a // gcd)
        b = abs(b // gcd)
        if b == 1:
            return f"{sign}{a}"
        return f"{sign}{a}/{b}"


def main():
    calculator = Calculator(sys.argv[2])
    if sys.argv[1] == '-c':
        calculator.getCoefs()
    else:
        calculator.getExtremes()

if __name__ == "__main__":
    main()
