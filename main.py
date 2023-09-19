import numpy as np
import re


def tokenize(s, separators):
    pattern = "|".join(map(re.escape, separators))
    return re.split(pattern, s)


def main():
    dictionary = [
        ["O peã e o caval são pec de xadrez. O caval é o melhor do jog."],
        ["A jog envolv a torr, o peã e o rei."],
        ["O peã lac o boi"],
        ["Caval de rodei!"],
        ["Polic o jog no xadrez."],  # documentos
    ]
    stopwords = ["a", "o", "e", "é", "de", "do", "no", "são"]  # lista de stopwords
    query = "xadrez peã caval torr"  # consulta
    separators = [" ", ",", ".", "!", "?"]  # separadores para tokenizacao

    tokenized_dictionary = [tokenize(s, separators) for s in dictionary]
    print(tokenized_dictionary)


if __name__ == "__main__":
    main()
