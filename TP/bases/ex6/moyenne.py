#!/usr/bin/env python

note_maths = (17, 9)

note_physique = (15, 6)

note_histoire_ancienne_info = (4, 1)

resultat = (
    note_maths[0]*note_maths[1] + 
    note_physique[0]*note_physique[1] + 
    note_histoire_ancienne_info[0]*note_histoire_ancienne_info[1]) / (
        note_maths[1] + note_physique[1] + note_histoire_ancienne_info[1]
    )

print(resultat)

# tuples are immutable
# note_histoire_ancienne_info[1] = 5 