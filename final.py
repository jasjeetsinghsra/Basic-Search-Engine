def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
    
def get_next_target(page):
    start_link=page.find('<a href=')
    if start_link==-1:
        return None, 0
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(page_content):
    while True:
        url, endpos=get_next_target(page_content)
        if url:
            print url
            page_content=page_content[endpos:]
        else:
            break
        
    #url,endpos=get_next_target(page)
    #while url !=None:
     #   print url
      #  page=page[endpos:]
       # url,endpos=get_next_target(page)

def get_all_links(page_content):
    links=[]
    while True:
        url, endpos=get_next_target(page_content)
        if url:
            links.append(url)
            page_content=page_content[endpos:]
        else:
            break
    return links
        
    #url,endpos=get_next_target(page)
    #while url !=None:
     #   print url
      #  page=page[endpos:]
       # url,endpos=get_next_target(page)

def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)

def crawl_web(seed):
    to_crawl=[seed]
    crawled=[]
    index=[]
    while to_crawl:
        page=to_crawl.pop()
        if page not in crawled and len(crawled)<10:
            content=get_page(page)
            add_page_to_index(index,page,content)
            union(to_crawl, get_all_links(content))
            crawled.append(page)
    return index, crawled

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0]==keyword:
            if url not in entry[1]:
                entry[1].append(url)
                return
    index.append([keyword,[url]])
    
def add_page_to_index(index,url,content):
    words=content.split()
    for word in words:
        add_to_index(index,word, url)
        
def lookup(index,keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return []

import time

def exe_time(code):
    start_time=time.clock()
    res=eval(code)
    run_time=time.clock()-start_time
    return res,run_time
    
index, crawled= crawl_web('http://xkcd.com/554')    
    
print exe_time('lookup(index,"safer,")')

#print 'index is: \n', index
#print '\n crawled is: \n', crawled
#print 'lookup results: \n', lookup(index,'var')
#print '\n The process has finished'
