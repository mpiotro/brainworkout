# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
import timeit
from collections import defaultdict


def num_encodings(s):
    # Recursive solution:
    # '' should return 1, since we can parse it as ''
    # '1' should return 1, since we can parse it as 'a' + ''
    # '11' should return 2, since we can parse it as 'a' + 'a' + '' and 'k' + ''
    # '111' should return 3, 'a'+'a'+'a'+'', 'k'+'a'+'', 'a'+'k'+''
    # '011' should return 0, no letter can start with 0
    # '602' should return 0, no letter encoded with 60

    if s.startswith("0"):
        return 0
    elif len(s) <= 1:  # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total


def num_encodings_opt(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1  # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        if s[i].startswith("0"):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i : i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]


if __name__ == "__main__":
    print(num_encodings_opt("11" * 18))
    print(num_encodings("11" * 18))
