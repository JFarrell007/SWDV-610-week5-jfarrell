"""
Name: Jim Farrell
Description:Research perfect has functions.
Using a list of names (classmates, family, etc. generate the hash values using the perfect hash algorithm.
"""

class hashElement:
    def __init__(self, key, name):
        self.key = key
        self.name = name
    def getKey(self):
        return self.key
    def getName(self):
        return self.name
        
class perfectHash:
    
    def __init__(self, size):
        self.size = size
        self.nameDict = [None] * self.size
        
    def generateHash(self, name):
        total = sum(map(ord,name))
        hash = total % self.size
        return hash
        
    def addElement(self, name):
        element = hashElement(self.generateHash(name), name)
        self.nameDict[element.getKey()] = element.getName()
        
    def getElement(self, name):
        return self.nameDict[self.generateHash(name)]      
    
    
def main():
    names = ('Sneezy','Sleepy','Dopey','Doc','Happy','Bashful','Grumpy')
    PH = perfectHash(11)
    for name in names:
        PH.addElement(name)
        
    print("{0:30}{1}".format("NAME", "HASH VALUE"))
    for name in names:
        print("{0:20}{1:16}".format(PH.getElement(name), PH.generateHash(name)))
       

    
main()
