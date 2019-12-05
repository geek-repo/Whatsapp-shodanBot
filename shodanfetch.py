from shodan import Shodan
import re

api = Shodan('XXXXXXXXXXXXXXXXXXX')



def final(query,level):
        if level=='1':
            return (api.search(query,page=2,limit=10, offset=None, facets=None, minify=True))
        elif level=='2':
            return (api.search(query,page=None,limit=None, offset=None, facets=None, minify=True))
        elif level=='3':
            return (api.search(query,page=15,limit=None, offset=8, facets=None, minify=True))
        else:
            return("ERROR!!!!")        

def sh(query,resp):
    level='1'
    if re.findall("--level\s[0-3]",query):
        level=str(re.findall("--level\s[0-3]",query)[0].replace("--level ",""))
        query=query.replace("--level {}".format(level),"")
        #print (query)
        out=final(query,level)
        for i in out['matches']:
            resp.message("{}\n".format(("IP: {}\nOS: {}\nISP: {}\nPostal Code: {}\nCity Name: {}\nCountry Name: {}".format(i['ip_str'],i['os'],i['isp'],i['location']['postal_code'],i['location']['city'],i['location']['country_name']))))
        return resp    
    else:
        if re.findall("--level\s[0-9]",query):
            level=str(re.findall("--level\s[0-9]",query)[0].replace("--level ",""))
            query=query.replace("--level {}".format(level),"")
            #print(query)
        out=final(query,'1')
        #print(query)
        for i in out['matches']:
            resp.message("{}\n".format(("IP: {}\nOS: {}\nISP: {}\nPostal Code: {}\nCity Name: {}\nCountry Name: {}".format(i['ip_str'],i['os'],i['isp'],i['location']['postal_code'],i['location']['city'],i['location']['country_name']))))
        return resp