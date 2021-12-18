from random import randint, choice

class Neuron:
    def __init__(self, data):
        self.data = data
    
    def store_signal(self, new_signal):
        self.data = new_signal

    def emit_signal(self):
        s = str(self.data)
        return s

class LetterNeuron(Neuron):
    def __init__(self, letter):
        self.letter = letter

class WordNeuron(Neuron):
    def __init__(self, word):
        self.word = word


def ReadDnA(dnaString):
    dna = dnaString
    return dna

def generateCreature(dnaString):
    creature = {}
    dna = dnaString
    geneLimit = len(dnaString * 4)
    random_chances = []
    random_health_A = [14, 24, 300, 19, 23, 30, 30, 30, 30, 30, 30, 30, 30, 49, 30, 30, 21, 19, 30, 8, 8, 8, 32, 34, 125, 125, 125]
    random_health_B = [12, 34, 53, 30, 30, 30, 30, 30, 30, 30, 200, 30, 30, 30, 30, 30, 30, 45, 45, 45, 65, 43, 62, 23, 42, 53, 6, 53, 2, 45, 490]
    random_atk_A = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 32, 1, 34, 7, 5, 3, 2, 1, 6, 7, 87, 6, 7, 8, 10, 13, 134, 11, 31, 13, 52, 2, 5, 6, 2, 67, 7, 8, 4, 5, 3, 5, 6]
    random_atk_B = [5, 4, 2, 5, 32, 4, 42, 32, 45, 654, 31, 4, 32, 4, 13, 42, 77, 2, 23, 32, 5, 7, 6, 4, 1, 1, 1, 1, 1, 1, 1, 3, 6, 45, 42, 24, 75, 11, 23, 23, 23, 11, 11, 11, 11, 1, 11, 11, 34]
    random_resist_A = [3, 4, 6, 5, 2, 5, 7, 8, 7, 7, 5, 5, 8, 4, 3, 3, 4, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 2, 2, 2, 22, 13, 12, 10, 11, 45, 100, 100, 2, 1, 1, 1, 2, 2, 3, 4, 5, 20]
    random_resist_B = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 50, 13, 100]
    random_speed_A = [1, 2, 3, 4, 3, 3, 3, 3, 5, 5, 6, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 2, 1, 20]
    random_speed_B = [10, 11, 12, 22, 13, 13, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 10, 10, 10, 34, 11, 12, 10, 9, 9, 9, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21]
    random_gene_length_A = [4, 3, 4, 4, 6, 4, 4, 4, 5, 4, 4, 4, 6, 3, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2]
    random_gene_length_B = [5, 5, 5, 5, 3, 3, 3, 4, 6, 4, 4, 4, 4, 6, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 2, 2, 2, 4, 3, 3, 3, 3, 3, 8]
    # make dna from pregen
    new_dna = ""

    g = randint(0, 34)

    gene_length = 0
    if g == 0:
        gene_length = random_gene_length_B[randint(0, len(random_gene_length_B) - 1)]
    else:
        gene_length = random_gene_length_A[randint(0, len(random_gene_length_A) - 1)]
    
    print(f"<<DEBUG>> gene length set to: {gene_length}")

    for i in range(0, gene_length):
        print(f"<<DEBUG>> current gene length: {len(new_dna)}")
        h = randint(0, 1)
        a = randint(0, 1)
        r = choice([1, 0])
        s = randint(0, 1)
        if i == 0:
            if h == 0:
                new_dna += "A"
            else:
                new_dna += "B"
        if i == 1:
            if a == 1:
                new_dna += "B"
            else:
                new_dna += "A"
        if i == 2:
            if r == 0:
                new_dna += "A"
            else:
                new_dna += "B"
        if i == 3:
            if s == 0:
                new_dna += "A"
            else:
                new_dna += "B"
        if i == 4:
            if g == 0:
                new_dna += "B"
            else:
                new_dna += "A"

    
    print(f"new dna: {new_dna}")
    creature["DNA"] = new_dna
    new_dna = ""

    # read dna and set creature attributes
    creature["health"] = 0
    creature["attack"] = 0
    creature["resist"] = 0
    creature["speed"] = 0
    creature["genelength"] = len(creature["DNA"])
    # create and load rna copy
    rna = []
    for c in creature["DNA"]:
        rna.append(c)

    try:    
        if rna[0] == "A":
            creature["health"] = random_health_A[randint(0, len(random_health_A) - 1)]
        if rna[0] == "B":
            creature["health"] = random_health_B[randint(0, len(random_health_B) - 1)]
        if rna[1] == "A":
            creature["attack"] = random_atk_A[randint(0, len(random_atk_A) - 1)]
        if rna[1] == "B":
            creature["attack"] = random_atk_B[randint(0, len(random_atk_B) - 1)]
        if rna[2] == "A":
            creature["resist"] = random_resist_A[randint(0, len(random_resist_A) - 1)]
        if rna[2] == "B":
            creature["resist"] = random_resist_B[randint(0, len(random_resist_B) - 1)]
        if rna[3] == "A":
            creature["speed"] = random_speed_A[randint(0, len(random_speed_A) - 1)]
        if rna[3] == "B":
            creature["speed"] = random_speed_B[randint(0, len(random_speed_B) - 1)]
        if rna[4] == "A":
            creature["genelength"] = random_gene_length_A[randint(0, len(random_gene_length_A) - 1)] + 1
        if rna[4] == "B":
            creature["genelength"] = random_gene_length_B[randint(0, len(random_gene_length_B) - 1)] + 1
    except IndexError:
        print("<<DEBUG>> <<gene limit reached>>")

    while len(creature["DNA"]) < creature["genelength"]:
        roll = randint(0, 3)
        newgene = ""
        if roll == 0:
            newgene = "A"
        elif roll == 1:
            newgene = "B"
        elif roll == 2:
            newgene = "C"
        elif roll == 3:
            newgene = "B"
        else:
            newgene = "A"

        creature["DNA"] += newgene
        y = creature["DNA"]
        print(f"<<DEBUG>> creature {y} made.")

    return creature
    
def reproduce(c1, c2):
    # can reproduce? yes = same number of genes - 1
    print("<<DEBUG>>")

    if (c1["genelength"] - 1) > (c2["genelength"] + 1):
        print("species incompatible")
        return None
    else:
        print("species compatible")
        dna1 = c1["DNA"]
        dna2 = c2["DNA"]
        print(f"{dna1} & {dna2} are compatible")
        o = {"DNA":""}
        for v1 in dna1:
            for v2 in dna2:
                if v1 == v2:
                    o["DNA"] += v1
                else:
                    flip = randint(0, 1)
                    if flip == 1:
                        o["DNA"] += v1
                    else:
                        o["DNA"] += v2
        
        return o["DNA"]


    
    dna = c1["DNA"]
    print(f"dna of c1: {dna}")

    



