from tabulate import tabulate

class Tableau:

    def afficher_titre(self, titre):
        print(tabulate([[titre]], tablefmt="rounded_outline"))

    def afficher_actions(self, actions):
        test = []
        for action  in actions:
            test.append([action[0], action[1]])
        print(tabulate(test ,tablefmt="rounded_grid"))