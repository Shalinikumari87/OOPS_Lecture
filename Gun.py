"""
Write a class of Gun which has bullets which is fixed of size 100 , it should have a scope , 
laser , level 


you have to create 3 objects of this class 
AKM -> level = 1 , scope = 2 , laser = 1
M416  -> level = 2 , scope = 3 , laser = 1
Sniper -> level = 3 , scope = 4 , laser = 7

finally print all the details of each gun
"""


class Gun:
    def __init__(self,brand,level,scope,laser):
        self.brand = brand
        self.level = level
        self.scope = scope
        self.laser = laser
        self.bullet_size = 100
        print("brand of Gun",level,scope and laser)

    def display(self):
        print(self.brand,self.bullet_size)

G1 = Gun("AKM",1,2,1)
G1.display()
print(G1.brand,G1.level,G1.scope,G1.laser,G1.bullet_size)
G2 = Gun("M416",2,3,1)
print(G2.brand,G2.level,G2.scope,G2.laser,G2.bullet_size)
G3 = Gun("Sniper",3,4,7)
print(G3.brand,G3.level,G3.scope,G3.laser,G3.bullet_size)