import os
import deepl


def deepl_translator(text, target):

    auth_key = 'Your credential here'
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(text, target_lang=target)
    return result.text

# Function that translates a given dataset from any language to English


def traduction(dataset, language="EN-US"):
    original_dataset = open(dataset, 'r')
    translated_dataset = deepl_translator(original_dataset.read(), language)
    return translated_dataset

# Function that write a txt file with the translated dataset


def write_txt(text, name):
    with open(name, 'w') as f:
        f.write(text)


translated_dataset = traduction('../DataSets/europarl-v7.es-en.es')
write_txt(translated_dataset, 'deepl_traduction.txt')
