from nltk.stem import SnowballStemmer 
russian_stemmer = SnowballStemmer('russian')

queries = ["эпл айфоны", 
           "купить эпл телефон", 
           "лучшие смартфоны", 
           "барон фон", 
           "смартфон эпл айфон", 
           "смартфоны 2019", 
           "эплан", 
           "фоновая музыка", 
           "эпл айфоны икс", 
           "эпл айфон 64гб",
           "фон для фото",
           "купить эпл",
           "эпл айфон купить",
           "эплеренон купить", 
           "смартфон где купить", 
           "эплан показания", 
           "смартфон huawei",
           "эпл"]

for query in queries:
    for word in query.split(' '):
        stemmed_word = russian_stemmer.stem(word)
        if stemmed_word == 'эпл':
            print(query)
        
