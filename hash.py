"""
Name: Jim Farrell
Description:Research perfect has functions.
Using a list of names (classmates, family, etc. generate the hash values using the perfect hash algorithm.
"""
from full_error import *

class hashElement:
    """element to store key and name"""
    def __init__(self, key, name):
        self.key = key
        self.name = name
    def getKey(self):
        return self.key
    def getName(self):
        return self.name
        
class perfectHash:
    """contains methods to create perfect hash number for specific set of names"""
    
    def __init__(self, size):
        self.size = size
        #create hashElement list and initialize each element to None
        self.hashElements = [None] * self.size
        self.collisions = 0 #counter for collisions
        self.elementCount = 0
    
    def getCollisions(self):
        """return collision count"""
        return self.collisions
    
    def getTableSize(self):
        """return list size"""
        return self.size
    
    def genKey(self,name):
        """method sum the ordinal values of string"""
        key = sum(map(ord,name))
        return key
        
    def generateHash(self, name):
        """method that uses modulus operator to generate hash that is less than size of list"""
        key = sum(map(ord,name))
        hash = key % self.size
        #If the hash has been used perform a rehash to get new hash number
        if self.hashElements[hash] != None:
            #make sure user doens't try to insert more names than allowed
            if self.elementCount >= self.size:
                try:
                    #raise exception when trying to add elements to a full list
                    raise FullError("No slots left cannot add {}".format(name))
                #catch the error and print a message
                except FullError as err:
                    print("generateHash error perfectHash: ", err)  
                exit()                
            hash = self.rehash(key)
            self.collisions += 1 #increment collions since hash had been used
        return hash,key
    
    def rehash(self, key):
        """methond to rehash new number"""
        searching = True
        while searching:
            key += 1 #increment the key value
            newhash = (key) % self.size #perform modulus operation to get newhash
            #If you find an empty slot None set searching to false
            if self.hashElements[newhash] == None: 
                searching = False
        return newhash       
        
    def addElement(self, name):
        """method to add element to list"""
        tHash, key = self.generateHash(name)
        element = hashElement(key, name)
        self.hashElements[tHash] = element
        self.elementCount += 1
        return key, tHash
        
    def getElement(self, name):
        """method to return name"""
        searching = True
        
        key = self.genKey(name)
        hash = (key) % self.size
        if self.hashElements[hash].getName() == name:
            return self.hashElements[hash].getName()
        else:
            while searching:
                key += 1
                newhash = (key) % self.size
                if self.hashElements[newhash].getName() == name:
                    searching = False
        return self.hashElements[newhash].getName()
    
    
def testIt():
    names = ('Sneezy','Sleepy','Dopey','Doc','Happy','Bashful','Grumpy')
    hashSmall = perfectHash(7)
    hashLarge = perfectHash(11)
        
    print("{0:20}{1:10}{2:20}{3}".format("NAME", "KEY", "Hash modulus 7", "Hash modulus 11"))
    for name in names:
        sKey,sHash = hashSmall.addElement(name)
        lKey,lHash = hashLarge.addElement(name)
        print("{0:20}{1:3}{2:16}{3:16}".format(name, sKey, sHash, lHash))  
        
    print("When inserting {0} items into a {1} element table there were {2} collisions".format(len(names),
    hashSmall.getTableSize(), hashSmall.getCollisions()))
    
    print("When inserting {0} items into a {1} element table there were {2} collisions".format(len(names),
    hashLarge.getTableSize(), hashLarge.getCollisions()))
    
    #for name in names:
        #print(hashSmall.getElement(name))
    
testIt()
