# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(n, flag=True):
    """Returns n jokes"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    if not flag:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for i, (noun, adverb, adjective) in enumerate(zip(nouns, adverbs, adjectives)):
            joke.append(f'{noun} {adverb} {adjective}')
            if i == n:
                break
    else:
        for _ in range(n):
            joke.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return joke


print(get_jokes(2))
