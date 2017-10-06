import urlparse
import sys,urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import getinfo


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def play_video(path):
    
    play_item = xbmcgui.ListItem(path=path)

    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

mode = args.get('mode', None)


if mode is None:
    resp = getinfo.urllib2.urlopen('http://kekzdee.github.io/Repos/moviedatabase.txt')
    exec(resp.read())
    xbmcplugin.endOfDirectory(addon_handle)


elif mode[0] == 'play':
    final_link = args['playlink'][0]
    final_link = getinfo.get_url(final_link)
    play_video(final_link)
