# import sys
# import timeit
#
# class Ma_matrice:
#     """Classe contenant une matrice sous forme de liste de listes et des méthodes qui performent
#     des opérations sur la matrice."""
#
#     def __init__(self, liste):
#         """Input: liste de listes contenant la matrice
#         Doit contenir la variable self. = liste
#         La matrice doit être recentrée lors de l'initialisation de l'objet en utilisant translation_haut_gauche(self)"""
#         self.matrice = liste
#         self.size = len(liste)
#         self.translation_haut_gauche()
#
#     def colonne(self, col_index):
#         """ Input: col_index est un int
#         Output = colonne col_index de self.matrice sous forme de liste"""
#         col = []
#         for pos_y in range(self.size):
#             col.append(self.matrice[pos_y][col_index])
#         return col
#
#     def rotation_horaire(self):
#         """Output = objet de la classe Ma_matrice dont la matrice est la rotation horaire de
#         90 degrés de self.matrice. La nouvelle matrice doit également être translatée en haut à
#         gauche en utilisant translation_haut_gauche(self).
#         Attention, self.matrice reste inchangée."""
#         new_m = []
#         for pos_x in range(self.size):
#             line = []
#             for pos_y in range(self.size - 1, -1, -1):
#                 line.append(self.matrice[pos_y][pos_x])
#             new_m.append(line)
#         return Ma_matrice(new_m)
#
#     def reflexion_axe_horizontal(self):
#         """Output = objet de la classe Ma_matrice dont la matrice est la réflexion sur l'axe horiontal
#         de self.matrice. La nouvelle matrice doit également être translatée en haut à
#         gauche en utilisant translation_haut_gauche(self).
#         Attention, self.matrice reste inchangée."""
#         new_m = []
#         for pos_y in range(self.size - 1, -1, -1):
#             new_m.append(self.matrice[pos_y])
#         return Ma_matrice(new_m)
#
#     def translation_haut(self, n):
#         """Fonction interne qui translate circulairement vers le haut self.matrice par n lignes
#         Pas de output"""
#         for _ in range(n):
#             for pos_y in range(self.size):
#                 if pos_y != self.size - 1:
#                     self.matrice[pos_y] = self.matrice[pos_y + 1]
#                 else:
#                     self.matrice[pos_y] = [0] * self.size
#
#     def translation_gauche(self, n):
#         """Fonction interne qui translate circulairement vers la gauche self.matrice par n colonnes
#         Pas de output"""
#         for _ in range(n):
#             for pos_y in range(self.size):
#                 for pos_x in range(self.size):
#                     if pos_x != self.size - 1:
#                         self.matrice[pos_y][pos_x] = self.matrice[pos_y][pos_x + 1]
#                     else:
#                         self.matrice[pos_y][pos_x] = 0
#
#     def translation_haut_gauche(self):
#         """Fonction interne qui recentre self.matrice de telle manière que ni la première colonne
#         ni la première ligne ne contiennent que des 0.
#         Cette opération est nécessaire pour ne pas avoir en double certaines variantes d'une pièce
#         après rotations/réflexions dans la classe Piece.
#         Pas de output"""
#         # Translation vers le haut
#         nb_up = 0
#         s_up = True
#         for line in self.matrice:
#             if s_up and line == [0] * self.size:
#                 nb_up += 1
#             else:
#                 s_up = False
#         self.translation_haut(nb_up)
#
#         # Translation vers la gauche
#         nb_l = 0
#         s_l = True
#         for pos_x in range(self.size):
#             if s_l and self.colonne(pos_x) == [0] * self.size:
#                 nb_l += 1
#             else:
#                 s_l = False
#         self.translation_gauche(nb_l)
#
#
# class Piece:
#     """Classe définissant un polyomino, contenant son nom et la liste de matrices pour
#     toutes ses variantes dues à des rotations et réflexions."""
#
#     def __init__(self, nom, variante):
#         """ Input: nom = 1 caractère ASCII sous forme de string
#                    variante = objet de classe Ma_matrice.
#         Toutes ses rotations/réflexions différentes doivent être ajoutées dans la
#         liste self.liste_variantes"""
#         self.nom = nom
#         self.liste_variantes = [variante]
#
#     def ajout_variante(self, nouvelle_variante):
#         """Ajoute l'objet nouvelle_variante de la classe Ma_matrice à la liste self.liste_variantes
#         si elle n'y est pas encore.
#         Pas de output"""
#         nouvelle_variante.translation_haut_gauche()
#         add = True
#         for lt in self.liste_variantes:
#             if lt.matrice == nouvelle_variante.matrice:
#                 add = False
#         if add:
#             self.liste_variantes.append(nouvelle_variante)
#
#     def posibilite(self):
#         rota = self.liste_variantes[0].rotation_horaire()
#         rota2 = Ma_matrice(rota.matrice).rotation_horaire()
#         rota3 = Ma_matrice(rota2.matrice).rotation_horaire()
#         self.ajout_variante(rota)
#         self.ajout_variante(rota2)
#         self.ajout_variante(rota3)
#         for lt in self.liste_variantes:
#             self.ajout_variante(lt.reflexion_axe_horizontal())
#
#
# class Tableau:
#     """Classe définissant un tableau"""
#
#     def __init__(self, dimensions, liste_pieces):
#         """Input: dimensions = tuple de 2 integers contenant la hauteur = dimensions[0] et la largeur du tableau = dimensions[1]
#                   liste_pieces = liste d'objets de la classe piece
#             Les variables suivantes doivent être contenues dans la classe:
#             - liste_pieces
#             - hauteur = hauteur du tableau
#             - largeur = largeur du tableau
#             - tableau = matrice sous forme de liste de listes de strings de longueur 1.
#             Lorsque le tableau est initialisé, il est vide et ne contient que des espaces.
#             - Pos_pieces = liste de même longueur que liste_pieces.
#             Si pièce i n'est pas placée sur le tableau, Pos_pieces[i] = []
#             Si pièce i est placée sur le tableau, Pos_pieces[i] = [x,y] où x et y sont les coordonnées
#             sur le tableau du coin en haut à gauche de la sous matrice de la variante ajoutée de la pièce
#             """
#         self.hauteur = dimensions[0]
#         self.largeur = dimensions[1]
#         self.liste_pieces = liste_pieces
#         self.tableau = [[" " for _ in range(self.largeur)] for _ in range(self.hauteur)]
#         self.Pos_pieces = []
#         for i in self.liste_pieces:
#             if i not in self.tableau:
#                 self.Pos_pieces.append([0, 0])
#
#     def ajouter_piece(self, index_piece, num_var, pos):
#         """Ajoute si possible le polyomino self.liste_pieces[index_piece] à variante liste_variante[num_var]
#         dont le coin en haut à gauche de la matrice se trouve à la position pos 😊 liste de 2 integers) du tableau.
#         Tenez en compte le fait que certaines matrices de pièces peuvent contenir des lignes ou colonnes vides en bas ou à droite.
#         Si l'ajout est possible, cette méthode modifie les variables:
#         - self.Pos_pieces[index_piece] = pos
#         - self.tableau[i][j] = nom_piece là où la pièce est placée sur le tableau
#         Output = True si la pièce a été ajoutée, False si l'ajout n'était pas possible"""
#         test_add = True
#         pos_list = []
#         for pos_y, line in enumerate(self.liste_pieces[index_piece].liste_variantes[num_var].matrice):
#             for pos_x, case in enumerate(line):
#                 if self.hauteur > pos_y + pos[0] and self.largeur > pos_x + pos[1]\
#                         and self.tableau[pos_y + pos[0]][pos_x + pos[1]] == " " and case == 1:
#                     pos_list.append((pos_x + pos[1], pos_y + pos[0]))
#                 elif case == 1:
#                     test_add = False
#
#         if test_add:
#             self.Pos_pieces[index_piece] = pos
#             for pos_case in pos_list:
#                 self.tableau[pos_case[1]][pos_case[0]] = self.liste_pieces[index_piece].nom
#
#         return test_add
#
#     def enlever_piece(self, index_piece):
#         """Enlève la pièce à la position index_piece dans self.liste_piece du tableau.
#         Cette méthode modifie les variables:
#
#         - self.tableau[i][j] = " " là où était la pièce
#         Si la pièce n'est pas sur le tableau, cette fonction ne fait rien.
#         Pas de output"""
#         for pos_y in range(self.hauteur):
#             for pos_x in range(self.largeur):
#                 if self.tableau[pos_y][pos_x] == self.liste_pieces[index_piece].nom:
#                     self.tableau[pos_y][pos_x] = " "
#
#     def imprimer(self):
#         """Imprime le tableau
#         Pas de output"""
#         print(" " + "-" * self.largeur + " ")
#         for i in range(self.hauteur):
#             content = ''
#             for j in range(self.largeur):
#                 content += self.tableau[i][j]
#             print("|" + content + "|")
#         print(" " + "-" * self.largeur + " ")
#
#     def lt_var(self):
#         """
#         yo
#         :return:
#         """
#         lt = []
#         where = []
#         for var in self.liste_pieces:
#             lt.append(len(var.liste_variantes))
#             where.append(0)
#         return lt, where
#
#     def backtracking(self, profondeur):
#         """Fonction de backtracking qui essaie de placer les pièces sur le tableau
#         profondeur est un integer qui indique la profondeur dans le backtracking qui dans ce cas
#         correspond à l'index de la pièce à ajouter à ce niveau du backtracking
#         Output = True si une solution trouvée"""
#         piece = 0
#         max_var, where_var = self.lt_var()
#         while True:
#             if not self.ajouter_piece(piece, where_var[piece], self.Pos_pieces[piece]):
#                 if max_var[piece]-1 > where_var[piece]:
#                     where_var[piece] += 1
#                 else:
#                     where_var[piece] = 0
#                     if self.Pos_pieces[piece][0] < self.hauteur-1:
#                         self.Pos_pieces[piece][0] += 1
#                     else:
#                         self.Pos_pieces[piece][0] = 0
#                         self.Pos_pieces[piece][1] += 1
#
#                     if self.Pos_pieces[piece][1] == self.largeur:
#                         self.Pos_pieces[piece] = [0, 0]
#                         piece -= 1
#                         if piece < 0 or self.Pos_pieces[0][1] == self.largeur:
#                             return False
#                         else:
#                             self.enlever_piece(piece)
#                             if max_var[piece] - 1 > where_var[piece]:
#                                 where_var[piece] += 1
#                             else:
#                                 where_var[piece] = 0
#                                 if self.Pos_pieces[piece][0] < self.hauteur - 1:
#                                     self.Pos_pieces[piece][0] += 1
#                                 else:
#                                     self.Pos_pieces[piece][0] = 0
#                                     self.Pos_pieces[piece][1] += 1
#             else:
#                 piece += 1
#                 if piece == profondeur:
#                     return True
#
#
# def lire_fichier(nom_fichier):
#     """ Input = string étant le nom du fichier
#     Output = liste d'objets de classe Piece représentant les polyominos
#     contenus dans le fichier"""
#     liste_pieces = []
#     with open(nom_fichier, 'r') as file:
#         str_file = file.read().split("\n")
#     nb_p = int(str_file[0][0])
#     size = int(str_file[0][2])
#     for where in range(nb_p):
#         name = str_file[(where * (size + 1)) + 1][0]
#         matrice = []
#         for pos_y in range(2, size + 2):
#             line = []
#             for pos_x in range(0, size * 2, 2):
#                 line.append(int(str_file[(where * (size + 1)) + pos_y][pos_x]))
#             matrice.append(line)
#         liste_pieces.append(Piece(name, Ma_matrice(matrice)))
#     return liste_pieces, nb_p
#
#
# def taille_totale_pieces(liste_pieces):
#     """ Input = liste d'objet de classe Piece
#     Output = somme de la taille de chaque pièce"""
#     nb = 0
#     for piece in liste_pieces:
#         for line in piece.liste_variantes[0].matrice:
#             nb += line.count(1)
#     return nb
#
#
# def possibles_factorisations(nb):
#     """Input: nb est un int
#     Output = liste de tuples de taille 2 contenant toutes les factorisations possibles en
#     2 facteurs de nb. Attention à ne pas les répéter 2 fois."""
#     facto = []
#     for i in range(1, int(nb / 2)):
#         for j in range(nb, 0, -1):
#             if i <= j and i * j == nb:
#                 facto.append((i, j))
#     return facto
#
#
# def trouver_liste_solutions(nom_fichier):
#     """Fonction principale qui trouve la liste des solutions.
#     Output = liste d'objets de la classe Tableau qui contiennent les différentes solutions"""
#     pieces, nb_p = lire_fichier(nom_fichier)
#     nb_piece = taille_totale_pieces(pieces)
#     for where in range(len(pieces)):
#         pieces[where].posibilite()
#
#     nb_add = 0
#     solutions = []
#     soluce = False
#
#     while not soluce:
#         factos = possibles_factorisations(nb_piece + nb_add)
#         for size in factos:
#             tab = Tableau(size, pieces)
#             if tab.backtracking(nb_p):
#                 solutions.append(tab)
#                 soluce = True
#         nb_add += 1
#
#     return solutions
#
#
# if __name__ == '__main__':
#     # nom_fichier = sys.argv[1]
#     start = timeit.default_timer()
#     liste_solutions = trouver_liste_solutions("set_pieces_1.poly")
#     for tableau in liste_solutions:
#         tableau.imprimer()
#     end = timeit.default_timer()
#     print("time " + str(end-start) + " sec")
#
#
# # def backtrac(self, profondeur):
# #     self.imprimer()
# #     if len(self.liste_pieces) == profondeur:
# #         return True
# #     elif profondeur < 0 or self.Pos_pieces[0][1] == self.largeur:
# #         return False
# #     else:
# #         if self.ajouter_piece(profondeur, self.var[profondeur], self.Pos_pieces[profondeur]):
# #             self.backtracking(profondeur + 1)
# #         else:
# #             if self.lt_var[profondeur] - 1 > self.var[profondeur]:
# #                 self.var[profondeur] += 1
# #                 self.backtracking(profondeur)
# #             else:
# #                 if self.Pos_pieces[profondeur][0] < self.hauteur - 1:
# #                     self.Pos_pieces[profondeur][0] += 1
# #                     self.backtracking(profondeur)
# #                 else:
# #                     self.Pos_pieces[profondeur][0] = 0
# #                     self.Pos_pieces[profondeur][1] += 1
# #                     if self.Pos_pieces[profondeur][1] == self.largeur:
# #                         self.Pos_pieces[profondeur] = [0, 0]
# #                         self.enlever_piece(profondeur - 1)
# #                         if self.lt_var[profondeur] - 1 > self.var[profondeur]:
# #                             self.var[profondeur] += 1
# #                         else:
# #                             self.var[profondeur] = 0
# #                             if self.Pos_pieces[profondeur][0] < self.hauteur - 1:
# #                                 self.Pos_pieces[profondeur][0] += 1
# #                             else:
# #                                 self.Pos_pieces[profondeur][0] = 0
# #                                 self.Pos_pieces[profondeur][1] += 1
# #                         self.backtracking(profondeur - 1)
# #                     else:
# #                         self.backtracking(profondeur)