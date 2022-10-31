class Polynome:
    """ Representation d'un polynome a coefficients reels """

    def __init__(self, liste_des_coef=[0]):
        """" Initialisation des coefficients du polynome """
        self.coeffs = liste_des_coef

    def deg(self):
        """ Calcul du degre du polynome """
        return len(self.coeffs) - 1

    def valeur(self, x):
        """ Retourne la valeur de l'expression P(x)"""
        Val = self.coeffs[0]
        Puissance = 1
        for p in range(1, len(self.coeffs)):
            Puissance *= x
            Val += self.coeffs[p] * Puissance
        return Val

    def __str__(self):
        """Convertit le polynome en chaine pour l'affichage"""
        expr = str(self.coeffs[0])
        for i in range(1,len(self.coeffs)):
            expr += '+'+str(self.coeffs[i])+'X'+str(i)
        return expr

test = Polynome([0, 1, 2])
print(test.valeur(2))
print(test)
print(test.deg())
