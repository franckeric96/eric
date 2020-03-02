class GestionMoyenne:

    def __init__(self, moymin):
        self.moymin = moymin

    def ismean(self, moy):
        if moy >= self.moymin:
            return True
        else:
            return False

    def calculmean(self, notes):
        nbre_notes = len(notes)
        somme = 0

        for item in notes:
            somme += item

        if nbre_notes > 0:
            moyenne = somme/nbre_notes

        else:
            moyenne = 0
        return moyenne
