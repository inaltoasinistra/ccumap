#!/usr/bin/env python2

USERS_URL = 'http://criticalcity.org/users?page=%d'
USERMAP_URL = 'http://criticalcity.org/locations/user_map?id='
# http://criticalcity.org/locations/?show=users

import re
import urllib2

def main():
    print get_users()


'''
<a class="featured_item featured_user" href="/users/10971">
        <img alt="20080703-arte-di-mettersi-le-dita-ne" class="bg_image" src="http://s3.amazonaws.com/criticalcity/avatars/10971/featured/20080703-arte-di-mettersi-le-dita-ne.jpg" />
        
        <div class="info bg">
                <h1>755 <span>Punti</span></h1>
'''

re_users = re.compile('/users/(\d+).*?(\d+)[\s\n]*\<span>Punti',re.MULTILINE|re.DOTALL)
# re.findall(re_users,s)

def get_users():
    
    stop = False
    page = 1
    users = set()

    while True:
        print page
        for u,p in get_and_parse(USERS_URL % page, lambda x: re.findall(re_users, x)):
            u = int(u)
            p = int(p)
            if p:
                users.add(u)
            else:
                stop = True

        if stop:
            break
        page += 1

    return users

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
def get_and_parse(url,parse,err='err'):

    if not parse:
        parse = lambda x: x

    try:
        data = opener.open(url).read()
        #data = urllib2.urlopen(url).read()
    except urllib2.HTTPError:
        return err
    else:
        return parse(data)

if __name__=="__main__":
    main()
