def palindrome(text):
    text = text.replace(' ', '').lower()  # Убираем все пробелы и переводим текст в нижний регистр
    if text == text[::-1]:  # Делаем срез с конца строки до начала и сравниваем
        return True
    else:
        return False


text_ = input('Ввведите текст: \t')
check = palindrome(text_)
print(check)
