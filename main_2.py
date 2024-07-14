
def count_vowels(s: str) -> int: # функция принимает один аргумент s, который должен быть строкой (str)
                                 # -> int функция возвращает значение типа int (целое число).
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels) # это генераторное выражение, которое выполняет подсчет количества гласных.