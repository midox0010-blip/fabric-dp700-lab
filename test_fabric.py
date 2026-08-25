def calcul_total(prix, quantite):
    return prix * quantite


def test_calcul_total():
    assert calcul_total(100, 3) == 300
