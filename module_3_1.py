calls = 0
n = 0
def count_calls():
    calls = n + 1
    return print(calls)

def string_info(string):
    return print([len(string),string.upper(), string.lower()]), count_calls()


def is_contains(string, list_to_search): # FFFFFFFFFFFFFFFFFFFFFFFF

    wow = (len(list_to_search))
    for i in range(1,wow):
            if string == list_to_search[i] or string.upper() == list_to_search[i] or string.lower() == list_to_search[i]:
                return print(True), count_calls()
            else:
                return print(False), count_calls()

string_info("grsdrgdrgihnihn ih ")
is_contains("abcd", [1,"abcd"])
is_contains("abc", [1,"abca"])
count_calls()
