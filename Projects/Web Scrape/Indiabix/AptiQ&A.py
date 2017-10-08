from bs4 import BeautifulSoup as bs
import requests
import os

dest = r'./Aptitude'
if not os.path.exists(dest):
    print "Aptitude Folder Created"
    os.makedirs(dest)

f = open('AptiLinks.txt','r')
links = f.read().split('\n')
f.close()
#print links
#f = open('Q&A.txt','w+')

def cred():
    print '''
        https://github.com/Vinay26k/
        All copyrights related this software belongs to Vinay :)
        Mail : vinay@programmer.net
        Contact : +91-9872375950
        '''

'''
for x in links[:-1]:
    print x.split('/')[4]'''
def core(f):
    i = 1
    for url in links[:-1]:
        #print url
        r = requests.get(url).text
        soup = bs(r,'html.parser')
        fname = url.split('/')[4]+str(i)+'.txt'
        f = open(dest+'/'+fname,'w+')
        for X in soup.find_all('div',attrs={'class':'bix-div-container'}):
            for q in X.find_all('td',attrs={'class':'bix-td-qtxt'}):
                tVar = q.get_text().encode('utf-8')
                print tVar,'\n\t',
                f.write(tVar+"\n")
            for ops in X.find_all('td',attrs={'class':'bix-td-miscell'}):
                for op in ops.find_all('td',attrs={'class':'bix-td-option'}):
                    tVar= op.get_text().encode('utf-8')
                    print tVar,
                    f.write(tVar+" ")
                for ans in ops.find_all('input',attrs={'class':'jq-hdnakq'}):
                    tVar = ans['value']
                    print '\nAnswer - ',tVar
                    f.write('\nAnswer - '+tVar+'\n')
                for ansExp in ops.find_all('div',attrs={'class':'bix-ans-description'}):
                    tVar = ' '.join(ansExp.get_text().strip().split())
                    print tVar
                    f.write(tVar.encode('utf-8')+'\n\n')
        f.close()
        print fname+" Written :)"
        i += 1

core(f)
