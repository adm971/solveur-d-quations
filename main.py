
import PySimpleGUI4 as sg
from layouts import main_layout, eq1_layout, eq2_layout, eq1_solved_layout, eq1_input_layout, texts, texts2, eq1_verif_layout, eq2_input_layout, eq2_solved_layout, eq2_verif_layout

win = sg.Window("Solveur d'équations", main_layout)
history_steps = []

while True :
    event, values = win.read()

    if event == sg.WIN_CLOSED : # FERMER LA FENETRE
        break 
    


    # CHOISIR EQUATION DU PREMIER DEGRE
    if event == "eq1" : 
        win.close()
        win = sg.Window("Equation", eq1_layout)


    # VOIR LA REPONSE 
    if event == "rep1" :
        print("réponse")
        win.close()
        win = sg.Window("Equation", eq1_solved_layout)


    # PASSER EN MODE EXERCICE
    if event == "res1" :
        print("résoudre")
        win.close()
        win = sg.Window("Equation", eq1_input_layout, finalize=True)

    if event == "stepEq1" : # VALIDER LES INPUTS
        user_input = values["stepEq1Input"]
        print(user_input)
        history_steps.append(user_input)

        win.extend_layout( # AJOUTER LES INPUT DANS LE LAYOUT 
        win["history"],
        [[sg.Text(user_input)]]
    )
        # Forcer le scroll après la MàJ du layout
        win["history"].contents_changed()
        print(history_steps)

    if event == "finishEq1" : # FINIR L'EXERCICE
        print(values["stepEq1Input"])
        # ENTRER LES ETAPES USER
        for step in history_steps :
            eq1_verif_layout.append([sg.Text(step)])
        eq1_verif_layout.append([sg.Text("Correction")])
        # ENTRER LES ETAPES DE LA CORRECTION
        for step in texts['étapes']:
            eq1_verif_layout.append([sg.Text(step)])
        win.close()
        win = sg.Window("Résultat", eq1_verif_layout)




    # CHOISIR EQUATION DU SECOND DEGRE
    if event == "eq2" :  
        win.close()
        win = sg.Window("Equation", eq2_layout)
    # VOIR LA REPONSE 
    if event == "rep2" :
        print("réponse")
        win.close()
        win = sg.Window("Equation", eq2_solved_layout)


    # PASSER EN MODE EXERCICE
    if event == "res2" :
        print("résoudre")
        win.close()
        win = sg.Window("Equation", eq2_input_layout, finalize=True)

    if event == "stepEq2" : # VALIDER LES INPUTS
        user_input = values["stepEq2Input"]
        print(user_input)
        history_steps.append(user_input)

        win.extend_layout( # AJOUTER LES INPUT DANS LE LAYOUT 
        win["history2"],
        [[sg.Text(user_input)]]
    )
        # Forcer le scroll après la MàJ du layout
        win["history2"].contents_changed()
        print(history_steps)

    if event == "finishEq2" : # FINIR L'EXERCICE
        print(values["stepEq2Input"])
        # ENTRER LES ETAPES USER
        for step in history_steps :
            eq2_verif_layout.append([sg.Text(step)])
        eq2_verif_layout.append([sg.Text("Correction")])
        # ENTRER LES ETAPES DE LA CORRECTION
        for step in texts2['étapes']:
            eq2_verif_layout.append([sg.Text(step)])
        win.close()
        win = sg.Window("Résultat", eq2_verif_layout)
win.close()

