class HashTable:
    def __init__(self):
        self.size = 11 # must be a prime number
        self.slots = [None]*self.size
        self.data = [None]*self.size
    
    # this is the import part
    def hashfunction(self,key,size):
        return key%size
        
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def put(self,key,data):
        hv= self.hashfunction(key,len(self.slots))
        if self.slots[hv] == None:
            self.slots[hv] = key
            self.data[hv] = data
        else: # collision
            if self.slots[hv] == key:
                self.data[hv] = data #update existing key value pair
            else: # insert key to next available slot
                # look for an available slot
                nextslot = self.rehash(hv,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                    
                # find an available slot,empty or existing
                if self.slots[nextslot] == None: #insert here
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else: # replace old data
                    self.data[nextslot] = data
    def get(self,key):
        hv = self.hashfunction(key,len(self.slots))
        startpos = hv 
        data = None
        
        while self.slots[hv] != None:
            
            if self.slots[hv] == key: # found
                data = self.data[hv]
                break
            else:
                # scan next possible position
                hv = self.rehash(hv,len(self.slots))
                # break the loop when all possible positions have been visited
                if hv == startpos:
                    break
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        return self.put(key,data)
                    
if __name__ == "__main__":
    h = HashTable()
    h[113] = "cat"
    h[117] = "mouse"
    h[97] = "cow"
    h[100] = "bird"
    h[114] = "hawk"
    h[108] = "sheep"
    h[116] = "pig"
    h[105] = "chick"
    h[99] = "snake"
    print h[99]
