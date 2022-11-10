from nltk.translate.bleu_score import sentence_bleu


def bleu_score():
    ref = [
        'this is moonlight'.split(),
        'Look, this is moonlight'.split(),
        'moonlight it is'.split()
    ]
    test = 'it is moonlight'.split()
    print('BLEU score for test-> {}'.format(sentence_bleu(ref, test)))

    test01 = 'it is cat and moonlight'.split()
    print('BLEU score for test01-> {}'.format(sentence_bleu(ref, test01)))


translate_text("cat", "continual-bay-368200")
