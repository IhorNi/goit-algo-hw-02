from collections import deque


def is_palindrome(string):
    processed_string = ''.join(string.split()).lower()

    d = deque(processed_string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


if __name__ == '__main__':

    words = [
        'raDar',
        'A dog! A panic in a pagoda!',
        'A dog A panic in a pagoda',
        'Python',
        'bread',
        'Not a banana baton'
    ]
    for word in words:
        print(f"Is '{word}' ({len(word)} chars) a palindrome? - {is_palindrome(word)}")
