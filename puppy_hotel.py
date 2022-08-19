
"""
Puppy hotel object oriented design exercise:

Hotel can hold small, medium, big puppies
Insertion in O(1)
check_out in O(1)

"""
from enum import IntEnum

class Size(IntEnum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3

class Room:
    def __init__(self,id,size):
        self.id = id
        self.occupant=None
        self.size = size
    def __repr__(self):
        return(f"Room {self.id}, {Size(self.size).name}, occupant: ({self.occupant})")
    def set_occupant(self,occupant):
        if not occupant:
            return
        if occupant.size > self.size:
            raise ValueError(f"Occupant size {occupant.size} is greater than room size {self.size}")
        self.occupant = occupant
    def get_occupant(self):
        return self.occupant
    def check_out(self):
        self.occupant = None

class Hotel:
    def __init__(self,id):
        self.id = id
        self.rooms = {
            Size.SMALL: {
                "vacant": dict(),
                "occupied": dict(),
            },
            Size.MEDIUM: {
                "vacant": dict(),
                "occupied": dict(),
            },
            Size.BIG: {
                "vacant": dict(),
                "occupied": dict(),
            }
        }
        self.guests = dict()
    def __repr__(self):
        out = f"Hotel {self.id}"
        for size in self.rooms:
            out+=f"\n{Size(size).name}"
            for status in self.rooms[size]:
                out += f"\n\t{status} : "
                for room in self.rooms[size][status]:
                    out += f"\n\t\t{self.rooms[size][status][room]}"

        return out

    def add_room(self,room_id,size):
        self.rooms[size]["vacant"][room_id] = (Room(room_id,size))
        return room_id

    def check_in(self,guest):
        size = guest.size
        while size <= max(Size):
            print("CHECKING SIZE", size, max(Size))
            if not self._is_vacant(size):
                print(size,self._is_vacant(size))
                size +=1
            else:
                room_id,room = self.rooms[size]["vacant"].popitem()
                
                room.set_occupant(guest)
                print("SETTING OCCUPANT FOR ",room)
                self.rooms[size]["occupied"][room_id]=room

                self.guests[guest.name] = room
                print(f"ADDED {guest.name} to {room_id}")
                return room_id
        raise ValueError(f"No vacancy for {Size(guest.size).name}")

    def check_out(self,guest_name):
        room = self.guests[guest_name]
        room.check_out()
        del self.rooms[room.size]["occupied"][room.id] 
        self.rooms[room.size]["vacant"][room.id] = room

        return guest_name

    def _is_vacant(self,size):
        return len(self.rooms[size]["vacant"]) > 0

class Puppy:
    def __init__(self,size: int,name):
        self._size = size
        self.name = name
    
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
    def __repr__(self):
        return f"{self.name}, size {Size(self._size).name}"

if __name__ == "__main__":
    
    hotel = Hotel(1)
    
    size = Size.SMALL
    for i in range(10):

        hotel.add_room(i,size)
        if i >0 and i%3 == 0 and size < max(Size):
            size +=1
    print(hotel)
    puppy = Puppy(Size.SMALL,"BOB")
    for i in range(8):
        hotel.check_in(Puppy(Size.SMALL,f"gerald_{i}"))
        
        print(i)
    print(hotel)
    print(hotel.guests)
    hotel.check_out("gerald_0")
    print(hotel)
    hotel.check_in(Puppy(Size.BIG,f"BIGLY"))
    print(hotel)