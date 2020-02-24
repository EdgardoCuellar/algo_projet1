import sys


class Ma_matrice:
    """Classe contenant une matrice sous forme de liste de listes et des méthodes qui performent
    des opérations sur la matrice."""

    def __init__(self, liste):
        """Input: liste de listes contenant la matrice
        Doit contenir la variable self. = liste
        La matrice doit être recentrée lors de l'initialisation de l'objet en utilisant translation_haut_gauche(self)"""
        self.matrice = liste
        self.size = len(liste)

    def colonne(self, col_index):
        """ Input: col_index est un int
        Output = colonne col_index de self.matrice sous forme de liste"""
        col = []
        for pos_y in range(self.size):
            col.append(self.matrice[pos_y][col_index])
        return col

    def rotation_horaire(self):
        """Output = objet de la classe Ma_matrice dont la matrice est la rotation horaire de
        90 degrés de self.matrice. La nouvelle matrice doit également être translatée en haut à
        gauche en utilisant translation_haut_gauche(self).
        Attention, self.matrice reste inchangée."""
        new_m = []
        for pos_x in range(self.size):
            line = []
            for pos_y in range(self.size-1, -1, -1):
                line.append(self.matrice[pos_y][pos_x])
            new_m.append(line)
        return Ma_matrice(new_m)

    def reflexion_axe_horizontal(self):
        """Output = objet de la classe Ma_matrice dont la matrice est la réflexion sur l'axe horiontal
        de self.matrice. La nouvelle matrice doit également être translatée en haut à
        gauche en utilisant translation_haut_gauche(self).
        Attention, self.matrice reste inchangée."""
        new_m = []
        for pos_y in range(self.size - 1, -1, -1):
            new_m.append(self.matrice[pos_y])
        return Ma_matrice(new_m)

    def translation_haut(self, n):
        """Fonction interne qui translate circulairement vers le haut self.matrice par n lignes
        Pas de output"""
        for _ in range(n):
            for pos_y in range(self.size):
                if pos_y != self.size-1:
                    self.matrice[pos_y] = self.matrice[pos_y+1]
                else:
                    self.matrice[pos_y] = [0] * self.size

    def translation_gauche(self, n):
        """Fonction interne qui translate circulairement vers la gauche self.matrice par n colonnes
        Pas de output"""
        for _ in range(n):
            for pos_y in range(self.size):
                for pos_x in range(self.size):
                    if pos_x != self.size-1:
                        self.matrice[pos_y][pos_x] = self.matrice[pos_y][pos_x+1]
                    else:
                        self.matrice[pos_y][pos_x] = 0

    def translation_haut_gauche(self):
        """Fonction interne qui recentre self.matrice de telle manière que ni la première colonne
        ni la première ligne ne contiennent que des 0.
        Cette opération est nécessaire pour ne pas avoir en double certaines variantes d'une pièce
        après rotations/réflexions dans la classe Piece.
        Pas de output"""
        # Translation vers le haut
        nb_up = 0
        s_up = True
        for line in self.matrice:
            if s_up and line == [0]*self.size:
                nb_up += 1
            else:
                s_up = False
        self.translation_haut(nb_up)

        # Translation vers la gauche
        nb_l = 0
        s_l = True
        for pos_x in range(self.size):
            if s_l and self.colonne(pos_x) == [0]*self.size:
                nb_l += 1
            else:
                s_l = False
        self.translation_gauche(nb_l)



class Piece:
    """Classe définissant un polyomino, contenant son nom et la liste de matrices pour
    toutes ses variantes dues à des rotations et réflexions."""

    def __init__(self, nom, variante):
        """ Input: nom = 1 caractère ASCII sous forme de string
                   variante = objet de classe Ma_matrice.
        Toutes ses rotations/réflexions différentes doivent être ajoutées dans la
        liste self.liste_variantes"""
        self.nom = nom
        self.liste_variantes = variante

    def ajout_variante(self, nouvelle_variante):
        """Ajoute l'objet nouvelle_variante de la classe Ma_matrice à la liste self.liste_variantes
        si elle n'y est pas encore.
        Pas de output"""
        if nouvelle_variante not in self.liste_variantes:
            self.liste_variantes.append(nouvelle_variante)


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
        self.hauteur = dimensions[1]
        self.largeur = dimensions[0]
        self.liste_pieces = liste_pieces
        self.tableau = [[" " for _ in range(self.hauteur)] for _ in range(self.largeur)]
        self.Pos_pieces = []
        for i in self.liste_pieces:
            if i not in self.tableau:
                self.Pos_pieces.append([])

    def ajouter_piece(self, index_piece, num_var, pos):
        """Ajoute si possible le polyomino self.liste_pieces[index_piece] à variante liste_variante[num_var]
        dont le coin en haut à gauche de la matrice se trouve à la position pos (= liste de 2 integers) du tableau.
        Tenez en compte le fait que certaines matrices de pièces peuvent contenir des lignes ou colonnes vides en bas ou à droite.
        Si l'ajout est possible, cette méthode modifie les variables:
        - self.Pos_pieces[index_piece] = pos
        - self.tableau[i][j] = nom_piece là où la pièce est placée sur le tableau
        Output = True si la pièce a été ajoutée, False si l'ajout n'était pas possible"""
        test_add = True
        pos_list = []
        for pos_y, line in enumerate(self.liste_pieces[index_piece].liste_variantes.matrice):
            for pos_x, case in enumerate(line):
                if self.tableau[pos_y + pos[1]][pos_x + pos[0]] == " " and case == 1:
                    pos_list.append((pos_x + pos[0], pos_y + pos[1]))
                elif case == 1:
                    test_add = False

        if test_add:
            self.Pos_pieces[index_piece] = pos
            for pos_case in pos_list:
                self.tableau[pos_case[1]][pos_case[0]] = self.liste_pieces[index_piece].nom

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
    str_file = []
    with open(nom_fichier + '.poly', 'r') as file:
        str_file = file.read().split("\n")


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
    nom_fichier = sys.argv[1]
    # liste_solutions = trouver_liste_solutions(nom_fichier)
    # for tableau in liste_solutions:
    #     tableau.imprimer()
