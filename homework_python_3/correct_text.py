text = str(input('Введите ваше текст:'))
text_correct: str
text_correct = (text .lower())  # Переводим текст в нижний регистр
text_correct = text_correct + ' '  # Прибавляем к строке пробел, чтобы проверить "черт" в конце текста
text_correct = text_correct .replace('черт ', '#### ')  # Проверяем "черт" в начале текста
text_correct = text_correct .replace(' черт ', ' #### ')  # Проверяем "черт" в середине текста
# Делаем срез от начала строки и до конца, без последнего элемента (убираем пробел в конце строки)
text_correct = text_correct[:-1]
print(text_correct)
