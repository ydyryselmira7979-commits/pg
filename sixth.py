import sys
import requests

def download_url_and_get_all_hrefs(url):
    r = requests.get(url)
    if r.status_code != 200:
        return []
    
    t = r.text
    out = []
    i = 0
    
    search_string = 'href="' 
    search_len = len(search_string)
    
    while True:
        i = t.find(search_string, i)
        if i == -1:
            break
            
        i += search_len
        
        j = t.find('"', i)
        
        if j != -1:
            out.append(t[i:j])
            i = j + 1
        else:
            break
            
    print(out)
    return out

if __name__ == "__main__":
    try:
        download_url_and_get_all_hrefs(sys.argv[1])
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
