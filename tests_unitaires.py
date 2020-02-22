"""Ce script performe des tests unitaires sur les fonctions et méthodes du fichier Polyominos_solution.py
Ce script prend un nombre comme argument qui indique le numéro de test performé:
1. Ma_matrice.colonne
2. Ma_matrice.rotation_horaire
3. Ma_matrice.reflexion_axe_horizontal
4. Ma_matrice.translation_haut
5. Ma_matrice.translation_gauche
6. Ma_matrice.translation_haut_gauche
7. Piece.ajout_variante
8. Tableau.ajouter_piece
9. Tableau.enlever_piece
10. taille_totale_pieces
11. possibles_factorisations
12. trouver_liste_solutions set_pieces_1.poly
12. trouver_liste_solutions set_pieces_2.poly
"""

import sys
from Polyominos import *

def test_1():
	#teste Ma_matrice.colonne
	matrice = Ma_matrice([[1,0,1],[1,1,1],[0,0,1]])
	try:
		matrice.colonne(1)
	except:
		print("une excéption s'est produite dans ta méthode Ma_matrice.colonne")

	if (matrice.colonne(1) == [0,1,0]):
		print('test 1 réussi')
	else:
		print('test 1 raté')
		print('la matrice testée est', matrice.matrice)
		print('la colonne 1 est', [0,1,0])
		print('ta méthode donne', matrice.colonne(1))

def test_2():
	#teste Ma_matrice.rotation_horaire
	matrice = Ma_matrice([[1,0,1],[1,1,1],[0,0,1]])
	try:
		matrice_apres_rotation = matrice.rotation_horaire()
	except:
		print("une excéption s'est produite dans ta méthode Ma_matrice.rotation_horaire")

	if matrice.matrice != [[1,0,1],[1,1,1],[0,0,1]]:
		print('test 2 raté')
		print('la matrice originale ne doit pas être modifiée, seulement celle du output subi une rotation')
	elif matrice_apres_rotation.matrice != [[0, 1, 1], [0, 1, 0], [1, 1, 1]]:
		print('test 2 raté')
		print('la matrice testée est', [[1,0,1],[1,1,1],[0,0,1]])
		print('Ta matrice est', matrice_apres_rotation.matrice)
		print("alors qu'elle devrait être", [[0, 1, 1], [0, 1, 0], [1, 1, 1]])
	else:
		print('test 2 réussi')

def test_3():
	#teste Ma_matrice.reflexion_axe_horizontal
	matrice = Ma_matrice([[1,0,1],[1,1,1],[0,0,1]])
	try:
		matrice_apres_reflexion = matrice.reflexion_axe_horizontal()
	except:
		print("une excéption s'est produite dans ta méthode Ma_matrice.reflexion_axe_horizontal")
	if matrice.matrice != [[1,0,1],[1,1,1],[0,0,1]]:
		print('test 3 raté')
		print('la matrice originale ne doit pas être modifiée, seulement celle du output subi une reflexion')
	elif matrice_apres_reflexion.matrice != [[0, 0, 1], [1, 1, 1], [1, 0, 1]]:
		print('test 3 raté')
		print('la matrice testée est', [[1,0,1],[1,1,1],[0,0,1]])
		print('Ta matrice est', matrice_apres_reflexion.matrice)
		print("alors qu'elle devrait être", [[0, 0, 1], [1, 1, 1], [1, 0, 1]])
	else:
		print('test 3 réussi')

def test_4():
	#teste Ma_matrice.translation_haut(1)
	matrice = Ma_matrice([[0,0,0],[0,0,1],[0,0,1]])
	matrice.matrice = [[0,0,0],[1,1,1],[0,0,1]]
	try:
		matrice.translation_haut(1)
	except:
		print("une excéption s'est produite dans ta méthode Ma_matrice.translation_haut")
	if matrice.matrice != [[1,1,1],[0,0,1],[0,0,0]]:
		print('test 4 raté')
		print('la matrice testée est', [[0,0,0],[1,1,1],[0,0,1]])
		print('Ta matrice est', matrice.matrice)
		print("alors qu'elle devrait être", [[1,1,1],[0,0,1],[0,0,0]])
	else:
		print('test 4 réussi')
	pass

def test_5():
	#teste Ma_matrice.translation_gauche(2)
	matrice = Ma_matrice([[0,0,0],[0,0,1],[0,0,1]])
	matrice.matrice = [[0,0,0],[0,0,1],[0,0,1]]
	try:
		matrice.translation_gauche(2)
	except:
		print("une excéption s'est produite dans ta méthode Ma_matrice.translation_gauche")
	if matrice.matrice != [[0,0,0],[1,0,0],[1,0,0]]:
		print('test 5 raté')
		print('la matrice testée est', [[0,0,0],[0,0,1],[0,0,1]])
		print('Ta matrice est', matrice.matrice)
		print("alors qu'elle devrait être", [[0,0,0],[1,0,0],[1,0,0]])
	else:
		print('test 5 réussi')

def test_6():
	#teste Ma_matrice.translation_haut_gauche()
	matrice = Ma_matrice([[0,0,0],[0,0,1],[0,0,1]])
	try:
		matrice.translation_haut_gauche()
	except:
		print("une excéption s'est produite dans ta méthode Ma_matrice.translation_haut_gauche")
	if matrice.matrice != [[1,0,0],[1,0,0],[0,0,0]]:
		print('test 6 raté')
		print('la matrice testée est', [[0,0,0],[0,0,1],[0,0,1]])
		print('Ta matrice est', matrice.matrice)
		print("alors qu'elle devrait être", [[1,0,0],[1,0,0],[0,0,0]])
	else:
		print('test 6 réussi')

def test_7():	
	#teste Piece.ajout_variante
	matrice = Ma_matrice([[1,0,1],[1,1,1],[0,0,1]])
	try:
		piece = Piece('a',matrice)
		piece.liste_variantes = [matrice]
	except:
		print("une excéption s'est produite dans ta méthode Piece.__init__")
	if (piece.nom!='a'):
		print('test 7 raté')
		print("le nom de la pièce n'est pas correct")
		print("il devrait être", "a")
		print("et le tien est", piece.nom)
	try:
		piece.ajout_variante(matrice)
	except:
		print("une excéption s'est produite dans ta méthode piece.ajout_variante")
	if (len(piece.liste_variantes) != 1):
		print('test 7 raté')
		print('si la variante est déjà présente, ne pas la rajouter dans la liste')
	
	try:
		piece.ajout_variante(matrice.rotation_horaire())
	except:
		print("une excéption s'est produite dans ta méthode piece.ajout_variante")
	if (len(piece.liste_variantes) != 2):
		print('test 7 raté')
		print("si la variante n'est pas présente, il faut la rajouter")
	else:
		print('test 7 réussi')

def test_8():
	#8. Tableau.ajouter_piece
	matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])
	try:
		liste_pieces = [Piece('a',matrice),Piece('b',matrice)]
	except:
		print("une excéption s'est produite dans ta méthode Piece.__init__")
	
	try:
		tableau = Tableau([6,4], liste_pieces)
	except:
		print("une excéption s'est produite dans ta méthode Tableau.__init__")

	try:
		tableau.ajouter_piece(0,0,[0,0])
	except:
		print("une excéption s'est produite dans l'ajout de la pièce Piece('a',matrice) à un tableau vide,"+
			" matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]]), variante 0, pos = [0,0]")

	if (tableau.Pos_pieces[0] != [0,0]):
		print('test 8 raté')
		print("tableau.Pos_pieces n'a pas été mis à jour correctement durant le test pour l'input:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("tableau = Tableau([6,4], liste_pieces)")
		print("tableau.ajouter_piece(0,0,[0,0])")
		print("tableau.Pos_pieces devrait être ", [[0,0],[]])
		print("le votre est", tableau.Pos_pieces)


	bon_tableau = [[" " for i in range(4)] for j in range(6)]
	bon_tableau[0][0:3] = [" ","a"," "]
	bon_tableau[1][0:3] = ["a","a","a"]
	bon_tableau[2][0:3] = [" ","a"," "]
	   
	if (tableau.tableau != bon_tableau):
		print('test 8 raté')
		print("tableau.tableau n'a pas été mis à jour correctement durant le test pour l'input suivant:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("tableau = Tableau([6,4], liste_pieces)")
		print("tableau.ajouter_piece(0,0,[0,0])")
		print("votre tableau est")
		print(tableau.tableau)
		print("alors qu'il devrait être")
		print(bon_tableau)

	try:
		tableau.ajouter_piece(1,0,[1,0])
	except:
		print("une excéption s'est produite dans l'ajout de la pièce Piece('b',matrice) à la postion [1,0] à un tableau qui contenait la piece Piece('a',matrice) à la position [0,0],"+
			"matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")

	if (tableau.tableau!=bon_tableau):
		print('test 8 raté')
		print("tableau.tableau a été modifié lors de la temptative d'ajout d'une pièce qui avait un overlap avec une autre. Input:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("tableau = Tableau([6,4], liste_pieces)")
		print("tableau.ajouter_piece(0,0,[0,0])")
		print("tableau.ajouter_piece(1,0,[1,0])")
		print("votre tableau est")
		print(tableau.tableau)
		print("alors qu'il devrait être")
		print(bon_tableau)

	try:
		tableau.ajouter_piece(1,0,[3,0])
	except:
		print("une excéption s'est produite dans l'ajout de la pièce Piece('b',matrice) à la postion [3,0] à un tableau qui contenait la piece Piece('a',matrice) à la position [0,0],"+
			"matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")

	bon_tableau[3][0:3] = [" ","b"," "]
	bon_tableau[4][0:3] = ["b","b","b"]
	bon_tableau[5][0:3] = [" ","b"," "]
	if (tableau.tableau!=bon_tableau):
		print('test 8 raté')
		print("tableau.tableau n'a pas été correctement mis à jour. Input:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("tableau = Tableau([6,4], liste_pieces)")
		print("tableau.ajouter_piece(0,0,[0,0])")
		print("tableau.ajouter_piece(3,0,[1,0])")
		print("votre tableau est")
		print(tableau.tableau)
		print("alors qu'il devrait être")
		print(bon_tableau)
	else:
		print('test 8 réussi')

def test_9():
	#teste Tableau.enlever_piece
	matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])
	liste_pieces = [Piece('a',matrice),Piece('b',matrice)]
	tableau = Tableau([6,4], liste_pieces)
	tableau.ajouter_piece(0,0,[0,0])
	tableau.ajouter_piece(1,0,[3,0])
	try:
		tableau.enlever_piece(1)
	except:
		print("une excéption s'est produite dans le code:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("tableau = Tableau([6,4], liste_pieces)")
		print("tableau.ajouter_piece(0,0,[0,0])")
		print("tableau.ajouter_piece(1,0,[3,0])")
		print("tableau.enlever_piece(1)")

	bon_tableau = [[" " for i in range(4)]
				for j in range(6)]
	bon_tableau[0][0:3] = [" ","a"," "]
	bon_tableau[1][0:3] = ["a","a","a"]
	bon_tableau[2][0:3] = [" ","a"," "]

	if tableau.tableau != bon_tableau:
		print('test 9 raté')
		print("tableau.tableau n'a pas été correctement mis à jour après enlever une pièce. Input:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("tableau = Tableau([6,4], liste_pieces)")
		print("tableau.ajouter_piece(0,0,[0,0])")
		print("tableau.ajouter_piece(1,0,[3,0])")
		print("tableau.enlever_piece(1)")
		print("votre tableau est")
		print(tableau.tableau)
		print("alors qu'il devrait être")
		print(bon_tableau)
	else:
		print('test 9 réussi')

def test_10():
	#teste taille_totale_pieces
	matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])
	liste_pieces = [Piece('a',matrice),Piece('b',matrice)]
	try:
		taille = taille_totale_pieces(liste_pieces)
	except:
		print("une excéption s'est produite dans le code:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("taille = taille_totale_pieces(liste_pieces)")

	if(taille!=10):
		print('test 10 raté')
		print("La taille d'un ensemble de pièce n'a pas été calculé correctement. Lorsqu'on lance:")
		print("matrice = Ma_matrice([[0,1,0],[1,1,1],[0,1,0]])")
		print("liste_pieces = [Piece('a',matrice),Piece('b',matrice)]")
		print("taille = taille_totale_pieces(liste_pieces)")
		print("taille devrait être égale à 10")
		print("avec votre code elle est égale à", taille)
	else:
		print('test 10 réussi')


def test_11():
	try:
		solution = possibles_factorisations(16)
	except:
		print("une excéption s'est produite dans le code:")
		print("solution = possibles_factorisations(16)")
	if (len(solution)!= 3):
		print('test 11 raté')
		print("lorsqu'on lance, solution = possibles_factorisations(16), solution devrait avoir 3 éléments: (1,16), (2,8) et (4,4). L'ordre n'est pas important. Vous n'avez pas 3 exactement factorisations.")
	elif ((1,16) not in solution and (16,1) not in solution):
		print('test 11 raté')
		print("lorsqu'on lance: solution = possibles_factorisations(16), (1,16) ou (16,1) doit être contenu dans la solution et ce n'est pas le cas avec votre code")
	elif ((2,8) not in solution and (8,2) not in solution):
		print('test 11 raté')
		print("lorsqu'on lance: solution = possibles_factorisations(16), (2,8) ou (8,2) doit être contenu dans la solution et ce n'est pas le cas avec votre code")
	elif ((4,4) not in solution):
		print('test 11 raté')
		print("lorsqu'on lance: solution = possibles_factorisations(16), (4,4) doit être contenu dans la solution et ce n'est pas le cas avec votre code")
	else:
		print('test 11 réussi')

def test_12():
	try:
		liste_solutions = trouver_liste_solutions('set_pieces_1.poly')
	except:
		print("une excéption s'est produite dans le code:")
		print("liste_solutions = trouver_liste_solutions('set_pieces_1.poly')")

	print("Une solution possible pour le set de pièce 1 est:")
	print(" ------ ")
	print("|aacddd|")
	print("|accced|")
	print("|ffceee|")
	print("|ffbbbe|")
	print(" ------ ")
	print("Votre solution est")
	for tableau in liste_solutions:
		tableau.imprimer()
	print("Elle doit avoir les mêmes dimensions que la solution donnée et toutes les pièces doivent être présentes")

def test_13():
	try:
		liste_solutions = trouver_liste_solutions('set_pieces_2.poly')
	except:
		print("une excéption s'est produite dans le code:")
		print("liste_solutions = trouver_liste_solutions('set_pieces_2.poly')")

	print("Une solution possible pour le set de pièce 2 est:")
	print(" -------- ")
	print("|aacbbbed|")
	print("|accceeed|")
	print("|  c  edd|")
	print(" -------- ")
	print(" ------ ")
	print("|aabbb |")
	print("|ac e d|")
	print("|ccceed|")
	print("| ceedd|")
	print(" ------ ")
	print("Votre solution est")
	for tableau in liste_solutions:
		tableau.imprimer()
	print("Les tableaux doivent avoir les mêmes dimensions que ceux donnés, toutes les pièces doivent être présentes et la hauteur du premier tableau doit être plus petite que celle du deuxième tableau")

try:
	test_number = int(sys.argv[1])
except:
	print('Ce script prend 1 argument qui est le numéro de test')
if test_number == 1: test_1()
elif test_number == 2: test_2()
elif test_number == 3: test_3()
elif test_number == 4: test_4()
elif test_number == 5: test_5()
elif test_number == 6: test_6()
elif test_number == 7: test_7()
elif test_number == 8: test_8()
elif test_number == 9: test_9()
elif test_number == 10: test_10()
elif test_number == 11: test_11()
elif test_number == 12: test_12()
elif test_number == 13: test_13()
