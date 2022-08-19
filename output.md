# Initialize
# ADDED ROOMS TO HOTEL
Hotel 1
SMALL
        vacant :
                Room 0, SMALL, occupant: (None) 
                Room 1, SMALL, occupant: (None) 
                Room 2, SMALL, occupant: (None) 
                Room 3, SMALL, occupant: (None) 
        occupied :
MEDIUM
        vacant :
                Room 4, MEDIUM, occupant: (None)
                Room 5, MEDIUM, occupant: (None)
                Room 6, MEDIUM, occupant: (None)
        occupied :
BIG
        vacant :
                Room 7, BIG, occupant: (None)
                Room 8, BIG, occupant: (None)
                Room 9, BIG, occupant: (None)
        occupied :
# ADD GUESTS
Size.SMALL False
Size.SMALL False
Size.SMALL False
Size.SMALL False
2 False
Hotel 1
SMALL
        vacant :
        occupied :
                Room 3, SMALL, occupant: (gerald_0, size SMALL)
                Room 2, SMALL, occupant: (gerald_1, size SMALL)
                Room 1, SMALL, occupant: (gerald_2, size SMALL)
                Room 0, SMALL, occupant: (gerald_3, size SMALL)
MEDIUM
        vacant :
        occupied :
                Room 6, MEDIUM, occupant: (gerald_4, size SMALL)
                Room 5, MEDIUM, occupant: (gerald_5, size SMALL)
                Room 4, MEDIUM, occupant: (gerald_6, size SMALL)
BIG
        vacant :
                Room 7, BIG, occupant: (None)
                Room 8, BIG, occupant: (None)
        occupied :
                Room 9, BIG, occupant: (gerald_7, size SMALL)
# GUESTS ROSTER:
gerald_0 : Room 3, SMALL, occupant: (gerald_0, size SMALL)
gerald_1 : Room 2, SMALL, occupant: (gerald_1, size SMALL)
gerald_2 : Room 1, SMALL, occupant: (gerald_2, size SMALL)
gerald_3 : Room 0, SMALL, occupant: (gerald_3, size SMALL)
gerald_4 : Room 6, MEDIUM, occupant: (gerald_4, size SMALL)
gerald_5 : Room 5, MEDIUM, occupant: (gerald_5, size SMALL)
gerald_6 : Room 4, MEDIUM, occupant: (gerald_6, size SMALL)
gerald_7 : Room 9, BIG, occupant: (gerald_7, size SMALL)
# CHECKOUT:
Hotel 1
SMALL
        vacant :
                Room 3, SMALL, occupant: (None)
        occupied :
                Room 2, SMALL, occupant: (gerald_1, size SMALL)
                Room 1, SMALL, occupant: (gerald_2, size SMALL)
                Room 0, SMALL, occupant: (gerald_3, size SMALL)
MEDIUM
        vacant :
        occupied :
                Room 6, MEDIUM, occupant: (gerald_4, size SMALL)
                Room 5, MEDIUM, occupant: (gerald_5, size SMALL)
                Room 4, MEDIUM, occupant: (gerald_6, size SMALL)
BIG
        vacant :
                Room 7, BIG, occupant: (None)
                Room 8, BIG, occupant: (None)
        occupied :
                Room 9, BIG, occupant: (gerald_7, size SMALL)
# CHECK IN LARGER GUEST:
Hotel 1
SMALL
        vacant :
                Room 3, SMALL, occupant: (None)
        occupied :
                Room 2, SMALL, occupant: (gerald_1, size SMALL)
                Room 1, SMALL, occupant: (gerald_2, size SMALL)
                Room 0, SMALL, occupant: (gerald_3, size SMALL)
MEDIUM
        vacant :
        occupied :
                Room 6, MEDIUM, occupant: (gerald_4, size SMALL)
                Room 5, MEDIUM, occupant: (gerald_5, size SMALL)
                Room 4, MEDIUM, occupant: (gerald_6, size SMALL)
BIG
        vacant :
                Room 7, BIG, occupant: (None)
        occupied :
                Room 9, BIG, occupant: (gerald_7, size SMALL)
                Room 8, BIG, occupant: (BIGLY, size BIG)