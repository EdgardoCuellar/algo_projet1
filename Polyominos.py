import sys

class Ma_matrice:
    """Classe contenant une matrice sous forme de liste de listes et des méthodes qui performent
    des opérations sur la matrice."""

    def __init__(self, liste):
        """Input: liste de listes contenant la matrice 
        Doit contenir la variable self.matrice = liste
        La matrice doit être recentrée lors de l'initialisation de l'objet en utilisant translation_haut_gauche(self)"""
        pass

    def colonne(self, col_index):
        """ Input: col_index est un int
        Output = colonne col_index de self.matrice sous forme de liste"""
        pass

    def rotation_horaire(self):
        """Output = objet de la classe Ma_matrice dont la matrice est la rotation horaire de 
        90 degrés de self.matrice. La nouvelle matrice doit également être translatée en haut à 
        gauche en utilisant translation_haut_gauche(self).
        Attention, self.matrice reste inchangée."""
        pass

    def reflexion_axe_horizontal(self):
        """Output = objet de la classe Ma_matrice dont la matrice est la réflexion sur l'axe horiontal  
        de self.matrice. La nouvelle matrice doit également être translatée en haut à 
        gauche en utilisant translation_haut_gauche(self).
        Attention, self.matrice reste inchangée."""
        pass

    def translation_haut(self, n):
        """Fonction interne qui translate circulairement vers le haut self.matrice par n lignes
        Pas de output"""
        pass

    def translation_gauche(self, n):
        """Fonction interne qui translate circulairement vers la gauche self.matrice par n colonnes
        Pas de output"""
        pass

    def translation_haut_gauche(self):
        """Fonction interne qui recentre self.matrice de telle manière que ni la première colonne
        ni la première ligne ne contiennent que des 0. 
        Cette opération est nécessaire pour ne pas avoir en double certaines variantes d'une pièce 
        après rotations/réflexions dans la classe Piece.
        Pas de output"""
        pass


class Piece:
    """Classe définissant un polyomino, contenant son nom et la liste de matrices pour 
    toutes ses variantes dues à des rotations et réflexions."""

    def __init__(self, nom, variante):
        """ Input: nom = 1 caractère ASCII sous forme de string
                   variante = objet de classe Ma_matrice.
        Toutes ses rotations/réflexions différentes doivent être ajoutées dans la
        liste self.liste_variantes"""
        pass

    def ajout_variante(self, nouvelle_variante):
        """Ajoute l'objet nouvelle_variante de la classe Ma_matrice à la liste self.liste_variantes
        si elle n'y est pas encore.
        Pas de output"""
        pass


class Tableau:
    """Classe définissant un tableau"""

    def __init__(self, dimensions, liste_pieces):
        """Input: dimensions = tuple de 2 integers contenant la hauteur = dimensions[0] et la largeur du tableau = dimensions[1]
                  liste_pieces = liste d'objets de la classe piece
            Les variables suivantes doivent être contenues dans la classe:
            - liste_pieces
            - hauteur = hauteur du tableau
            - largeur = largeur du tableau
            - tableau = matrice sous forme de liste de listes de strings de longueur 1.
            Lorsque le tableau est initialisé, il est vide et ne contient que des espaces. 
            - Pos_pieces = liste de même longueur que liste_pieces. 
            Si pièce i n'est pas placée sur le tableau, Pos_pieces[i] = []
            Si pièce i est placée sur le tableau, Pos_pieces[i] = [x,y] où x et y sont les coordonnées 
            sur le tableau du coin en haut à gauche de la sous matrice de la variante ajoutée de la pièce
            """

    def ajouter_piece(self, index_piece, num_var, pos):
        """Ajoute si possible le polyomino self.liste_pieces[index_piece] à variante liste_variante[num_var]
        dont le coin en haut à gauche de la matrice se trouve à la position pos (= liste de 2 integers) du tableau.
        Tenez en compte le fait que certaines matrices de pièces peuvent contenir des lignes ou colonnes vides en bas ou à droite. 
        Si l'ajout est possible, cette méthode modifie les variables:
        - self.Pos_pieces[index_piece] = pos
        - self.tableau[i][j] = nom_piece là où la pièce est placée sur le tableau 
        Output = True si la pièce a été ajoutée, False si l'ajout n'était pas possible"""
        pass

    def enlever_piece(self, index_piece):
        """Enlève la pièce à la position index_piece dans self.liste_piece du tableau. 
        Cette méthode modifie les variables:
        - self.Pos_pieces[index_piece] = [] 
        - self.tableau[i][j] = " " là où était la pièce
        Si la pièce n'est pas sur le tableau, cette fonction ne fait rien.
        Pas de output"""
        pass

    def imprimer(self):
        """Imprime le tableau
        Pas de output"""
        print(" " + "-" * self.largeur + " ")
        for i in range(self.hauteur):
            content = ''
            for j in range(self.largeur):
                content += self.tableau[i][j]
            print("|" + content + "|")
        print(" " + "-" * self.largeur + " ")

    def backtracking(self, profondeur):
        """Fonction de backtracking qui essaie de placer les pièces sur le tableau
        profondeur est un integer qui indique la profondeur dans le backtracking qui dans ce cas 
        correspond à l'index de la pièce à ajouter à ce niveau du backtracking
        Output = True si une solution trouvée"""
        pass


def lire_fichier(nom_fichier):
    """ Input = string étant le nom du fichier
    Output = liste d'objets de classe Piece représentant les polyominos 
    contenus dans le fichier"""
    pass

def taille_totale_pieces(liste_pieces):
    """ Input = liste d'objet de classe Piece
    Output = somme de la taille de chaque pièce"""
    pass


def possibles_factorisations(nb):
    """Input: nb est un int
    Output = liste de tuples de taille 2 contenant toutes les factorisations possibles en 
    2 facteurs de nb. Attention à ne pas les répéter 2 fois."""
    pass


def trouver_liste_solutions(nom_fichier):
    """Fonction principale qui trouve la liste des solutions.
    Output = liste d'objets de la classe Tableau qui contiennent les différentes solutions"""
    pass

if __name__ == '__main__':
    pass
    # nom_fichier = sys.argv[1]
    # liste_solutions = trouver_liste_solutions(nom_fichier)
    # for tableau in liste_solutions:
    #     tableau.imprimer()
