import urllib.request
import os



def url_open(url):
        
        headers = {
                   'Referer':'https://www.mzitu.com/',
                   'User-Agent':'Mozilla /5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
                   }
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read()

        return html
        

def get_page(url):
        html = url_open(url).decode('utf-8')
        
        a = html.find('page-numbers current') + 22
        b = html.find('<', a)
        print(html[a:b])
        return html[a:b]

def find_imgs(url):
        html = url_open(url).decode('utf-8')
        img_addrs = []
        
        a = html.find('data-original=')
        
        while a != -1:
                b = html.find('.jpg', a, a+255)
                if b != -1:
                        img_addrs.append(html[a+15
