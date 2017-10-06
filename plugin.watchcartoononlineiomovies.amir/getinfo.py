import urllib
import re
import urllib2

def get_url(url):
    _VALID_URL = r'(?:https://)?(?:www\.)?watchcartoononline\.io/([^/]+)'
    #checks if url is valid
    if re.match(_VALID_URL, url) is not None:
        #sets user_agent so watchcartoononline doesn't cause issues
        user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1'
        headers = { 'User-Agent' : user_agent }
        
        print "[watchcartoononline-dl]  Downloading webpage"
        request = urllib2.Request(url,headers=headers)
        webpage = urllib2.urlopen(request).read()
    
        print "[watchcartoononline-dl]  Finding video"
        video_url = re.search(r'<iframe [^>]*src="https://www.watchcartoononline.io/inc/(.+?)>', webpage).group()
        video_url = re.search('src="(.+?)"', video_url).group(1).replace(' ','%20')
        
        # "clicks" the "Click Here to Watch Free" button to so it can access the actual video file url
        #print "[watchcartoononline-dl]  Clicking stupid 'Watch Free' button"
        params = urllib.urlencode({'fuck_you':'','confirm':'Click Here to Watch Free!!'})
    
        print "[watchcartoononline-dl]  Getting video URL"
        request = urllib2.Request(video_url,params,headers=headers)
        video_webpage = urllib2.urlopen(request).read()
        #scrapes the actual file url
        final_url =  re.findall(r'file: "(.+?)"', video_webpage)
        #throws error if list is blank
        if not final_url:
            print "ERROR: Video not found"
        else:
            return final_url[0]

if __name__ == "__main__":
    print get_url("https://www.watchcartoononline.io/big-hero-6")

    # ^^ test ^^ #
