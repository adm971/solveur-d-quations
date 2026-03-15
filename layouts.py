
from equation import Equation, Equation2
import PySimpleGUI4 as sg 


# Récupérer les éléments de l'équation dans un dictionnaire(expression, solution, étape, delta)
def make_equa() : 
    equa = Equation()
    equa.test()
    steps = equa.solve()
    texts = {"expression" : equa.expr,
             "solution" : equa.x, 
             "étapes" : steps}
    return texts
def make_equa2() :
    equa = Equation2()
    equa.test()
    steps = equa.solve()
    texts = {"expression" : equa.expr, 
             "delta" : equa.delta, 
             "solution" : equa.solution,
             "étapes" : steps}
    return texts


# MENU PRINCIPAL
main_layout = [
    [sg.Text("Choisir un exercice")],

    [sg.Button(button_text="Equation du 1er degré", key="eq1", button_color="green", disabled_button_color="red", auto_size_button=True, mouseover_colors="blue")],
    [sg.Button(button_text="Equation du 2nd degré", key="eq2",button_color="green", disabled_button_color="red", auto_size_button=True, mouseover_colors="blue")],
    ]



# LAYOUT DES EQUATIONS 
texts = make_equa()
# MENU EQUATION 1ER DEGRE
eq1_layout = [

    [sg.Text("Equation du premier degré")],

    [
    sg.Button("Réponse", key="rep1", auto_size_button=True), 
    sg.Button("Résoudre", key="res1", auto_size_button=True)
    ]
]
# REPONSE DE l'EQUATION
eq1_solved_layout = [
    [sg.Text(f"Expression : {texts['expression']}")],
    [sg.Text(f"Solution : {texts['solution']}")],
    [sg.Text("Étapes :")]
]
for step in texts['étapes']:
    eq1_solved_layout.append([sg.Text(step)])
# MODE RESOUDRE EQUATION
eq1_input_layout = [
    [sg.Text("Résoudre l'équation suivante : "), sg.Text(texts['expression'])],
    [sg.Input("", key="stepEq1Input"), sg.Button("Valider", key="stepEq1"), sg.Button("Terminer", key="finishEq1")],
    [sg.Text("Historique des étapes :")],
    [sg.Column([[]], key="history", scrollable=True, vertical_scroll_only=True, size=(400, 200))]
] # COLUMN POUR METTRE A JOUR DYNAMIQUEMENT

# COMPARER INPUT UTILISATEUR ET CORRECTION
eq1_verif_layout = [
    [sg.Text(f"Expression : {texts['expression']}")],
    [sg.Text("Mes étapes :")]
]




# SECOND DEGRE
texts2 = make_equa2()
eq2_layout = [

    [sg.Text("Equation du second degré")],

    [
    sg.Button("Réponse", key="rep2", auto_size_button=True), 
    sg.Button("Résoudre", key="res2", auto_size_button=True)
    ],

]

# REPONSE DE L'EQUATION 2ND DEGRE
eq2_solved_layout = [
    [sg.Text(f"Expression : {texts2['expression']}")],
    [sg.Text(f"Delta : {texts2['delta']}")],
    [sg.Text(f"Solution(s) : {texts2['solution']}")]
]


# MODE RESOUDRE EQUATION 2ND DEGRE
eq2_input_layout = [
    [sg.Text("Résoudre l'équation suivante : "), sg.Text(texts2['expression'])],
    [sg.Input("", key="stepEq2Input"), 
    sg.Button("Valider", key="stepEq2"), 
    sg.Button("Terminer", key="finishEq2")],

    [sg.Text("Historique des étapes :")],
    [sg.Column([[]], key="history2", scrollable=True, vertical_scroll_only=True, size=(400, 200))]
]


# COMPARER INPUT UTILISATEUR ET CORRECTION
eq2_verif_layout = [
    [sg.Text(f"Expression : {texts2['expression']}")],
    [sg.Text("Mes étapes :")]
]