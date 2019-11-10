"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    matrix = []
    if isinstance(num_rows, int) and isinstance(num_cols, int):
        for i in range(num_rows):
            row = [0] * num_cols
            matrix.append(row)
    return matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    if not isinstance(edit_matrix, tuple) or edit_matrix == ():
        return []
    edit_matrix = list(edit_matrix)
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return edit_matrix
    if edit_matrix == [[]] * len(edit_matrix):
        return edit_matrix
    for i in range(1, len(edit_matrix)):
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
    for j in range(1, len(edit_matrix[0])):
        edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
    return edit_matrix


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if not isinstance(edit_matrix, tuple):
        return []
    edit_matrix = list(edit_matrix)
    if not isinstance(original_word, str) or not isinstance(target_word, str) or original_word == '' \
            or target_word == '':
        return edit_matrix
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return edit_matrix
    original_word = ' ' + original_word
    target_word = ' ' + target_word
    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[0])):
            a = edit_matrix[i - 1][j] + remove_weight
            b = edit_matrix[i][j - 1] + add_weight
            if original_word[i] != target_word[j]:
                c = edit_matrix[i - 1][j - 1] + substitute_weight
            else:
                c = edit_matrix[i - 1][j - 1]
            number_s = (a, b, c)
            minimum = minimum_value(number_s)
            edit_matrix[i][j] = minimum
    return edit_matrix


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if not isinstance(original_word, str) or not isinstance(target_word, str) or not isinstance(add_weight, int) \
            or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return -1
    rows = len(original_word) + 1
    cols = len(target_word) + 1
    matrix = generate_edit_matrix(rows, cols)
    matrix = tuple(matrix)
    i_matrix = initialize_edit_matrix(matrix, add_weight, remove_weight)
    i_matrix = tuple(i_matrix)
    f_matrix = fill_edit_matrix(i_matrix, add_weight, remove_weight, substitute_weight,
                                   original_word, target_word)
    d = f_matrix[-1][-1]
    return d


def save_to_csv(edit_matrix: list, path_to_file: str) -> None:
    if not isinstance(edit_matrix, list) or not isinstance(path_to_file, str):
        return None
    file = open(path_to_file, "a")
    for m, el in enumerate(edit_matrix):
        for n, i in enumerate(el):
            file.write(str(i) + ',')
        file.write('\n')
    file.close()


def load_from_csv(path_to_file: str) -> list:
    if not isinstance(path_to_file, str):
        return []
    file = open(path_to_file)
    matrix = []
    for line in file:
        row = []
        for el in line:
            if el.isdigit():
                row.append(int(el))
        matrix.append(row)
    file.close()
    return matrix

