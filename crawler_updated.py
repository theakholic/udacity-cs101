
def get_page(url):
    """
    Return the content from the url as a string.

    Keyword arguments:
        url -- string containing url of page.

    Returns:
        content -- string containing content of page. Empty string returned if error.
    """

    try:
        import urllib
        content = urllib.urlopen(url).read()
        return content
    except:
        return ''

def get_next_link(content, start):
    """
    Return the next link and end_quote from the page.
    """

    start_link = content.find('<a href=', start)
    if (start_link == -1):
        return (None,-1)
    start_quote = content.find('"',start_link)
    end_quote = content.find('"',start_quote+1)
    link = content[start_quote+1 : end_quote]
    return (link,end_quote)


def get_all_links(content):
    """
    Return all the links from the page as a list.
    """
    links = []
    start = 0

    while True:
        current_link,start = get_next_link(content,start)
        if current_link:
            links.append(current_link)
        else:
            break
    return links


def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None


def add_to_index(index, keyword, url):
    """
    Add the keyword to index.
    """
    #update the dict
    if not lookup(index, keyword):
        index[keyword] = [url]
    else:
        index[keyword].append(url)


def add_page_to_index(index, url, content):
    """
    Add all keywords from page into index.

    Keyword arguments:
        index -- dictionary that is the inverted index of keywords and associated urls.
        url -- the url whose content is to be added to index.
        content -- associated content.
    """
    words = content.split()
    for keyword in words:
        add_to_index(index, keyword, url)



def union(p,q):
    """ Perform set union of p and q and store in p."""
    for e in q:
        if e not in p:
            p.append(e)


def crawl_web(seed, max_depth = -1):
    """
    Crawl reachable webpages and return inverted index of keyword and urls.

    Keyword arguments:
        seed -- string containing url of seed.
        max_depth -- maximum depth of search. If not reqd, defaults to -1.

    Returns:
        index -- inverted index implemented as dictionary
    """
    to_crawl = [(seed,0)]
    tc = [seed]
    crawled = []
    index = dict()

    use_depth = True
    if max_depth == -1:
        use_depth = False

    while to_crawl:
        #pop from the beginning. popping from end results
        #in a depth first traversal
        current_url,current_depth = to_crawl.pop(0)
        if use_depth and current_depth > max_depth:
            break
        temp = tc.pop(0)
        if current_url not in crawled:
            #1) get the content
            content = get_page(current_url)

            #2) get all links from content
            links = get_all_links(content)

            #3) add them to to_crawl with appropriate depth and ensure uniqueness.

            union(tc,links)
            x = len(tc) - len(to_crawl)
            y = len(to_crawl)
            for i in range(x):
                to_crawl.append((tc[y+i], current_depth + 1))
            #4)add current_url to crawled
            crawled.append(current_url)

            #5)add this page to the index
            add_page_to_index(index,current_url,content)

    return index



def main():
    l1 = crawl_web('https://www.udacity.com/cs101x/index.html')
    print l1

    l2 = crawl_web('https://www.udacity.com/cs101x/index.html',0)
    print l2

    print len(l1)
    print len(l2)

    print l1['Ossifrage!']


if __name__ == '__main__':
    main()





