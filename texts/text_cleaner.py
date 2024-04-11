#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import re
from nltk.corpus import stopwords
from pymystem3 import Mystem

pattern = re.compile("[^a-zA-Z0-9а-яА-ЯёЁ-]+")
stopwords_rus = stopwords.words('russian')
stemmer = Mystem()


def text_cleaner(text):
    clean_text = ' '.join(list(filter(None, [i.strip() for i in re.sub(pattern, ' ', text).lower().split(' ') if
                                             i not in stopwords_rus])))
    out = ' '.join([i for i in stemmer.lemmatize(clean_text) if i not in (' ', '\n')])
    return out
