from utilities.connection import Connect
from utilities.proxies import Proxy
from httpmethods import Methods

class Scraper(Connect, Proxy):
    def __init__(self):
        Connect.__init__(self)

    # def
# test = Scraper()
# test.HTTP_mode = Methods.GET
# test.url = "https://api.github.com/users/mralexgray/repos"
# test.fetch()


# test = Scraper()
# test.HTTP_mode = Methods.GET
# test.url = "https://www.dnsdynamic.org"
# test.fetch()
#
# test.HTTP_mode = Methods.POST
# test.url = "https://www.dnsdynamic.org/auth.php"
# test.parameters = {'email': 'alexander.ward1@gmail.com',
#                    'pass': 'alex3412'}
# test.headers = {}
# test.fetch()


test = Scraper()
test.HTTP_mode = Methods.GET
test.url = "http://imgsv.imaging.nikon.com/lineup/lens/zoom/normalzoom/af-s_dx_18-140mmf_35-56g_ed_vr/img/sample/sample1_l.jpg"
test.fetch()
