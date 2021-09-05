from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
# import ast
import concurrent.futures
import json
PATH = 'D:\drivers\chromedriver.exe'
quality = ["360", "1080"]
# wasted = []
# wasted = ['https://myflixer.today/movie/radio-america-60803', 'https://myflixer.today/movie/the-cave-60742', 'https://myflixer.today/movie/wives-on-strike-the-revolution-60723', 'https://myflixer.today/movie/trolls-world-tour-60624', 'https://myflixer.today/movie/helens-last-love-60490', 'https://myflixer.today/movie/saints-rest-60477', 'https://myflixer.today/movie/beauty-and-the-dogs-60092', 'https://myflixer.today/movie/the-school-60020', 'https://myflixer.today/movie/blood-child-59963', 'https://myflixer.today/movie/fear-love-and-agoraphobia-59956', 'https://myflixer.today/movie/all-is-foreseen-59931', 'https://myflixer.today/movie/angels-on-tap-59890', 'https://myflixer.today/movie/pondemonium-2-59818', 'https://myflixer.today/movie/a-i-tales-59772']
# wasted = ['https://myflixer.today/movie/words-and-music-53977', 'https://myflixer.today/movie/whos-your-caddy-53969', 'https://myflixer.today/movie/growing-up-and-other-lies-53961', 'https://myflixer.today/movie/the-party-53930', 'https://myflixer.today/movie/lee-evans-monsters-53921', 'https://myflixer.today/movie/the-letters-53913', 'https://myflixer.today/movie/jill-and-joys-winter-53912', 'https://myflixer.today/movie/twinkle-toes-lights-up-new-york-53911', 'https://myflixer.today/movie/me-him-her-53910', 'https://myflixer.today/movie/what-ever-happened-to-baby-jane-53901', 'https://myflixer.today/movie/ufc-196-mcgregor-vs-diaz-53900', 'https://myflixer.today/movie/body-team-12-53893', 'https://myflixer.today/movie/the-other-wife-53881', 'https://myflixer.today/movie/last-girl-standing-53879', 'https://myflixer.today/movie/hot-road-53868', 'https://myflixer.today/movie/murder-in-the-hamptons-53851', 'https://myflixer.today/movie/meet-the-deedles-53832', 'https://myflixer.today/movie/lies-my-mother-told-me-53829', 'https://myflixer.today/movie/ernest-goes-to-africa-53828', 'https://myflixer.today/movie/to-catch-a-killer-53810', 'https://myflixer.today/movie/blood-feud-53808', 'https://myflixer.today/movie/downshift-53801', 'https://myflixer.today/movie/suicide-note-53800', 'https://myflixer.today/movie/true-bloodthirst-53780', 'https://myflixer.today/movie/yosemite-53773', 'https://myflixer.today/movie/cannibal-holocaust-53758', 'https://myflixer.today/movie/the-perfect-student-53754', 'https://myflixer.today/movie/ernest-in-the-army-53715', 'https://myflixer.today/movie/lan-kwai-fong-3-53713', 'https://myflixer.today/movie/lan-kwai-fong-53711', 'https://myflixer.today/movie/from-justin-to-kelly-53693', 'https://myflixer.today/movie/frankenstein-53685', 'https://myflixer.today/movie/neanderthal-apocalypse-53657', 'https://myflixer.today/movie/alone-yet-not-alone-53586', 'https://myflixer.today/movie/half-past-dead-2-53555', 'https://myflixer.today/movie/lock-stock-and-two-smoking-barrels-53516', 'https://myflixer.today/movie/cats-eye-53444', 'https://myflixer.today/movie/curse-of-the-mayans-53407', 'https://myflixer.today/movie/strangled-53405', 'https://myflixer.today/movie/a-close-shave-53404', 'https://myflixer.today/movie/the-pirates-who-dont-do-anything-a-veggietales-movie-53397', 'https://myflixer.today/movie/in-the-mix-53323', 'https://myflixer.today/movie/summer-of-dreams-53204', 'https://myflixer.today/movie/school-spirits-52961', 'https://myflixer.today/movie/madtv-20th-anniversary-reunion-52915', 'https://myflixer.today/movie/dino-brained-52896', 'https://myflixer.today/movie/among-thieves-52876', 'https://myflixer.today/movie/51-nevada-52832', 'https://myflixer.today/movie/killer-sofa-52814', 'https://myflixer.today/movie/devils-revenge-52812', 'https://myflixer.today/movie/rogue-warfare-51649', 'https://myflixer.today/movie/the-cleansing-hour-51456', 'https://myflixer.today/movie/undercover-cheerleader-51372', 'https://myflixer.today/movie/forever-in-my-heart-51365', 'https://myflixer.today/movie/a-fire-in-the-cold-season-51335', 'https://myflixer.today/movie/already-gone-50783', 'https://myflixer.today/movie/running-with-the-devil-49980', 'https://myflixer.today/movie/american-dreamer-49973', 'https://myflixer.today/movie/nimic-49738', 'https://myflixer.today/movie/dog-town-49550', 'https://myflixer.today/movie/the-tunnel-49194', 'https://myflixer.today/movie/tito-48854', 'https://myflixer.today/movie/otherhood-48754', 'https://myflixer.today/movie/capsized-blood-in-the-water-48731', 'https://myflixer.today/movie/the-fighting-preacher-48670', 'https://myflixer.today/movie/the-demonic-dead-48655', 'https://myflixer.today/movie/rebuilding-48649', 'https://myflixer.today/movie/scoobydoo-return-to-zombie-island-48637', 'https://myflixer.today/movie/bottom-of-the-9th-48599', 'https://myflixer.today/movie/black-magic-for-white-boys-48595', 'https://myflixer.today/movie/redemption-48589', 'https://myflixer.today/movie/ring-ring-48585', 'https://myflixer.today/movie/puppy-swap-love-unleashed-48533', 'https://myflixer.today/movie/in-broad-daylight-48495', 'https://myflixer.today/movie/cargo-48478', 'https://myflixer.today/movie/a-storybook-christmas-48459', 'https://myflixer.today/movie/the-deeper-you-dig-48429', 'https://myflixer.today/movie/ruta-madre-48393', 'https://myflixer.today/movie/cult-girls-48282', 'https://myflixer.today/movie/back-of-the-net-48177', 'https://myflixer.today/movie/zoo-wars-2-48165', 'https://myflixer.today/movie/through-black-spruce-48157', 'https://myflixer.today/movie/missing-411-the-hunted-48023', 'https://myflixer.today/movie/chhota-bheem-kung-fu-dhamaka-48020', 'https://myflixer.today/movie/desolate-47983', 'https://myflixer.today/movie/aziz-ansari-right-now-47976', 'https://myflixer.today/movie/13-graves-47946', 'https://myflixer.today/movie/a-serial-killers-guide-to-life-47843', 'https://myflixer.today/movie/breaker-47822', 'https://myflixer.today/movie/hell-47759', 'https://myflixer.today/movie/iliza-shlesinger-over-and-over-47745', 'https://myflixer.today/movie/frankensteins-monsters-monster-frankenstein-47708', 'https://myflixer.today/movie/mindo-taseeldarni-47688', 'https://myflixer.today/movie/storm-over-brooklyn-47652', 'https://myflixer.today/movie/blood-money-47610', 'https://myflixer.today/movie/captain-sabertooth-and-the-magical-diamond-47549', 'https://myflixer.today/movie/a-score-to-settle-47474', 'https://myflixer.today/movie/the-trap-47422', 'https://myflixer.today/movie/theyre-inside-47418', 'https://myflixer.today/movie/the-general-47414', 'https://myflixer.today/movie/fist-and-furious-47394', 'https://myflixer.today/movie/home-47314', 'https://myflixer.today/movie/house-owner-47262', 'https://myflixer.today/movie/highwire-live-in-times-square-with-nik-wallenda-47201', 
# 'https://myflixer.today/movie/astronaut-47196', 'https://myflixer.today/movie/fluidity-47182', 'https://myflixer.today/movie/thumbaa-47179', 'https://myflixer.today/movie/tal-der-skorpione-47144', 'https://myflixer.today/movie/home-47103', 'https://myflixer.today/movie/game-changers-inside-the-video-game-wars-47085', 'https://myflixer.today/movie/casa-47075', 'https://myflixer.today/movie/tempting-fate-47048', 'https://myflixer.today/movie/reese-the-movie-a-movie-about-reese-46929', 'https://myflixer.today/movie/ganges-46847', 'https://myflixer.today/movie/father-46818', 'https://myflixer.today/movie/thamaasha-46803', 'https://myflixer.today/movie/colourblind-46790', 'https://myflixer.today/movie/the-father-46761', 'https://myflixer.today/movie/take-46752', 'https://myflixer.today/movie/nick-griffin-cheer-up-46697', 'https://myflixer.today/movie/pest-46685', 'https://myflixer.today/movie/sita-46630', 'https://myflixer.today/movie/red-nose-day-2019-46621', 'https://myflixer.today/movie/deadly-assistant-46584', 'https://myflixer.today/movie/romantic-criminals-46572', 'https://myflixer.today/movie/dada-46566', 'https://myflixer.today/movie/dying-for-a-baby-46515', 'https://myflixer.today/movie/lie-low-46502', 'https://myflixer.today/movie/99-46488', 'https://myflixer.today/movie/the-monster-46485', 'https://myflixer.today/movie/blackia-46476', 'https://myflixer.today/movie/the-world-we-make-46448', 'https://myflixer.today/movie/national-anthem-girl-46438', 'https://myflixer.today/movie/post-46420', 'https://myflixer.today/movie/hotline-46366', 'https://myflixer.today/movie/mon-jane-na-46361']
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
drivers = []
def getDrivers(n):
    for  i in range(0,n):
        i = webdriver.Chrome(PATH,options=chrome_options)
        drivers.append(i)

# print(drivers)
# driver.execute_script("window.open('');")
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[0])
# driver.execute_script("window.open('');")
# driver.execute_script("window.open('');")
# driver.execute_script("window.open('');")
# driver.execute_script("window.open('');")
# driver.execute_script("window.open('');")
def getFlixer(op):
    try:
        z = {}
        vtt = []
        genre = []
        countries = []
        producers = []
        actors = []
        sessss = requests.Session()
        # sessss.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        # sessss.max_redirects = 100
        p = sessss.get(op['url'])
        q = BeautifulSoup(p.text , 'html.parser')
        cover = str(q.select('#main-wrapper > div.detail_page.detail_page-style > div.cover_follow')[0]['style']).replace(')','(').split('(')[1]
        poster = q.select('#main-wrapper > div.detail_page.detail_page-style > div.container > div.detail_page-watch > div.detail_page-infor > div > div.dp-i-c-poster > div.film-poster.mb-2 > img')[0]['src']
        urll = op['url'].replace('movie', 'watch-movie')
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(executable_path=r'D:\drivers\chromedriver.exe',options=options)
        # done = True
        try:
            # drivers[op['number']%2-1].switch_to.window(drivers[op['number']%2-1].window_handles[op['number']%2])
            drivers[op['number']%8-1].get(urll)
            drivers[op['number']%8-1].implicitly_wait(10)
            time.sleep(3)
            # a = drivers[op['number']%2-1].find_element_by_css_selector('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > h2 > a')
            soup =  BeautifulSoup(drivers[op['number']%8-1].page_source, 'html.parser')
            a = soup.select('#iframe-embed')[0]['src']
            name = soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > h2 > a')[0].text
            rating = soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.dp-i-stats > span.item.mr-2 > button')[0].text
            trailer = soup.select('#iframe-trailer')[0]['data-src']
            sypnosis = soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.description')[0].text.strip()
            released = str(soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.elements > div > div.col-xl-5.col-lg-6.col-md-8.col-sm-12 > div:nth-child(1)')[0]).split('/span> ')[1].split(' ')[0].strip()
            for i in soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.elements > div > div.col-xl-5.col-lg-6.col-md-8.col-sm-12 > div:nth-child(2) > a'):
                genre.append(i.text)
                # print(i)
            for i in soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.elements > div > div.col-xl-5.col-lg-6.col-md-8.col-sm-12 > div:nth-child(3) > a'):
                actors.append(i.text)
            
            for i in soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.elements > div > div.col-xl-6.col-lg-6.col-md-4.col-sm-12 > div:nth-child(2) > a'):
                countries.append(i.text)
            
            for i in soup.select('#main-wrapper > div.detail_page.watch_page > div > div > div.detail_page-infor > div > div.dp-i-c-right > div.elements > div > div.col-xl-6.col-lg-6.col-md-4.col-sm-12 > div:nth-child(3) > a'):
                producers.append(i.text)
            z['cover'] = cover
            z['poster'] = poster
            # z['urll']
            z['name'] = name
            z['released'] = released
            z['trailer'] = trailer
            z['rating'] = rating
            z['sypnosis'] = sypnosis
            z['genre'] = genre
            z['actors'] = actors
            z['producers'] = producers
            z['countries'] = countries
            if a == '':
                # print("tf happened ")
                return(op['url'])
            else:
                response = requests.get(a)
                soup1 = BeautifulSoup(response.text, "html.parser")
                for i in str(soup1.select('body > script')).split('\n')[2][17:-1].replace('}', '{').split('{'):
                    if 't' in i:
                        vtt.append({
                            i.split(',')[1].split(':')[1][1:-1] : i.split(',')[0][8:-1].replace('\/', '/')
                        })
                
                m3u8 = (
                    str(soup1.select("body > script"))
                    .split("\n")[1]
                    .split('"file":')[1]
                    .split('"')[1]
                    .replace("\/", "/")
                )
                z['url'] = a    
                z['m3u8'] = m3u8
                z['vtt'] = vtt
                # print(p720)
                # for i in quality:
                #     x = requests.head(p720.replace('720',i))
                #     if x.ok:
                #         tracks.append(i)
                #     try:
                #         r = s.get(p720.replace("720", i))
                #         tracks.append(i)
                #     except requests.ConnectionError as exception:
                #         continue
                # try:
                #     f.write(str(z)+'\n')
                #     print(z)
                # except:
                #     return z
                # print('asdasdsa')
                # print(z['name'])
                return z
                # drivers[op['number']%2-1].close()
                # y = y+1
                # print(y)
                # done = True
                # driver.execute_script("window.open('');")

                # print(tracks)
        except:
            # driver.close()
            return a
    except:
        return op['url']
    # driver.close()
# y = 0
def getFmovies():
    for j in range(226,400):
        op = []
        m = requests.get('https://myflixer.today/movie?page='+str(j))
        n = BeautifulSoup(m.text, 'html.parser')
        for i in n.select('#main-wrapper > div > section > div.block_area-content.block_area-list.film_list.film_list-grid > div > div')[0:-1]:
            mov = str(i).split('href="')[1].split('"')[0]
            string = 'https://myflixer.today'+mov
            op.append({'url':string, 'number':len(op)})
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            for i in executor.map(getFlixer,op):
                if isinstance(i, str)==False: 
                    json.dump(i, outfile, indent=4)
                    outfile.write(',\n')
                    # print(i['name'])
                else:
                    wasted.append(i)
        print(j)
        print(wasted)
# f = open('flix.txt', 'a')
# s = f.readline()
# print(ast.literal_eval(s)['cover'])
with open("flix.json", "a") as outfile:
    getDrivers(8)
    getFmovies()
outfile.close()