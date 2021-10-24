from lxml import etree
from io import StringIO
import requests

# Set explicit HTMLParser
parser = etree.HTMLParser()

page = requests.get('https://shamela.ws/')

# Decode the page content from bytes to string
html = page.content.decode("utf-8")

# Create your etree with a StringIO object which functions similarly
# to a fileHandler
tree = etree.parse(StringIO(html), parser=parser)

# Call this function and pass in your tree
def get_links(tree):
    # This will get the anchor tags <a href...>
    refs = tree.xpath("//a")
    # Get the url from the ref
    # links = [link.get('href', '') for link in refs]
    links = [link.get('href') for link in refs]
    # print ([link.get('') for link in refs])
    for l in refs:
        print (l.get('href', ))
        print (l.tag, l.attrib, l.text)
    # Return a list that only ends with .com.br
    # print ([l for l in links if l.find('category/') >0])
    # print (links)

# Example call
links = get_links(tree)