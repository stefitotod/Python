# Напишете програма с функция, която получава един текстов аргумент и произволен брой числови аргумети.
# Резултатът от функцията се явява текст, сформиран от буквите на първия текстов аргумент.
# Целочислените аргументи определят индексите на буквите, които трябва да влизат в текстови резултати.

def my_function(text,*nums):
    result = ""
    for i in nums:
        if i < len(text):
            result += text[i]  
    return result

print(my_function("random text",1,2,3,4))
