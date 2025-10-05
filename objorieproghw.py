class dog:

    species="dog"

    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed

Bolt=dog("Bolt",6,"Beagle")
Masha=dog("Masha",8,"Labrador")

print("Bolt is a {}".format(Bolt.species))
print("Masha is also a {}".format(Masha.species))

print("{} is {} years old and is a {}".format(Bolt.name,Bolt.age,Bolt.breed))
print("{} is {} years old and is a {}".format(Masha.name,Masha.age,Masha.breed))