 = [     11111   ]
waittime=0.015 #It checks every hour
import datetime

from pyquery import PyQuery as pq
import mechanize
import cookielib
import re
import getpass
import time
kkk
fangni gueen
fangnimaheipi
ziya
zi ya 
def getCourse(browser,crn):
    response = browser.open("https://ui2web1.apps.uillinois.edu/BANPROD1/bwckschd.p_disp_detail_sched?term_in=120168&crn_in="+str(crn))
    cls = pq(response.read())("table.datadisplaytable tr")
    #print pq(cls[0]).text()
    result = {}
    result["description"] = pq(cls[0]).text()
    try:
        result["capacity"]=[int(pq(pq(cls[3])("td")[0]).text()),int(pq(pq(cls[5])("td")[0]).text())]
        result["actual"]=[int(pq(pq(cls[3])("td")[1]).text()),int(pq(pq(cls[5])("td")[1]).text())]
        result["remaining"]=[int(pq(pq(cls[3])("td")[2]).text()),int(pq(pq(cls[5])("td")[2]).text())]
    except:
        result["capacity"]=[int(pq(pq(cls[3])("td")[0]).text()),1]
        result["actual"]=[int(pq(pq(cls[3])("td")[1]).text()),1]
        result["remaining"]=[int(pq(pq(cls[3])("td")[2]).text()),1]
    return result
#Set booleans for each course: Are seats available?
available = [False]*len(courses)
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
# br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Chrome')]
from selenium import webdriver

you mo!

while (True):
    print "----------------------------------"
    flag = True
    for i in xrange(len(courses)):
        crn = courses[i]
        res = getCourse(br,crn)
        # print res["description"],
        x = res["remaining"]
        if x[0] > 0 and x[1] > 0:
            continue
        else:
            flag = False
            break
    if (flag is True):
        browser = webdriver.Firefox()
        browser.get('https://apps.uillinois.edu/selfservice/')
        uiuc = browser.find_element_by_xpath("//div[@class='row2']//ul[1]/li[3]/a")
        browser.get(uiuc.get_attribute('href'))
        username = browser.find_element_by_id("ENT_ID")
        password = browser.find_element_by_id("PASSWORD");
        username.send_keys("账号")
        password.send_keys("密码")
        button = browser.find_element_by_xpath("//input[@name='BTN_LOGIN']")
        button.click()
        register = browser.find_element_by_xpath("//tbody/tr[3]/td[2]/a")
        register.click()
        browser.find_element_by_xpath("//tbody/tr[1]/td[2]/a").click()
        browser.find_element_by_partial_link_text("Add/Drop Classes").click()
        browser.find_element_by_partial_link_text("I Agree").click()
        browser.find_element_by_xpath("//option[@value='120168']").click()
        browser.find_element_by_xpath("//input[@value='Submit']").click()
        for i in xrange(len(courses)):
            CRN = browser.find_element_by_id("crn_id"+str(i+1))
            CRN.send_keys(str(courses[i]))

        browser.find_element_by_xpath("//input[@value='Submit Changes']").click()
        break;
    else:
        print datetime.datetime.now()
        continue
    time.sleep(waittime)


