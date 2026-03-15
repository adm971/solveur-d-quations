import random
from fractions import Fraction
from math import sqrt


def sqr(x) :
    return x*x


class Equation :
    def __init__(self): pass

        # on cherche A,B,C,D,x,n et deux signes s1,s2
    def test(self, min_coeff=-9, max_coeff=9, min_n=11, max_n=99) :
        while True: 
            self.x, self.A, self.B = random.randint(min_coeff, max_coeff), random.randint(0,1), random.randint(0,1)
            n = [-1,-2,-3,-4,-5,-6,-7,-8,-9,1,2,3,4,5,6,7,8,9]

            match self.A :
                case 0 :
                    self.A = random.randint(min_coeff, max_coeff)
                case 1 :
                    self.A = Fraction(random.choice(n), random.choice(n))
            match self.B :
                case 0 :
                    self.B = random.randint(min_coeff, max_coeff)
                case 1 :
                    self.B = Fraction(random.choice(n), random.choice(n))

            if self.x == 0 or self.A == 0 or self.B == 0:
                continue

            self.s1 = random.choice(["+", "-"]) # choisir signe1 et calculer n
            if self.s1 == "+":
                n = self.A * self.x + self.B
            else:
                n = self.A * self.x - self.B
            if not (min_n <= n <= max_n): # limiter n à l'intervalle voulu
                continue


            # maintenant choisir C et signe2, en calculant D pour obtenir n
            self.C = random.randint(min_coeff, max_coeff)  
            if self.C == 0:
                continue
            self.s2 = random.choice(["+", "-"])
            if self.s2 == "+":
                self.D = n + self.C * self.x # C*x + D = n  => D = n + C*x
            else:
                self.D = self.C * self.x - n # C*x - D = n  => D = C*x - n
            if self.D == 0 or self.D < min_coeff or self.D > max_coeff :  # vérifier limites et non-nullité
                continue


            # présentation de l'exo
            left = self.A*self.x + self.B if self.s1 == "+" else self.A*self.x - self.B
            right = self.C*self.x + self.D if self.s2 == "+" else self.C*self.x - self.D

            self.result = str(self.x)
            self.exo = f"{self.A}x {self.s1} {self.B} = {self.C}x {self.s2} {self.D}"
            return self.A, self.B, self.C, self.D, self.x, n, self.s1, self.s2, self.exo
    def solve(self) : 


        steps = []

        # Ax +/- B   =   Cx +/- D
        # EQUATION INITIALE
        print("Equation : ")
        print(self.exo)
        self.expr = self.exo
        steps.append(self.expr)



        # ENLEVER LE X DE DROITE 
        # Ax +/- B   =   (Cx +/- Cx)  +/- D
        if self.C < 0: # SI C EST NEGATIF ON AJOUTE -C
            self.exo = f"{self.A}x {self.s1} {self.B} = {self.C}x + {-self.C}x {self.s2} {self.D}"
            new_s = "+" # nouveau signe à ajouter de l'autre coté sur les x
        else: # SI C EST POSITIF ON ENLEVE C 
            self.exo = f"{self.A}x {self.s1} {self.B} = {self.C}x - {self.C}x {self.s2} {self.D}"
            new_s = "-"
        print(self.exo)
        steps.append(self.exo)



        # DEPLACER LE X A GAUCHE
        # (Ax +/- Cx) +/ B   =   0x  +/- D
        self.exo = f"{self.A}x {new_s} {self.C}x {self.s1} {self.B} = 0x {self.s2} {self.D}"
        print(self.exo)
        steps.append(self.exo)
        # (Ax +/- Cx) +/ B   =   0  +/- D  
        self.exo = f"{self.A}x {new_s} {self.C}x {self.s1} {self.B} = 0 {self.s2} {self.D}"
        print(self.exo)
        steps.append(self.exo)



        # CALCULER LES X A GAUCHE
        # (Ax +/- Cx) +/ B   =     D
        self.D = 0 + self.D if self.s2 == "+" else 0 - self.D
        self.exo = f"{self.A}x {new_s} {self.C}x {self.s1} {self.B} = {self.D}"
        print(self.exo)
        steps.append(self.exo)
        # Ax  +/- B   =    D
        self.A = self.A + self.C if new_s == "+" else self.A - self.C
        self.exo = f"{self.A}x {self.s1} {self.B} = {self.D}"
        print(self.exo)
        steps.append(self.exo)



        # ENLEVER LE COEFFICIENT DE GAUCHE ET REGROUPER A DROITE
        # Ax +/- B +/ B    =    D  +/ B 
        if self.s1 == "+" : # SI LE SIGNE EST POSITIF ON ENLEVE B
            self.exo = f"{self.A}x {self.s1} {self.B} - {self.B} = {self.D} - {self.B}"
            print(self.exo)
            steps.append(self.exo)

            self.E = self.D - self.B
            self.exo = f"{self.A}x {self.s1} {self.B - self.B} = {self.E}"
        else : # SI LE SIGNE EST NEGATIF ON AJOUTE B
            self.exo = f"{self.A}x {self.s1} {self.B} + {self.B} = {self.D} + {self.B}"
            print(self.exo)
            steps.append(self.exo)

            self.E = self.D + self.B
            self.exo = f"{self.A}x {self.s1} {self.B + self.B} = {self.E}"
        print(self.exo)
        steps.append(self.exo)




        # TROUVER X
        # Ax = E
        self.exo = f"{self.A}x = {self.E}"
        print(self.exo)
        steps.append(self.exo)

        if self.A == 0:
            if self.E == 0:
                print("0x = 0 : infinité de solutions")
                x = "infinité de solutions"
                steps.append("0x = 0 : infinité de solutions")
            else:
                print(f"0x = {self.E} : pas de solution")
                x = "pas de solution"
                steps.append("pas de solution")
        else:
            x = self.E / self.A
            self.exo = f"x = {self.E}/{self.A}"

            print(self.exo)
            steps.append(self.exo)

            print(f"x = {x}")
            steps.append(f"x = {x}")


        # COMPARER SOLUTION
        print("\n")
        print("===============COMPARAGE DES SOLUTIONS==========")
        print(f"x = {x}")

        print(f"verif result initial : {self.result}")
        if not x == self.result :
            self.result = x
            print(f"nouvelle valeur de result : {self.result}")
            print(f"vrai x = {x}")
        print("======================================================================================================= \n")
        print("\n")

        self.x = x # METTRE A JOUR LE PARAMETRE X A RECUPERER

        # RESUMAX
        for step in steps : 
            print(step)
        return steps



class Equation2() : 
    def __init__(self):
        self.signes = ["+", "-"] # signe des calculs 
        self.n = [-1,-2,-3,-4,-5,-6,-7,-8,-9,1,2,3,4,5,6,7,8,9] # valeur que peuvent prendre x,a,b,c PAS DE 0

    def test(self) : 
        while True : 
            self.x, A, B, C = random.choice(self.n), random.choice(self.n), random.choice(self.n), random.choice(self.n)
            s1, s2 = random.choice(self.signes), random.choice(self.signes)


            expr = A * self.x**2 # ax²
            expr += B * self.x if s1 == "+" else -B * self.x # additionner/soustraire à bx en fonction de s1
            expr += C if s2 == "+" else -C # de meme pour c, en fonction de s2

            if expr == 0: # si l'équation est égale à 0
                self.write(A, B, C, s1, s2, expr) # c'est bon, on peut l'écrire
                break # arreter la boucle
        
    def write(self, a, b, c, s1, s2, expected_zero): # écrire l'équation 
        self.expr = f"{a}x² {s1} {b}x {s2} {c} = {expected_zero}"
        verif = f"{a}*{self.x}² {s1} {b}*{self.x} {s2} {c} = {expected_zero}"

        print(f"Equation quadratique trouvée : {self.expr} \nVérification : {verif}")

        b_ = b if s1 == "+" else -b # SIMPLIFIER LES SIGNES POUR TROUVER LE VRAI B ET LE VRAI C
        c_ = c if s2 == "+" else -c
        self.find_delta(a, b_, c_)

    
    def find_delta(self, a,b,c) : # Trouver delta
        self.delta = sqr(b) - 4*a*c
        self.solution = []
    

        if self.delta == 0 : # Une solution 
            x1 = (-b+sqrt(self.delta))/(2*a)
            self.solution.append(x1)
            
        if self.delta > 0 : # Deux solutions 
            x1 = (-b + sqrt(self.delta)) / (2*a)
            x2 = (-b - sqrt(self.delta)) / (2*a)
            self.solution.append(x1)
            self.solution.append(x2)

        if self.delta < 0 : # Aucune solution 
            self.solution.append("Aucune solution")
        
        print(f"delta = {b}² - 4*{a}*{c} = {self.delta}")
        print(f"solution : {self.solution}")
        return self.delta, self.solution

    def solve(self):

        steps = []

        print("Equation : ")
        print(self.expr)
        steps.append(self.expr)

        expr = self.expr.replace(" = 0", "")
        parts = expr.split()

        a = int(parts[0].replace("x²", ""))
        s1 = parts[1]
        b = int(parts[2].replace("x", ""))
        s2 = parts[3]
        c = int(parts[4])

        b = b if s1 == "+" else -b
        c = c if s2 == "+" else -c

        # Mise sous forme standard
        self.exo = f"{a}x² + ({b})x + ({c}) = 0"
        print(self.exo)
        steps.append(self.exo)

        # CALCUL DU DELTA
        self.delta = b*b - 4*a*c
        self.exo = f"Δ = {b}² - 4×{a}×{c}"
        print(self.exo)
        steps.append(self.exo)

        self.exo = f"Δ = {self.delta}"
        print(self.exo)
        steps.append(self.exo)

        # TROUVER LES SOLUTIONS
        if self.delta < 0:
            sol = "Aucune solution"
            print(sol)
            steps.append(sol)

        elif self.delta == 0:
            x0 = (-b) / (2*a)
            self.exo = f"x = -({b}) / (2×{a})"
            print(self.exo)
            steps.append(self.exo)

            print(f"x = {x0}")
            steps.append(f"x = {x0}")
            sol = [x0]

        else:
            x1 = (-b + sqrt(self.delta)) / (2*a)
            x2 = (-b - sqrt(self.delta)) / (2*a)

            self.exo = f"x1 = (-{b} + √{self.delta}) / (2×{a})"
            print(self.exo)
            steps.append(self.exo)

            print(f"x1 = {x1}")
            steps.append(f"x1 = {x1}")

            self.exo = f"x2 = (-{b} - √{self.delta}) / (2×{a})"
            print(self.exo)
            steps.append(self.exo)

            print(f"x2 = {x2}")
            steps.append(f"x2 = {x2}")

            sol = [x1, x2]

        # Comparaison avec solution trouvée dans test()
        print("\n===============COMPARAISON DES SOLUTIONS==============")
        print(f"Solutions calculées : {sol}")
        print(f"Solutions attendues : {self.solution}")

        self.solution = sol

        print("======================================================\n")

        return steps
    