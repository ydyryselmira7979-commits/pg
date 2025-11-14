import sys
import requests

def download_url_and_get_all_hrefs(url):
    r = requests.get(url)
    if r.status_code != 200:
        return []
    t = r.text
    out = []
    i = 0
    while True:
        i = t.find('<a href="', i)
        if i == -1:
            break
        i += 9
        j = t.find('"', i)
        out.append(t[i:j])
    print(out)
    return out

if __name__ == "__main__":
    try:
        download_url_and_get_all_hrefs(sys.argv[1])
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
