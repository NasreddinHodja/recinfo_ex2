#!/usr/bin/env python3

"""
Author: Tomás Bizet de Barros
DRE: 116183736
"""

import numpy as np
import re


def tokenize(s, separators):
    pattern = "|".join(map(re.escape, separators))
    tokens = re.split(pattern, s)
    if tokens[-1] == "":
        tokens.pop()
    return [token for token in tokens if token]


def normalize(s):
    normalized = s.lower().strip()
    return normalized


def remove_stopwords():
    pass


def main():
    # input
    dictionary = np.array(
        [
            "O peã e o caval são pec de xadrez. O caval é o melhor do jog.",
            "A jog envolv a torr, o peã e o rei.",
            "O peã lac o boi",
            "Caval de rodei!",
            "Polic o jog no xadrez.",  # documentos
        ]
    )
    stopwords = ["a", "o", "e", "é", "de", "do", "no", "são"]  # lista de stopwords
    query = "xadrez peã caval torr"  # consulta
    separators = [" ", ",", ".", "!", "?"]  # separadores para tokenizacao

    # normalize
    # vectorized_normalize = np.vectorize(normalize, otypes=[object])
    normalized = [normalize(s) for s in dictionary]

    # tokenize
    # vectorized_tokenize = np.vectorize(normalize, otypes=[object])
    tokens_list = [tokenize(s, separators) for s in normalized]

    # # rmv stopwords
    tokens_list = [
        [token for token in tokens if token not in stopwords] for tokens in tokens_list
    ]
    print(tokens_list)


if __name__ == "__main__":
    main()
