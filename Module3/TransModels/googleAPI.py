import os
from google.cloud import translate_v2 as translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Your Credential Here'


def google_cloud_translator(text, target):
    translate_client = translate.Client()

    result = translate_client.translate(text, target_language=target)
    return result["translatedText"]


def traduction(dataset):
    original_dataset = open(dataset, 'r')
    translated_dataset = google_cloud_translator(original_dataset.read(), 'en')
    return translated_dataset


def write_txt(text, name):
    with open(name, 'w') as f:
        f.write(text)


translated_dataset = traduction('../DataSets/europarl-v7.es-en.es')
write_txt(translated_dataset, 'google_traduction.txt')
