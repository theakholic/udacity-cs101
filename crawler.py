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

def lookup(index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    return []


def add_to_index(index, keyword,url):
    for e in index:
        if e[0] == keyword:
            ###if url not in e[1]:
                e[1].append(url)
                return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    """
    Add page to inverted index. String url, string content.
    """
    for c in content.split():
        add_to_index(index,c,url)

def split_string(source, split_list):
    res = []
    split_point = True
    for c in source:
        if c in split_list:
            split_list = True
        else:
            if split_point:
                #NEW WORD ONLY IF FROM SPLIT POINT TO NORMAL POINT
                output.append(c)
                split_point = False
            else:
                output[-1] += c


##def crawl_web(seed,max_depth=-1):
##    #make it breadth_first search
##    tocrawl = [(seed,0)]
##    crawled = []
##
##    while tocrawl:
##        (page,depth) = tocrawl.pop(0)
##        if(not (max_depth == -1) and depth > max_depth):
##            break
##
##        if(page not in crawled):
##            links = get_all_links(get_page(page))
##            links = [t for t in links if t not in crawled]
##            links = [(t,depth+1) for t in links]
##
##            tocrawl += links
##            crawled.append(page)
##
##
##        #page = tocrawl.pop()
##        #if page not in crawled:
##         #   union(tocrawl, get_all_links(get_page(page)))
##         #   crawled.append(page)
##
##
##    return crawled
def special_union(p,q):
    for e in q:
        flag = True
        for w in p:
            if e[0] == w[0]:
                flag = False
                break
        if flag:
            p.append(e)

##def crawl_web(seed, max_depth = -1):
##    to_crawl = [(seed,0)]
##    crawled = []
##    index = []
##    depth = 0
##    i = 0
##    while to_crawl:
##        #i+=1
##        #if i == 5:
##           # break
##        if (depth > max_depth) and not (max_depth == -1):
##            break
##        (current_url,depth) = to_crawl.pop(0)
##        #print 'Here: ', current_url
##        content = get_page(current_url)
##        links = get_all_links(content)
##        #print links
##        links = [(p,depth + 1) for p in links]
##        #print links
##        special_union(to_crawl,links)
##
##        add_page_to_index(index,current_url,content)
##        crawled.append(current_url)
##
##    return index

def union(p,q):
    for c in q:
        if c not in p:
            p.append(c)
    #print p

def crawl_web_alt(seed,max_depth=-1):
    to_crawl =[(seed,0)]
    to_crawl_plan = [seed]
    crawled = []
    index = []
    use_depth = True
    if max_depth == -1:
        use_depth = False
    curr_depth = 0
    while to_crawl:

        (current_url,curr_depth) = to_crawl.pop(0)
        if use_depth:
            if curr_depth > max_depth:
                break
        t = to_crawl_plan.pop(0)
        if current_url not in crawled:
            content = get_page(current_url)

            links = get_all_links(content)
            union(to_crawl_plan,links)
            t = len(to_crawl_plan) - len(to_crawl)
            x = len(to_crawl)
            for i in range(t):
                to_crawl.append((to_crawl_plan[x + i],curr_depth+1))
    ##            except IndexError, e:
    ##                print i
    ##                print len(to_crawl)
    ##                print e
    ##                raise IndexError


            add_page_to_index(index,current_url,content)
            crawled.append(current_url)
    return index

def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    index = []
    while to_crawl:
        #print to_crawl
        page = to_crawl.pop(0)
        #print to_crawl
        content = get_page(page)
        #page is a url
        #to_crawl is a list of urls

        if page not in crawled:
            links = get_all_links(content)
            union(to_crawl,links)
            #print to_crawl
            add_page_to_index(index,page,content)
            crawled.append(page)
    return index





def main():
    l1 = crawl_web('https://www.udacity.com/cs101x/index.html')
    l1 = sorted(l1)
    print l1
    print "\n\n\n"
    l2 = crawl_web_alt('https://www.udacity.com/cs101x/index.html')

    l2 = sorted(l2)
    print l2
    #print (('https://www.udacity.com/cs101x/index.html',1)
    #max depth
    l3 = crawl_web_alt('https://www.udacity.com/cs101x/index.html',0)
    print l3

##    print l1 == l2

##    print len(l1)
###   print len(l2)
##
##
##    print c1
    #print c2

if __name__ == '__main__':
    main()
