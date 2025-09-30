class Animal:
    def __init__(self, name, lenArms, lenLegs, numEyes, hasTail, hasFur):
        self.name = name
        self.lenArms = lenArms
        self.lenLegs = lenLegs
        self.numEyes = numEyes
        self.hasTail = hasTail
        self.hasFur = hasFur

    def __str__(self):
        """ print(f"A {self.name}'s arms are {self.lenArms} inches long.")
        print(f"A {self.name}'s legs are {self.lenLegs} inches long.")
        print(f"A {self.name} has {self.numEyes} eyes.")
        print(f"A {self.name} ")
        print("has") if (self.hasTail) else print("does not have")
        print(" a tail.")
        print(f"A {self.name} ")
        print("has") if (self.hasFur) else print("does not have")
        print(" fur.") """

        tailStr = f"A {self.name} has a tail." if self.hasTail else f"A {self.name} does not have a tail."
        furStr = f"A {self.name} has fur." if self.hasTail else f"A {self.name} does not have fur."

        return f"""
        A {self.name}'s arms are {self.lenArms} inches long.
        A {self.name}'s arms are {self.lenArms} inches long.
        A {self.name} has {self.numEyes} eyes."
        {tailStr}
        {furStr}
        """

snake = Animal("snake", 0, 0, 2, True, False)
print(snake)