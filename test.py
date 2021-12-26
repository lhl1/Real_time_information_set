import tkinter as tk
import requests
import re
from lxml import etree
import subprocess
import _thread
import time

cmd = 'your command'
res = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
window = tk.Tk()
window.title("LHL's Information")
window.iconbitmap('favicon.ico')
window.geometry("1500x1000")

flag = ''
delay_time=62

def delete_text():
    global str1
    t.delete(1.0, 'end')
    str1 = ''



def weibo(threadName, delay):
    global flag
    flag='weibo'
    while flag=='weibo':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'https://s.weibo.com/top/summary'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        cnt = 1
        titles = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
        str1 = ''
        t.delete(1.0, 'end')
        t.insert("end",'                     微博Top50' + "       " + time.strftime("%H:%M:%S", time.localtime())+'\n\n')

        # lhlhlhlhl罗宏亮
        for i in titles:
            title = i.xpath('./td[2]/a/text()')[0]
            num = i.xpath('./td[1]/text()')
            if (len(num) > 0):
                num_print = num[0]
            else:
                num_print = '置顶'
            url = 'https://s.weibo.com' + i.xpath('./td[2]/a/@href')[0]
            url = 'https://s.weibo.com' + i.xpath('./td[2]/a/@href')[0]
            t.insert("end", "  "+num_print + '.   ' + title + '\n\n')

            cnt = cnt + 1

        t.insert(1.0, str1)
        time.sleep(delay_time)
def start_weibo():

    try:
        _thread.start_new_thread(weibo, ("weibo", 0))
    except:
        print("Error: 无法启动线程")

def baidu_time(threadName, delay):
    global flag
    flag='baidu_time'
    while flag=='baidu_time':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }

        url = 'https://top.baidu.com/board?tab=realtime'
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                     LHL's Baidu Top            ") +  time.strftime("%H:%M:%S", time.localtime())+'\n\n'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        titles = tree.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div')
        cnt = 1

        for i in titles:

            title = i.xpath('./div[2]/a/div[1]/text()')

            if (len(title) > 1):
                str1 = str1 + ("  "+str(cnt) + ".  " + "    直播中：" + title[1]) + '\n\n'
            else:
                str1 = str1 + ("  "+str(cnt) + ".  " + title[0]) + '\n\n'
            # print(str(cnt)+".  "+title)
            # print()

            cnt = cnt + 1
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_baidu_time():
    try:
        _thread.start_new_thread(baidu_time, ("baidu_time", 0))
    except:
        print("Error: 无法启动线程")



def zhihutop(threadName, delay):
    # lhlhlhlhl罗宏亮
    global flag
    flag='zhihutop'
    while flag=='zhihutop':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'cookie': '_zap=dad143a7-35e4-46c6-8825-919a78caa1f0; _xsrf=6v5ElWESwWsSsCI20UDgqqhHEhYxGoDn; d_c0="AFBQ5xef_xOPTi60j67vxkMWNkhm2SZf5cg=|1636351980"; captcha_session_v2="2|1:0|10:1636351981|18:captcha_session_v2|88:UzJwRkoxeFNNYngvdFVIUDN1Ykx2YWpkMkV4K1gwWkJaMGtBd245RnJ4Sm9IVGd2a3g5QjEwSXQzaUJ6TWdSdg==|5e740995cbb85969429ac01ba047fee68cf4c43558fa792b4988844ad50bc8ce"; __snaker__id=NjmbuhyUPcomkN0R; gdxidpyhxdE=T22%2BW%2Fh0bcM31kzrBWcICTOoKniKT4HXdI%5CMQw1e6pPK57HE5ZR7S1eeXxzU92E9IXaMkEmLD%2Bj%2FXyJsK8A%5CAm8xiKDqz4rNYSyWD%2BsbLlzASss%2BcKS5IamYtZB1Ak2kg5zXJ%2BmKZtghgVBhHwjiB%2BH4JNokD6nPbWLk4TI168dTwyfI%3A1636352882192; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=UqijRSCLTbkPImSIXu%2BIU40xafBLwh0srev6gFbrf7RVJEn84JFgL%2BlCawKr5syYGyLsjRPocMwVP1EyRHdDy0Ex9pR89y6%2B7AA6CNlmNgCR3GqtQBMiXxg8JJaWLKt1bG4%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee88e17ab69b84adee7ff3b08bb6c15a978e8b85f1808daafba5ce41a3ad8da3ae2af0fea7c3b92a97afa78bd15981949c83ea5c8bb39daadb7fe9979bd5b374a3ba8eadf664f4adbe86f53ea59aae93e53d928a86a6ed34f8968a88cf21b09daf98ca7af7adb7bac67390ada6b3d365a193b9b7d33b87a79ea9e750bbf08b99bc7c92e8f79ab521f59f8fd7c246b0b38288c25af199bf95d44a8fb79899e6348a96afb8cf41b8efaea8b737e2a3; YD00517437729195%3AWM_TID=O44%2FxDTeZYNFVRQQURJr8PFTUo%2FtY4CW; captcha_ticket_v2="2|1:0|10:1636351987|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfWUl1VUYwNGZLekdWeGpaMTdsc0kxN29qQWxFQ2pjUVE2YjdfLkpYbUQ3OTRlQTRuOUJQSktqLVA4TmR6em5NMENlNHRMLjVxSkRWenRMSEU5bmpWbzFPWk1uaDRKWTRnOWxxLTRGN3p4TUM2U0dHWldSU3B6UEdmcHhWa0FlZmFWR0d1ejdmMmZQa3R0MDdiOGJKYTlQaGdHQl9MV2dXU1ZyemQ3cHdzLjJpRUVSLVFJVE9SU0E3Xy5ES0R4TlQySlktQnI2d09SSk1lNm9YLU10MTAtME9YeGpkVVF4cEFKbjA2TklhLTFveTkxejhLS1VuZldqbWtDaDQ2RWtBTmpiMERQelJabFg4ZVBXLU5kN0xLei1wT2xtSko0LmdndlBHU2lKaWpDckxoTlFtamtyR3Y2WmNROGs1em91NVBUQ2IxTzhDLm94bG81c2xmcWJPS2ZDT0ZZeDZCYXFtbGtVNXpHektZd24wOUlnXzFONVZZZFRQTGxkNmpPMVUtRVVPa000Z19QLjZvZ1RhZ1V6dmk5MXY4dHM2SUM5UkJ3cC1BU0MuQ1RWX25mLnlRcVRfYkEwT3BFS1pabG1mWWlQMEMxUlBQVlB5YmFaWDR3VWFMbGs0NktUVjZjSGNGeDhmUDdQNm96NTA2TXR0WURRNWZGSGV1U0JpMyJ9|895d8c8b5d6e65a175fac0f9ed228f0dbd8622422530dda8a231e32b24ad0c42"; z_c0="2|1:0|10:1636351988|4:z_c0|92:Mi4xZDhRY0FnQUFBQUFBVUZEbkY1X19FeVlBQUFCZ0FsVk45QTEyWWdESjdzRElsdXlianl6TUtJcEtrVWxpaTl6RUF3|3c00a7a1b959bbcf72388a3bd105548581af65ff8b6f6263c2a47c2701658619"; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1637591904,1637632938,1637648317,1637668159; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1637668159; KLBRSID=b33d76655747159914ef8c32323d16fd|1637668159|1637668153'

        }
        url = 'https://www.zhihu.com/hot'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)  # lhlhlhlhl罗宏亮
        cnt = 1
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ('                                 知乎Top        ') +time.strftime("%%H:%M:%S", time.localtime())+ '\n\n'

        titles = tree.xpath('//*[@id="TopstoryContent"]/div/div/div[1]/section')
        for i in titles:
            title = i.xpath('./div[2]/a/h2/text()')[0]
            url = i.xpath('./div[2]/a/@href')[0]
            # lhlhlhlhl罗宏亮
            # lhlhlhlhl罗宏亮
            str1 = str1 + ("  "+str(cnt) + '.   ' + title) + '\n'
            str1 = str1 + ('            ' + url) + '\n\n'

            cnt = cnt + 1
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_zhihutop():
    try:
        _thread.start_new_thread(zhihutop, ("zhihutop", 0))
    except:
        print("Error: 无法启动线程")

def bilibili(threadName, delay):
    global flag
    flag='bilibili'
    while flag=='bilibili':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
            'cookie': "b_nut=1636280573; _uuid=7335F919-544F-02C8-639F-3BE7E68CDE3072638infoc; buvid3=C5B2E68C-332A-4572-9038-D6F8F8249D59148825infoc; DedeUserID=244138015; DedeUserID__ckMd5=0eb0b23188817111; blackside_state=1; rpdid=|(um|uuY|~lJ0J'uYJYk)|YmR; CURRENT_QUALITY=80; LIVE_BUVID=AUTO6916365473388926; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1636632597,1636683961,1636883884,1636902836; b_ut=2; i-wanna-go-back=-1; video_page_version=v_new_home_16; fingerprint3=3c798f63698baa034ab29ec3677c6ccb; fingerprint=3c400b3850fd22e16978e23932941eb6; fingerprint_s=cd10c11b5b559522fa6e0c1443114654; buvid_fp=C5B2E68C-332A-4572-9038-D6F8F8249D59148825infoc; buvid_fp_plain=C5B2E68C-332A-4572-9038-D6F8F8249D59148825infoc; CURRENT_BLACKGAP=0; SESSDATA=33755d5b%2C1653008926%2Cc679d%2Ab1; bili_jct=7140d11ecad1a999f48293c063d860d4; sid=90sn891v; PVID=4; CURRENT_FNVAL=976; bp_video_offset_244138015=596199425571884900; bp_t_offset_244138015=undefined; innersign=0"
        }

        url = 'https://www.bilibili.com/v/popular/rank/all'
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                     LHL's bilibili Top 100      ") +time.strftime("%H:%M:%S", time.localtime())+ '\n\n'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="app"]/div/div[2]/div[2]/ul/li')
        cnt = 1  # lhlhlhlhl罗宏亮

        for i in card_list:
            try:
                title = i.xpath('./div/div[2]/a/text()')[0]
                bofangliang = i.xpath('./div/div[2]/div/div/span[1]/text()')[0]
                bofangliang = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", bofangliang)
                #
                danmushuliang = i.xpath('./div/div[2]/div/div/span[2]/text()')[0]
                danmushuliang = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", danmushuliang)
                Up = i.xpath('./div/div[2]/div/a/span/text()')[0]
                Up = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", Up)
                #
                url = 'https:' + i.xpath('./div/div[1]/a/@href')[0]
                str1 = str1 + ("  "+str(cnt) + '. ' + title) + '\n'
                str1 = str1 + ('     UP：' + Up) + '\n'
                str1 = str1 + ('     播放量：' + bofangliang) + '\n'
                str1 = str1 + ('     弹幕量：' + danmushuliang) + '\n'

                str1 = str1 + ('     地址：' + url) + '\n\n'

                cnt = cnt + 1
            except:  # lhlhlhlhl罗宏亮
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)



def start_bilibili( ):
    try:
        _thread.start_new_thread(bilibili, ("bilibili", 0))
    except:
        print("Error: 无法启动线程")

def huxiu(threadName, delay):
    global flag
    flag='huxiu'
    while flag=='huxiu':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   LHL's 虎嗅文章      ") +time.strftime("%H:%M:%S", time.localtime())+ "\n\n"
        url = 'https://www.huxiu.com/article/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="top"]/div')
        cnthuxiu = 1
        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                str1 = str1 + "  "+str(cnthuxiu) + ".   " + i.xpath('./div/div/a/div[1]/img/@alt')[0] + '\n'
                str1 = str1 + "       " + 'https://www.huxiu.com' + i.xpath('./div/div/a/@href')[0] + '\n\n'
                cnthuxiu = cnthuxiu + 1

            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)



def start_huxiu( ):
    try:
        _thread.start_new_thread(huxiu, ("huxiu", 0))
    except:
        print("Error: 无法启动线程")

def game_list(threadName, delay):
    global  flag
    flag='game_list'
    while flag=='game_list':
        cnt = 1
        count = 0
        flag = 1
        cnt11 = 1
        t.delete(1.0, 'end')
        str1 = ''
        t.insert("end", "                     LHL' Game List     " +time.strftime("%H:%M:%S", time.localtime())+  '\n\n')

        url_head = 'https://bbs.3dmgame.com/'
        while True:
            url = 'https://bbs.3dmgame.com/forum-game0day-{}.html'.format(cnt)
            source = requests.get(url=url).text
            tree = etree.HTML(source)
            title = tree.xpath("//a[@style='font-weight: bold;color: #EE1B2E;']")

            for i in title:
                title_m = i.xpath('./text()')[0]
                url_m = "        " + url_head + i.xpath('./@href')[0]
                if (title_m[0] == '【') & (ord(title_m[1]) >= 48) & (ord(title_m[1]) <= 57):
                    t.insert("end", "  "+str(cnt11) + ".    " + title_m + '\n')
                    t.insert("end", url_m + '\n\n')
                    cnt11 = cnt11 + 1
                    count = count + 1
                    if count >= int(10):
                        flag = 0
                        break  # lhlhlhlhl罗宏亮
            cnt = cnt + 1
            if flag == 0:
                break
            t.insert(1.0, str1)
    time.sleep(delay_time)


def start_game_list( ):
    try:
        _thread.start_new_thread(game_list, ("game_list", 0))
    except:
        print("Error: 无法启动线程")



def douban_movies(threadName, delay):
    global flag
    flag='douban_movies'
    while flag=='douban_movies':

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        cntdouban = 1
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   LHL's Latest Movie    ") +time.strftime("%H:%M:%S", time.localtime())+ "\n\n"
        url = 'https://movie.douban.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        title_list = tree.xpath('//*[@id="screening"]/div[2]/ul/li')
        for i in title_list:
            try:
                title = i.xpath("./@data-title")[0]
                pingfen = i.xpath('./ul/li[3]/span[2]//text()')[0]  # lhlhlhlhl罗宏亮
                place = i.xpath("./@data-region")[0]
                shichang = i.xpath("./@data-duration")[0]
                director = i.xpath("./@data-director")[0]
                actors = i.xpath("./@data-actors")[0]
                url = i.xpath('./ul/li[2]/a/@href')[0]
                t.insert("end", "  "+str(cntdouban) + ". " + title + '\n')
                t.insert("end", '    评分:' + pingfen + '\n')
                t.insert("end", '    导演:' + director + '\n')
                t.insert("end", '    主演:' + actors + '\n')
                t.insert("end", '    国家地区:' + place + '\n')
                t.insert("end", '    时长:' + shichang + '\n')  # lhlhlhlhl罗宏亮
                t.insert("end", '    地址:' + url + '\n' + '\n')
                cntdouban = cntdouban + 1
            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_douban_movies( ):
    try:
        _thread.start_new_thread(douban_movies, ("douban_movies", 0))
    except:
        print("Error: 无法启动线程")


def steamcracked(threadName, delay):
    global flag
    flag = 'steamcracked'
    while flag == 'steamcracked':


        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        t.delete(1.0, 'end')
        str1 = ''
        str1 = str1 + ("                   SteamCracked       ") +time.strftime("%H:%M:%S", time.localtime())+ '\n\n'
        url = 'https://steamcrackedgames.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div')
        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                title = i.xpath('./div/div/a/text()')[0]
                url_tail = i.xpath('./div/div/div/small/span[1]/text()')[0]
                t.insert("end","  "+ str(cnt) + '. ' + title + "\n")
                t.insert("end", '     状态:   ' + url_tail + "\n" + "\n")

                cnt = cnt + 1
            except:
                continue
        t.insert(1.0, str1)
        time.sleep(delay_time)

def start_steamcracked( ):
    try:
        _thread.start_new_thread(steamcracked, ("steamcracked", 0))
    except:
        print("Error: 无法启动线程")

def skidrowcodex(threadName, delay):
    global flag
    flag = 'skidrowcodex'
    while flag == 'skidrowcodex':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
        }
        t.delete(1.0, 'end')

        t.insert("end", "                   Skidrowcodex      " +time.strftime("%H:%M:%S", time.localtime())+'\n\n')
        url = 'https://www.skidrowcodex.net/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="main_wrapper"]/div[6]/div/div[1]/div')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            try:
                title = i.xpath('./div[1]/div[2]/h2/a/text()')[0]
                url_tail = i.xpath('./div[1]/div[2]/h2/a/@href')[0]
                t.insert("end", "  "+str(cnt) + '. ' + title + '\n')
                t.insert("end", '     地址: ' + url_tail + '\n' + '\n')

                cnt = cnt + 1

            except:
                continue

        time.sleep(delay_time)


def start_skidrowcodex():
    try:
        _thread.start_new_thread(skidrowcodex, ("skidrowcodex", 0))
    except:
        print("Error: 无法启动线程")


def pdoro(threadName, delay):
    global flag
    flag = 'pdoro'
    while flag == 'pdoro':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookie': 'bbs_sid=31e211fd2aa2aef7; UM_distinctid=17d18bf7845241-0a04ae99cfc603-561a1053-384000-17d18bf7846e0; bbs_lastday=1638285770; bbs_lastonlineupdate=1638357242; timeoffset=%2B08; CNZZDATA1260924983=591798974-1636794189-%7C1638349746; __tins__17773989=%7B%22sid%22%3A%201638357241795%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201638359041795%7D; __51cke__=; __51laig__=1'
        }
        t.delete(1.0, 'end')
        t.insert("end", "                   pdoro      " +time.strftime("%H:%M:%S", time.localtime())+ "\n" + "\n")
        url = 'http://www.pdoro.com/'
        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="post-item-pobu"]/div[2]/ul/li')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./div/div[2]/h2/a/text()')[0]
            urll = i.xpath('./div/div[2]/h2/a/@href')[0]

            t.insert("end", "  "+str(cnt) + ". " + title + "\n")
            t.insert("end", "     " + urll + "\n" + "\n")
            cnt = cnt + 1
            continue
        time.sleep(delay_time)

def start_pdoro( ):
    try:
        _thread.start_new_thread(pdoro, ("pdoro", 0))
    except:
        print("Error: 无法启动线程")

def pianku(threadName, delay):
    global flag
    flag = 'pianku'
    while flag == 'pianku':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        }
        url = 'https://www.pianku.li/'
        lists = requests.get(url=url, headers=headers).text
        tree = etree.HTML(lists)
        t.delete(1.0, 'end')
        t.insert("end", "                 pianku     " +time.strftime("%H:%M:%S", time.localtime())+ '\n')
        t.insert("end", "电影：" + '\n')
        cnt = 1
        dianying = tree.xpath('/html/body/main/div[2]/ul/li')
        for i in dianying:
            title = i.xpath('./div[2]/h3/a/text()')[0]
            pingfen = i.xpath('./div[2]/h3/span/text()')[0]
            xiangxi = i.xpath('./div[2]/div/text()')[0]
            url_tail = 'https://www.pianku.li' + i.xpath('./div[1]/a/@href')[0]
            t.insert("end", '    ' + str(cnt) + '.' + title + '\n')
            t.insert("end", '         ' + pingfen + '分' + '\n')
            t.insert("end", '          ' + xiangxi + '\n')
            t.insert("end", '            ' + url_tail + '\n' + '\n')

            cnt = cnt + 1
        t.insert("end", '剧集:' + '\n')
        cnt = 1
        juji = tree.xpath('/html/body/main/div[3]/ul/li')
        for i in juji:
            title = i.xpath('./div[2]/h3/a/text()')[0]
            pingfen = i.xpath('./div[2]/h3/span/text()')[0]
            xiangxi = i.xpath('./div[2]/div/text()')[0]
            url_tail = 'https://www.pianku.li' + i.xpath('./div[1]/a/@href')[0]
            t.insert("end", '    ' + str(cnt) + '.' + title + '\n')
            t.insert("end", '         ' + pingfen + '分' + '\n')
            t.insert("end", '          ' + xiangxi + '\n')
            t.insert("end", '            ' + url_tail + '\n' + '\n')

            cnt = cnt + 1
        t.insert("end", '动漫:' + '\n')
        cnt = 1
        dongman = tree.xpath('/html/body/main/div[4]/ul/li')
        for i in dongman:
            title = i.xpath('./div[2]/h3/a/text()')[0]
            pingfen = i.xpath('./div[2]/h3/span/text()')[0]
            xiangxi = i.xpath('./div[2]/div/text()')[0]
            url_tail = 'https://www.pianku.li' + i.xpath('./div[1]/a/@href')[0]
            t.insert("end", '    ' + str(cnt) + '.' + title + '\n')
            t.insert("end", '         ' + pingfen + '分' + '\n')
            t.insert("end", '          ' + xiangxi + '\n')
            t.insert("end", '            ' + url_tail + '\n' + '\n')

            cnt = cnt + 1
        time.sleep(delay_time)


def start_pianku( ):
    try:
        _thread.start_new_thread(pianku, ("pianku", 0))
    except:
        print("Error: 无法启动线程")

def Pirate_Bay(threadName, delay):
    global flag
    flag = 'Pirate_Bay'
    while flag == 'Pirate_Bay':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'cookie': 'gaDts48g=q8h5pp9t; gaDts48g=q8h5pp9t; use_alt_cdn=1; aby=2; skt=qrpze70pbv; skt=qrpze70pbv; tcc'
        }
        print("                   bt")
        url = 'https://tpb.party/top/200'
        source = requests.get(url=url, headers=headers).text

        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@class="detName"]')
        t.delete(1.0, 'end')
        t.insert('end', "                        Pirate Bay      " +time.strftime("%H:%M:%S", time.localtime())+ '\n' + '\n')
        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./a/text()')[0]
            urll = i.xpath('./a/@href')[0]

            t.insert('end', "  "+str(cnt) + ". " + title + '\n')
            t.insert('end', "       " + urll + '\n' + '\n')
            cnt = cnt + 1

            continue
        time.sleep(delay_time)
def start_Pirate_Bay( ):
    try:
        _thread.start_new_thread(Pirate_Bay, ("Pirate_Bay", 0))
    except:
        print("Error: 无法启动线程")

def RARGB(threadName, delay):
    global flag
    flag = 'RARGB'
    while flag == 'RARGB':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'cookie': 'gaDts48g=q8h5pp9t; gaDts48g=q8h5pp9t; use_alt_cdn=1; aby=2; skt=autywde7kx; skt=autywde7kx; sk=09ajfqwdc8; expla=1; tcc'


        }
        t.delete(1.0, 'end')
        t.insert('end', "                  RARGB         " +time.strftime("%H:%M:%S", time.localtime())+ '\n' + '\n')
        url = 'https://rarbgprx.org/top100.php?category[]=14&category[]=15&category[]=16&category[]=17&category[]=21&category[]=22&category[]=42&category[]=44&category[]=45&category[]=46&category[]=47&category[]=48'
        source = requests.get(url=url, headers=headers).text

        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@class="lista2"]')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./td[2]/a[1]/text()')[0]
            size = i.xpath('./td[4]/text()')[0]
            urll = i.xpath('./td[2]/a[2]/@href')[0]
            score = i.xpath('./td[2]/span/text()')[0]
            t.insert('end',"  "+ str(cnt) + ". " + title + '\n')
            if (len(score.split('IMDB: ')) > 1):
                t.insert('end', "      " + score.split('IMDB: ')[1][0:3] + "分" + '\n')
            t.insert('end', "       " + size + '\n')
            t.insert('end', "         " + "https://rarbgprx.org" + urll + '\n' + '\n')
            cnt = cnt + 1

            continue
        time.sleep(delay_time)


def start_RARGB( ):
    try:
        _thread.start_new_thread(RARGB, ("RARGB", 0))
    except:
        print("Error: 无法启动线程")


def hd_ai(threadName, delay):
    global flag
    flag = 'hd_ai'
    while flag == 'hd_ai':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'cookie': 'c_secure_uid=4938; c_secure_pass=7cacb523faeba010505abe93d675adde; c_secure_ssl=nope; c_secure_tracker_ssl=nope; c_secure_login=nope; PHPSESSID=964ja96rnvaeg4pkmcpp38vfg1'}
        t.delete(1.0, 'end')
        t.insert('end', "                   hd_ai     " +time.strftime("%H:%M:%S", time.localtime())+'\n' + '\n')
        url = 'https://www.hd.ai/Torrents.tableList'
        source = requests.get(url=url, headers=headers).json()
        card_list = source['data']['items']

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i['small_descr']
            url = i['details']
            if (title == ''):
                continue
            t.insert('end',"  "+ str(cnt) + ".  " + title + '\n')
            t.insert('end', "       " + "https://www.hd.ai" + url + '\n' + '\n')
            cnt = cnt + 1
        time.sleep(delay_time)
def start_hd_ai( ):
    try:
        _thread.start_new_thread(hd_ai, ("hd_ai", 0))
    except:
        print("Error: 无法启动线程")
def youtube():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
        'cookie': 'VISITOR_INFO1_LIVE=A3bSAIfUGDs; LOGIN_INFO=AFmmF2swRQIhAMySgN7wyUcmshqsJciBm75tV8-sreSVlgGclpobfuSKAiBaRBm-Lt6jB11mYzmCqH6MZqvU91xf5vimrOdqpYHqwg:QUQ3MjNmd0tYM2Y3aXFJcXY1dU9pN2hxaWV6NEtvbWpnWEVFa1pROW90THZjMlFLVUxtclRsdUVZak5jUHFod3l0dXd1Z0s2OWJ3Z1RqN25tcERxdjJLbV9wb2RmOUwzZUx1ZG5GSFFJUzVNWXZnMmpLOVRxbjV2clFOWnkzYTlrODJ4RnM0a3FodUU2VG4wZkVBeHU5LTg4SmE4d1I1UGxn; SID=Dghp0vBsy91HgkL6qoFj1j06olowRQaMs4olF7e6MKAs65UVCgMhY1Dw8ldK_YcwS66KYQ.; __Secure-1PSID=Dghp0vBsy91HgkL6qoFj1j06olowRQaMs4olF7e6MKAs65UVdxho_TAKkUaKC-qoGBYp0A.; __Secure-3PSID=Dghp0vBsy91HgkL6qoFj1j06olowRQaMs4olF7e6MKAs65UVXP6uhw1vSSau8ZR4jLZOcA.; HSID=A3Al_FPXLpbFQjoHt; SSID=ASCJ0cz7_MIFZld58; APISID=xlsWGWXCqsZsbDTE/A0sIYHSSNWjTSmvYr; SAPISID=3EupqtVNYod0L-aA/AyUBuaRH-XVS0Ylcv; __Secure-1PAPISID=3EupqtVNYod0L-aA/AyUBuaRH-XVS0Ylcv; __Secure-3PAPISID=3EupqtVNYod0L-aA/AyUBuaRH-XVS0Ylcv; _ga=GA1.2.1268668925.1636788103; _gcl_au=1.1.629964360.1637035019; PREF=f4=4000000&tz=Asia.Shanghai&f6=40000000&f5=30000&volume=100&library_tab_browse_id=FEmusic_liked_playlists; YSC=ks3CXdBqz_A; SIDCC=AJi4QfFCmgttS3x9wwry_HrVa09RIWtzF_zB9e_pcHdJ0XaynUl286un1JCmSD8P9niJ8hF3ynM; __Secure-3PSIDCC=AJi4QfE2mzmbe0dX90RCtTWR0cqUNIZUzjumEi0TnETLalo1QROO6yRrFx5ZxpJq_a_Ul34mCw'
    }

    url = 'https://www.youtube.com/feed/trending'
    t.delete(1.0, 'end')
    t.insert('end', "                     Youtube流行" + '\n' + '\n')
    source = requests.get(url=url, headers=headers).text
    tree = etree.HTML(source)
    # pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)

    youtube_json = re.compile('responseContext".*?"serviceTrackingParams(.*?)function serverContract()', re.S)
    json_get = (str)(re.findall(youtube_json, source)[0])

    # youtube_title1 = re.compile('"title".*?"text":"(.*?)".*?"accessibility"',re.S)
    # youtube_title = re.compile(',"accessibility":.*?"accessibilityData":.*?"label":"(.*?) 来自(.*?) (.*?)天前 (.*?) (.*?)".*?转到频道', re.S)
    youtube_title = re.compile(
        ',"title":{"runs":.{"text":"(.*?)"}.,.*?publishedTimeText":{"simpleText":"(.*?)"},.*?accessibilityData":{"label":"(.*?)"}},.*?viewCountText":{"simpleText":"(.*?)"},"navigationEndpoint.*?webCommandMetadata.*?url":"(.*?)".*?ownerText.*?text":"(.*?)","navigationEndpoint.*?操作菜单',
        re.S)
    cnt = 1
    names = re.findall(youtube_title, json_get)
    for i in names:
        title = i[0]
        Later_time = i[1]
        time_long = i[2]
        Watch_num = i[3]
        url = 'https://www.youtube.com' + i[4]
        youtuber = i[5]

        t.insert('end',"  "+ str(cnt) + ". " + title + '\n')
        t.insert('end', "       Youtuber： " + youtuber + '\n')
        t.insert('end', "       发布时间:   " + Later_time + '\n')
        t.insert('end', "       时长:      " + time_long + '\n')
        t.insert('end', "       观看数量:   " + Watch_num + '\n')
        t.insert('end', "       地址:      " + url + '\n' + '\n')

        cnt = cnt + 1


def BT_HOME(threadName, delay):
    global flag
    flag = 'BT_HOME'
    while flag == 'BT_HOME':

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
            'Cookie': 'SINAGLOBAL=6741639331961.842.1636351443105; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5merwV-edKPy4zi1nWB2WF; UOR=,,tophub.today; SUB=_2AkMWxpZdf8NxqwJRmfsUyWzjb49-wgHEieKgmmeGJRMxHRl-yT8XqmAktRB6PUa4sKj9bCE81uS9DWuk-pvHv3CkQsSr; _s_tentry=tophub.today; Apache=9191740774784.104.1637667572390; ULV=1637667572470:9:9:2:9191740774784.104.1637667572390:1637636253119'
        }
        # lhlhlhlhl罗宏亮
        url = 'https://btbtt20.com/'
        t.delete(1.0, 'end')
        t.insert('end', "                     BT_HOME       " +time.strftime("%H:%M:%S", time.localtime())+ '\n' + '\n')
        lists = requests.get(url=url, headers=headers).text
        lists_json = re.compile(
            '</a>\t.*?\n.*?<a href="(.*?)" class="subject_link thread-new"  target="_blank" title="(.*?)" >.*?<span class',
            re.S)
        json_get = re.findall(lists_json, lists)
        cnt = 1
        for i in range(1, len(json_get)):
            title = json_get[i][1]
            url = "https://btbtt20.com/" + json_get[i][0]
            t.insert('end',"  "+ str(cnt) + ".  " + title + '\n')
            t.insert('end', "       " + url + '\n' + '\n')
            cnt = cnt + 1
        time.sleep(delay_time)

def start_BT_HOME ( ):
    try:
        _thread.start_new_thread(BT_HOME, ("BT_HOME", 0))
    except:
        print("Error: 无法启动线程")


def Epic_freeGames(threadName, delay):
    global flag
    flag = 'Epic_freeGames'
    while flag == 'Epic_freeGames':

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        }

        url = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=US&allowCountries=US'


        t.delete(1.0, 'end')
        t.insert('end', "                     Epic_freeGames    " +time.strftime("%H:%M:%S", time.localtime())+ '\n\n')
        source = requests.get(url=url, headers=headers).json()

        # titles = tree.xpath('https://www.epicgames.com/store/zh-CN/free-games')
        cnt = 1
        list=source['data']['Catalog']['searchStore']['elements']
        shuzhu_Epic=[]
        Epic_lenn=len(list)-1
        for i in list:
            shuzhu_Epic.append(i['title'])
        while(Epic_lenn>=0):
            t.insert('end', str(Epic_lenn+1)+".  "+shuzhu_Epic[Epic_lenn]+'\n'+'\n')
            Epic_lenn=Epic_lenn-1
        time.sleep(delay_time)

def start_Epic_freeGames ( ):
    try:
        _thread.start_new_thread(Epic_freeGames, ("Epic_freeGames", 0))
    except:
        print("Error: 无法启动线程")

def steam_HOT(threadName, delay):
    global flag
    flag = 'douban_movies'
    while flag == 'douban_movies':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }


        url = 'https://store.steampowered.com/search/?filter=topsellers'
        source = requests.get(url=url, headers=headers).text
        t.delete(1.0, 'end')
        t.insert('end', "                    Steam Hot    " +time.strftime("%H:%M:%S", time.localtime())+ '\n\n')
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="search_resultsRows"]/a')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./div[2]/div[1]/span/text()')[0]
            hao_pings=i.xpath('./div[2]/div[3]/span/@data-tooltip-html')
            if (len(hao_pings) > 0):
                hao_ping = str(hao_pings[0])
                hao_ping = hao_ping.split('<br>')[1]

                hao_ping_num_peo = hao_ping.split('用户的游戏评测中有')
                if (len(hao_ping_num_peo) >= 2):
                    hao_ping_people = hao_ping_num_peo[0]
                    hao_ping_num = hao_ping_num_peo[1].replace("。", '')
                else:
                    hao_ping_people = ''
                    hao_ping_num = 0
            else:
                hao_ping_people = ''
                hao_ping_num = 0
            zhekoou=i.xpath('./div[2]/div[4]/div[1]/span/text()')

            release_time=i.xpath('./div[2]/div[2]/text()')


            url_game=i.xpath('./@href')[0]
            values_game_origion = i.xpath('./div[2]/div[4]/div[2]/text()')
            values_game_origion_origion=i.xpath('./div[2]/div[4]/div[2]/span/strike/text()')

            if(len(values_game_origion)>=2):
                values_game_zhe=i.xpath('./div[2]/div[4]/div[2]/text()')[1]
            else:
                values_game_zhe = str(i.xpath('./div[2]/div[4]/div[2]/text()')[0])
                values_game_zhe=values_game_zhe.replace("\r\n                        ",'')
            t.insert('end',"  "+ str(cnt)+".    "+  title+'\n')
            if len(hao_ping_people) > 0:
                t.insert('end', "            评价: "+ hao_ping_num+"    "+hao_ping_people+'\n')
            if(len(zhekoou)>0):
                t.insert('end', "            折扣:  "+zhekoou[0]+'\n')
                t.insert('end', "            原价:  "+values_game_origion_origion[0]+'\n')
            else:
                t.insert('end', "            折扣:  无"  +'\n')
            t.insert('end', "            价格:  "+values_game_zhe+'\n')
            if (len(release_time) >= 1):
                t.insert('end', "            时间:  " + release_time[0]+'\n')
            else:
                t.insert('end', "            时间:  无信息"  +'\n')
            t.insert('end', "            地址:  "+str(url_game).split('/?')[0]+'\n'+'\n')

            cnt = cnt + 1
        time.sleep(delay_time)

def start_steam_HOT ( ):
    try:
        _thread.start_new_thread(steam_HOT, ("steam_HOT", 0))
    except:
        print("Error: 无法启动线程")

def steam_new(threadName, delay):
    global flag
    flag = 'steam_new'
    while flag == 'steam_new':
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }


        url = 'https://store.steampowered.com/search/?filter=popularnew&sort_by=Released_DESC'
        source = requests.get(url=url, headers=headers).text
        t.delete(1.0, 'end')
        t.insert('end', "                    Steam Hot    " +time.strftime("%H:%M:%S", time.localtime())+ '\n\n')
        tree = etree.HTML(source)
        card_list = tree.xpath('//*[@id="search_resultsRows"]/a')

        cnt = 1

        for i in card_list:  # lhlhlhlhl罗宏亮
            title = i.xpath('./div[2]/div[1]/span/text()')[0]
            hao_pings=i.xpath('./div[2]/div[3]/span/@data-tooltip-html')
            if(len(hao_pings)>0):
                hao_ping=str(hao_pings[0])
                hao_ping=hao_ping.split('<br>')[1]

                hao_ping_num_peo=hao_ping.split('用户的游戏评测中有')
                if(len(hao_ping_num_peo)>=2):
                    hao_ping_people = hao_ping_num_peo[0]
                    hao_ping_num= hao_ping_num_peo[1].replace("。",'')
            zhekoou=i.xpath('./div[2]/div[4]/div[1]/span/text()')

            release_time=i.xpath('./div[2]/div[2]/text()')


            url_game=i.xpath('./@href')[0]
            values_game_origion = i.xpath('./div[2]/div[4]/div[2]/text()')
            values_game_origion_origion=i.xpath('./div[2]/div[4]/div[2]/span/strike/text()')

            if(len(values_game_origion)>=2):
                values_game_zhe=i.xpath('./div[2]/div[4]/div[2]/text()')[1]
            else:
                values_game_zhe = str(i.xpath('./div[2]/div[4]/div[2]/text()')[0])
                values_game_zhe=values_game_zhe.replace("\r\n                        ",'')
            t.insert('end',"  "+ str(cnt)+".    "+  title+'\n')
            t.insert('end', "            评价: "+ hao_ping_num+"    "+hao_ping_people+'\n')
            if(len(zhekoou)>0):
                t.insert('end', "            折扣:  "+zhekoou[0]+'\n')
                t.insert('end', "            原价:  "+values_game_origion_origion[0]+'\n')
            else:
                t.insert('end', "            折扣:  无"  +'\n')
            t.insert('end', "            价格:  "+values_game_zhe+'\n')
            if (len(release_time) >= 1):
                t.insert('end', "            时间:  " + release_time[0]+'\n')
            else:
                t.insert('end', "            时间:  无信息"  +'\n')
            t.insert('end', "            地址:  "+str(url_game).split('/?')[0]+'\n'+'\n')

            cnt = cnt + 1
        time.sleep(delay_time)

def start_steam_new ( ):
    try:
        _thread.start_new_thread(steam_new, ("steam_new", 0))
    except:
        print("Error: 无法启动线程")


def PT_Time(threadName, delay):
    global flag
    flag = 'PT_Time'
    while flag == 'PT_Time':

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
            'cookie': 'c_secure_uid=MzIwNDY%3D; c_secure_pass=ad5dc1d4c2b7ff2c09e9b3097f6a4ab8; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
        t.delete(1.0, 'end')
        t.insert('end', "                    PT_Time    " + time.strftime("%H:%M:%S", time.localtime()) + '\n\n')
        url = 'https://www.pttime.org/torrents.php'

        source = requests.get(url=url, headers=headers).text
        tree = etree.HTML(source)

        cnt=1
        youtube_json = re.compile('<tr>.*?<td class="rowfollow nowrap" valign="middle">.*?<b class="title">(.*?)<.*?</span></td><td class="rowfollow">(.*?)<br />(.*?)</td>.*?</tr>', re.S)
        json_get = (re.findall(youtube_json, source))
        print(json_get)
        # youtube_title1 = re.compile('"title".*?"text":"(.*?)".*?"accessibility"',re.S)
        # youtube_title = re.compile(',"accessibility":.*?"accessibilityData":.*?"label":"(.*?) 来自(.*?) (.*?)天前 (.*?) (.*?)".*?转到频道', re.S)
        # youtube_title = re.compile(
        #     ',"title":{"runs":.{"text":"(.*?)"}.,.*?publishedTimeText":{"simpleText":"(.*?)"},.*?accessibilityData":{"label":"(.*?)"}},.*?viewCountText":{"simpleText":"(.*?)"},"navigationEndpoint.*?webCommandMetadata.*?url":"(.*?)".*?ownerText.*?text":"(.*?)","navigationEndpoint.*?操作菜单',
        #     re.S)
        # cnt = 1
        # names = re.findall(youtube_title, json_get)
        for i in json_get:
            title = i[0]
            size=i[1]+i[2]
            t.insert('end', "  "+str(cnt)+".     "+title+'\n')
            t.insert('end', "              "+size+'\n'+'\n')


            cnt = cnt + 1
        time.sleep(delay_time)
def start_PT_Time ( ):
    try:
        _thread.start_new_thread(PT_Time, ("PT_Time", 0))
    except:
        print("Error: 无法启动线程")







scroll = tk.Scrollbar(width=20)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label="Information", menu=filemenu)
filemenu.add_command(label="Weibo", command=start_weibo)
filemenu.add_command(label="Baidu", command=start_baidu_time)
filemenu.add_command(label="Zhihu", command=start_zhihutop)
filemenu.add_command(label="Youtube", command=youtube)
filemenu.add_command(label="Bilibili", command=start_bilibili)
filemenu.add_command(label="huxiu", command=start_huxiu)
filemenu.add_command(label="GameList", command=start_game_list)
filemenu.add_command(label="Douban", command=start_douban_movies)
filemenu.add_command(label="Steamcracked", command=start_steamcracked)
filemenu.add_command(label="Skidrowcodex", command=start_skidrowcodex)
filemenu.add_command(label="pdoro", command=start_pdoro)
filemenu.add_command(label="Pianku", command=start_pianku)
filemenu.add_command(label="Pirate Bay", command=start_Pirate_Bay)
filemenu.add_command(label="RARGB", command=start_RARGB)
filemenu.add_command(label="HD_ai", command=start_hd_ai)
filemenu.add_command(label="BT_HOME", command=start_BT_HOME)
filemenu.add_command(label="Epic_freeGames", command=start_Epic_freeGames)
filemenu.add_command(label="Steam_HOT", command=start_steam_HOT)
filemenu.add_command(label="Steam_NEW", command=start_steam_new)
filemenu.add_command(label="PT_Time", command=start_PT_Time)
filemenu.add_command(label="Delete", command=delete_text)

# pyinstaller --onefile --icon=favicon.ico  test.py -w
# b1=tk.Button(window,text="Baidu",command=baidu_time)
# b2=tk.Button(window,text="Weibo",command=weibo)
# b3=tk.Button(window,text="Zhihu",command=zhihutop)
# b4=tk.Button(window,text="Bilibili",command=bilibili)
# b5=tk.Button(window,text="huxiu",command=huxiu)
# b6=tk.Button(window,text="GameList",command=game_list)
# b7=tk.Button(window,text="Douban",command=douban_movies)
# b8=tk.Button(window,text="Steamcracked",command=steamcracked)
# b9=tk.Button(window,text="Skidrowcodex",command=skidrowcodex)
# b10=tk.Button(window,text="pdoro",command=pdoro)
# b11=tk.Button(window,text="Pianku",command=pianku)
# b3=tk.Button(window,text="Delete",command=delete_text)


t = tk.Text(window, width=3840, height=2160, font=('Consolas', 15))

scroll.pack(side=tk.RIGHT, fill=tk.Y)
scroll.config(command=t.yview)

t.pack(side='top', fill="both")

window.config(menu=menubar)
window.mainloop()
