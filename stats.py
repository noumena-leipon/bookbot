def get_book_text(book):
    with open(book) as f:
        text = f.read()
        return text


def count_words(text):
    count = len(text.split())
    return count


def count_alphas(text):
    case = text.lower()
    alphas = {}
    for char in case:
        if char in alphas:
            alphas[char] += 1
        else:
            alphas[char] = 1
    return alphas


def sort_alphas(alphas):
    char_list = []
    for char, count in alphas.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(key=lambda d: d["count"], reverse=True)
    return char_list
