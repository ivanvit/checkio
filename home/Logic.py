class LogicGate():
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter pinA input for gate " + self.getLabel() + "---->"))

    def getPinB(self):
        return int(input("Enter pinB input for gate " + self.getLabel() + "---->"))


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(self, n)
        self.pin = None

    def getPin(self):
        return int(input("Enter pin input for gate " + self.getLabel() + "---->"))
