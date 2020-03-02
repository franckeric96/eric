
from mypackage.nanmoyenne import GestionMoyenne

gestion = GestionMoyenne(16)


students = [
    {
        'nom': "soro",
        'notes': [10, 16]
    },
    {
        'nom': "Koffi",
        'notes': [12, 14]
    }

]

for student in students:
    notes = student['notes']
    print(notes)
    moyenne = gestion.calculmean(notes)
    print(moyenne)
    if gestion.ismean(moyenne):
        print(student['nom'], " super vous avez la moyenne")
    else:
        print(student['nom'], " oups!!! vous n'avez pas la moyenne")
