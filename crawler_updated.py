
d = 0.8

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
    if keyword not in index:
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
    index = {}
    graph = {}
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
            graph[current_url] = links

    return index,graph




def compute_ranks(graph):
    inlinks = {}

    prev_ranks = {}
    ranks = {}
    num_pages = len(graph)

    for key in graph:
        inlinks [key] = []
        prev_ranks = 1/num_pages

    for key in graph:
        for url in graph[key]:
            inlinks[url].append(key)

    time_step = 10
    t = 0
    while t <= time_step:
        for url in graph:
            res = 0.0
            for link in inlinks[url]:
                res = res + prev_ranks[link]/len(graph[link])
            res = res*d

            res = res + (1 - d)/num_pages
            ranks[url] = res
            prev_ranks = ranks
        t += 1
    return ranks

def quick_sort(p):
    if len(p) <= 1:
        return p
    splitter = p.pop(0)
    lesser = [x for x in p if x[1] < splitter[1]]
    greater = [x for x in p if x[1] >= splitter[1]]
    return quick_sort(lesser)+[splitter]+quick_sort(greater)


def ordered_search(index, ranks, keyword):
    if keyword not in index:
        return None
    urls = index[keyword]
    t = [(u, ranks[u]) for u in urls]
    t = quick_sort(t)
    return [u[0] for u in t]



def best_lookup(index, keyword, ranks):
    if keyword in index:
        urls = index[keyword]
        rank_stuff = []

        for url in urls:
            rank_stuff.append(ranks[url])

        maximum = 0
        for i in range(len(rank_stuff) - 1):
            p = i+1
            if rank_stuff[p] > rank_stuff[maximum]:
                maximum = p
        return urls[minimum]
    else:
        return None

def main():
    l1,g1 = crawl_web('https://www.udacity.com/cs101x/index.html')
    print l1

    l2,g2 = crawl_web('https://www.udacity.com/cs101x/index.html',0)
    print l2

    print len(l1)
    print len(l2)

    print l1['Ossifrage!']


if __name__ == '__main__':
    main()





