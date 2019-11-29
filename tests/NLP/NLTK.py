def test1():
    import nltk
    sentence = """At eight o'clock on Thursday morning
    ... Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    print (tokens)
    tagged = nltk.pos_tag(tokens)
    print (tagged[0:6])


def plot_freq():
    from bs4 import BeautifulSoup
    import urllib.request
    import nltk
    from nltk.corpus import stopwords
    stopwords.words('english')

    response = urllib.request.urlopen('http://php.net/')
    html = response.read()
    soup = BeautifulSoup(html, "html5lib")
    text = soup.get_text(strip=True)
    tokens = [t for t in text.split()]
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

    freq = nltk.FreqDist(tokens)
    for key, val in freq.items():
        print(str(key) + ':' + str(val))

    freq.plot(20, cumulative=False)

def twitter_token():
    from nltk.corpus import twitter_samples
    from nltk.tag import pos_tag_sents

    tweets = twitter_samples.strings('positive_tweets.json')
    tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

    tweets_tagged = pos_tag_sents(tweets_tokens)
    """
    JJ:Adjective
    singular nouns (NN)
    plural nouns (NNS)
    
    """
    JJ_count = 0
    NN_count = 0

    for tweet in tweets_tagged:
        for key, tag  in tweet:
            #tag = pair[1]
            if tag == 'JJ':
                JJ_count += 1
            elif tag == 'NN':
                NN_count += 1

    print('Total number of adjectives = ', JJ_count)
    print('Total number of nouns = ', NN_count)

def my_tokinize():
    from nltk.tokenize import sent_tokenize, word_tokenize
    mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

    #for t in sent_tokenize(mytext, 'Arabic'):
    for t in sent_tokenize(mytext):
        print(t)

    #for w in word_tokenize(mytext, 'Arabic'):
    for w in word_tokenize(mytext):
        print (w)

def my_wornet():
    from nltk.corpus import wordnet

    syn = wordnet.synsets("pain")

    print(syn[0].definition())

    print(syn[0].examples())

def my_wordnet_lemma():
    from nltk.corpus import wordnet

    synonyms = []

    for syn in wordnet.synsets('Computer'):

        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            print (lemma.name())

    print(synonyms)
#plot_freq()
#twitter_token()
#my_tokinize()
#my_wornet()
my_wordnet_lemma()