#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Akshay
#
# Created:     15-05-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def get_link(page, start_pos):
    """
    Extracts the next link after start_link and returns (url,end_quote)
    Returns (None, -1) if no link found.
    """
    pos = page.find('<a href=',start_pos)
    if not (pos == -1):
        start_quote = page.find('"',pos+1)
        end_quote = page.find('"',start_quote + 1)
        url = page[start_quote+1:end_quote]
        return (url, end_quote)

    else:
        return (None,-1)


def get_all_links(page):
    """
    Returns a list of all urls from page
    """
    pos = 0
    urls = []
    while True:
        url,end_pos = get_link(page,pos)
        pos = end_pos
        if url:
            urls.append(url)
        else:
            break
    return urls


def crawl_web(seed,max_depth=-1):
    #make it breadth_first search
    tocrawl = [(seed,0)]
    crawled = []

    while tocrawl:
        (page,depth) = tocrawl.pop(0)
        if(not (max_depth == -1) and depth > max_depth):
            break

        if(page not in crawled):
            links = get_all_links(get_page(page))
            links = [t for t in links if t not in crawled]
            links = [(t,depth+1) for t in links]

            tocrawl += links
            crawled.append(page)


        #page = tocrawl.pop()
        #if page not in crawled:
         #   union(tocrawl, get_all_links(get_page(page)))
         #   crawled.append(page)


    return crawled

def main():
    print crawl_web('https://www.udacity.com/cs101x/index.html')
    print crawl_web('https://www.udacity.com/cs101x/index.html',1)

if __name__ == '__main__':
    main()
