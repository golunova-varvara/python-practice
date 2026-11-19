def find_book_linear(books, title):
    """
    Search for a book by title using linear search.

    Args:
        books (list): list of book titles
        title (str): target book title

    Returns:
        int: index of the book, or -1 if not found
    """
    if not books:
        return -1

    for i in range(len(books)):
        if books[i] == title:
            return i
    return -1


def find_book_binary(books, title):
    """
    Search for a book by title using binary search (requires a sorted list).

    Args:
        books (list): sorted list of book titles
        title (str): target book title

    Returns:
        int: index of the book, or -1 if not found
    """
    left = 0
    right = len(books) - 1

    while left <= right:
        mid = (left + right) // 2

        if books[mid] == title:
            return mid
        elif books[mid] < title:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def sort_books(books):
    """
    Sort a list of books alphabetically using bubble sort.

    Args:
        books (list): unsorted list of book titles

    Returns:
        list: alphabetically sorted list of books
    """
    n = len(books)
    for i in range(n):
        flag = False

        for j in range(n - i - 1):
            if books[j] > books[j + 1]:
                books[j], books[j + 1] = books[j + 1], books[j]
                flag = True

        if not flag:
            break
    return books


# Testing
sample_books = ['War and Peace', 'Eugene Onegin', 'Dead Souls', 'Crime and Punishment']
print(sort_books(sample_books.copy()))

sorted_books = sort_books(sample_books.copy())

print(find_book_linear(sorted_books, 'Eugene Onegin'))  # 2
print(find_book_binary(sorted_books, 'Eugene Onegin'))  # 2

# Edge cases and missing items
print(find_book_linear([], 'Eugene Onegin'))  # -1
print(find_book_linear(['Crime and Punishment', 'Dead Souls', 'War and Peace'], 'Eugene Onegin'))  # -1
print(find_book_binary(['Crime and Punishment', 'Dead Souls', 'War and Peace'], 'Eugene Onegin'))  # -1