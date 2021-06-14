import spacy
###https://realpython.com/natural-language-processing-spacy-python/

about_text = ('Gus Proto is a Python developer currently'
                  ' working for a London-based Fintech'
                  ' company. He is interested in learning'
                  ' Natural Language Processing.')
introduction_text = ('This tutorial is about Natural Language Processing in Spacy.')



def print_token():
    nlp = spacy.load('en_core_web_sm')
    introduction_doc = nlp(introduction_text)
    # Extract tokens for the given doc
    print ([token.text for token in introduction_doc])

def print_detailed_token():
    nlp = spacy.load('en_core_web_sm')
    about_doc = nlp(about_text)
    # Extract tokens for the given doc
    print (about_text)

    # text_with_ws prints token text with trailing space (if present).
    # is_alpha detects if the token consists of alphabetic characters or not.
    # is_punct detects if the token is a punctuation symbol or not.
    # is_space detects if the token is a space or not.
    # shape_ prints out the shape of the word.
    # is_stop detects if the token is a stop word or not.
    print ('token, token.idx, token.text_with_ws,'
            'token.is_alpha, token.is_punct, token.is_space,'
            'token.shape_, token.is_stop')
    for token in about_doc:
        #print (token, token.idx)
        print(token, token.idx, token.text_with_ws,
            token.is_alpha,
            token.is_punct,
            token.is_space,
            token.shape_,
            token.is_stop)

def print_stmt():
    nlp = spacy.load('en_core_web_sm')

    about_doc = nlp(about_text)
    sentences = list(about_doc.sents)
    print (len(sentences))

    for sentence in sentences:
        ...
        print(sentence)


def set_custom_boundaries(doc):
    # Adds support to use `...` as the delimiter for sentence detection
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc


def process_stmt_ellipsis():
    ellipsis_text = ('Gus, can you, ... never mind, I forgot'
                     ' what I was saying. So, do you think'
                     ' we should ...')
    # Load a new model instance
    custom_nlp = spacy.load('en_core_web_sm')
    custom_nlp.add_pipe(set_custom_boundaries, before='parser')
    custom_ellipsis_doc = custom_nlp(ellipsis_text)
    custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
    for sentence in custom_ellipsis_sentences:
        print(sentence)
    print ('# Sentence Detection with no customization')
    nlp = spacy.load('en_core_web_sm')
    ellipsis_doc = nlp(ellipsis_text)
    ellipsis_sentences = list(ellipsis_doc.sents)
    for sentence in ellipsis_sentences:
        print(sentence)

""" -----------------------------------
    Customized Tokenization
    
nlp.vocab is a storage container for special cases and is used to handle cases like contractions and emoticons.
prefix_search is the function that is used to handle preceding punctuation, such as opening parentheses.
infix_finditer is the function that is used to handle non-whitespace separators, such as hyphens.
suffix_search is the function that is used to handle succeeding punctuation, such as closing parentheses.
token_match is an optional boolean function that is used to match strings that should never be split. It overrides the previous rules and is useful for entities like URLs or numbers.
---------------------------------------"""
def my_tokenizer():
     import re
     import spacy
     from spacy.tokenizer import Tokenizer
     custom_nlp = spacy.load('en_core_web_sm')
     prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
     suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
     infix_re = re.compile(r'''[-~]''')
     def customize_tokenizer(nlp):
         # Adds support to use `-` as the delimiter for tokenization
         return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                          suffix_search=suffix_re.search,
                          infix_finditer=infix_re.finditer,
                          token_match=None
                          )


     custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
     custom_tokenizer_about_doc = custom_nlp(about_text)
     print([token.text for token in custom_tokenizer_about_doc])



def stop_words():
    nlp = spacy.load('en_core_web_sm')
    spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
    print ('len of spacy_stopwords: ', len(spacy_stopwords))
    for stop_word in list(spacy_stopwords)[:10]:
        ...
        print(stop_word)
    #nlp = spacy.load('en_core_web_sm')
    about_doc = nlp(about_text)
    for token in about_doc:
        if not token.is_stop:
            print(token)
    print ('---------------------')
    for token in about_doc:
        if token.is_stop:
            print(token)
    print('---------------------')

    about_no_stopword_doc = [token for token in about_doc if not token.is_stop]
    print(about_no_stopword_doc)


def my_limmatization():
    nlp = spacy.load('en_core_web_sm')
    conference_help_text = ('Gus is helping organize a developer '
                            'conference on Applications of Natural Language'
                            ' Processing. He keeps organizing local Python meetups'
                            ' and several internal talks at his workplace.')

    conference_help_doc = nlp(conference_help_text)
    for token in conference_help_doc:
        print(token, token.lemma_)

def my_word_frquency():
    from collections import Counter
    complete_text = ('Gus Proto is a Python developer currently'
                               'working for a London-based Fintech company. He is'
                          ' interested in learning Natural Language Processing.'
                          ' There is a developer conference happening on 21 July'
                          ' 2019 in London. It is titled "Applications of Natural'
                          ' Language Processing". There is a helpline number '
                          ' available at +1-1234567891. Gus is helping organize it.'
                          ' He keeps organizing local Python meetups and several'
                          ' internal talks at his workplace. Gus is also presenting'
                          ' a talk. The talk will introduce the reader about "Use'
                          ' cases of Natural Language Processing in Fintech".'
                          ' Apart from his work, he is very passionate about music.'
                          ' Gus is learning to play the Piano. He has enrolled '
                          ' himself in the weekend batch of Great Piano Academy.'
                          ' Great Piano Academy is situated in Mayfair or the City'
                          ' of London and has world-class piano instructors.')

    nlp = spacy.load('en_core_web_sm')
    complete_doc = nlp(complete_text)
         # Remove stop words and punctuation symbols
    words = [token.text for token in complete_doc if not token.is_stop and not token.is_punct]
    word_freq = Counter(words)
         # 5 commonly occurring words with their frequencies
    common_words = word_freq.most_common(5)
    print(common_words)
         # Unique words
    unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
    print(unique_words)

    print('---------------------')
    words_all = [token.text for token in complete_doc if not token.is_punct]
    word_freq_all = Counter(words_all)
    # 5 commonly occurring words with their frequencies
    common_words_all = word_freq_all.most_common(5)
    print (common_words_all)
    print('---------------------')

    for token in complete_doc:
        print(token, token.tag_, token.pos_, spacy.explain(token.tag_))

my_word_frquency()