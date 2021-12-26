实时主流信息设计

 



为解决实时主流信息获取的需求，采用python技术，设计了实时主流信息程序，获得了满意的结果，程序经测试，符合预期需求，为构建一种可以灵活扩展的应用程序提供解决思路或借鉴。

## 

l Python：

Python的设计哲学强调代码的[可读性](https://zh.wikipedia.org/wiki/程式可讀性)和简洁的语法，尤其是使用[空格缩进](https://zh.wikipedia.org/wiki/越位规则)划分代码块。相比

于[C](https://zh.wikipedia.org/wiki/C语言)或[Java](https://zh.wikipedia.org/wiki/Java)，Python让开发者能够用更少的代码表达想法。

Python[解释器](https://zh.wikipedia.org/wiki/解释器)本身几乎可以在所有的[操作系统](https://zh.wikipedia.org/wiki/操作系统)中运行。Python的官方[解释器](https://zh.wikipedia.org/wiki/直譯器)[CPython](https://zh.wikipedia.org/wiki/CPython)是用[C](https://zh.wikipedia.org/wiki/C语言)

语言编写的，它是一个由社群驱动的自由[软件](https://zh.wikipedia.org/wiki/軟體)，目前由[Python软件基金会](https://zh.wikipedia.org/wiki/Python軟體基金會)管理。

Python一直是最受欢迎的编程语言之一

l Tkinter：

 Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和 Tkinter 可以在大多

数的 Unix 平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本

可以实现本地窗口风格,并良好地运行在绝大多数平台中。

l wxPython：

wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序

员很方便的创建完整的、功能健全的 GUI 用户界面。

l Jython：

Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。Jython 可以被动态或静态地编译成 Java 字节码。

l Requests：

Python 的标准库 urllib 提供了大部分 HTTP 功能，但使用起来较繁琐。通常，我们会使用

另外一个优秀的第三方库：[Requests](https://github.com/kennethreitz/requests)，它的标语是：Requests: HTTP for Humans。

 

l [subprocess](#module-subprocess) ：

模块允许你生成新的进程，连接它们的输入、输出、错误管道，并且获取它们的返回码。此模块打算代替

一些老旧的模块与功能 





## **3.** ![img](https://s2.loli.net/2021/12/26/flb2esCThKtMj8G.jpg)

#### ***\*程序设计：\****

![img](https://s2.loli.net/2021/12/26/vIq2xfnGcNtyEYR.jpg) 

cmd = 'your command'

res = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

用于隐藏cmd命令窗口

打包时需要pyinstaller --onefile --icon=favicon.ico  test.py -w

普通的pyinstaller -F -i favicon.ico test.py

无法隐藏cmd命令窗口

window = tk.Tk()

创建gui

window.title("LHL's Information")

window.iconbitmap('favicon.ico')

window.geometry("1500x1000")

设置窗口名称，图标，大小

 

![img](https://s2.loli.net/2021/12/26/d28CrxKX43R1DEW.jpg) 

这两个为全局变量

Flag表示现在的线程 

![img](https://s2.loli.net/2021/12/26/MpekcuO7tji4xIb.jpg) 

用于控制临界资源，不抢占text输出窗口

delay_time

为time.sleep的时间，单位秒

定义定义线程刷新时间间隔

####  

#### ![img](https://s2.loli.net/2021/12/26/vSJjqUXeaAY2pzt.jpg) 

####  

#### ***\*Flag一定要用全局，不然无法起到控制临界资源的作用\****

 

HTTP是“Hypertext Transfer Protocol”的所写，整个万维网都在使用这种协议，几乎你在浏览器里看到的大部分内容都是通过

http协议来传输的.

HTTP Headers是HTTP请求和相应的核心，它承载了关于客户端浏览器，请求页面，服务器等相关的信息。

'user-agent':

User-Agent会告诉网站服务器，访问者是通过什么工具来请求的，如果是爬虫请求，一般会拒绝，如果是用户浏览器，就会应答。

'cookie'：

Cookie是保存在客户端的纯文本文件。比如txt文件。所谓的客户端就是我们自己的本地电脑。当我们使用自己的电脑通

过浏览器进行访问网页的时候，服务器就会生成一个证书并返回给我的浏览器并写入我们的本地电脑。

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

t = tk.Text(window, width=3840, height=2160, font=('Consolas', 15))   

创建一个文本框输出输出

####  

![img](https://s2.loli.net/2021/12/26/IzWasAShwO8tPre.jpg) 

t.delete(1.0, 'end') 为删除之前显示的内容

t.insert('end', "          hd_ai" + '\n' + '\n')

插入标题

JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式

url = 'https://www.hd.ai/Torrents.tableList'
	source = requests.get(url=url, headers=headers).json()

请求json数据

![img](https://s2.loli.net/2021/12/26/XTWMaRl67eJ4SsG.jpg) 

#### card_list = source['data']['items']

#### 定位到每个词条

Card_list中包含所有的词条，是一个集合

![img](https://s2.loli.net/2021/12/26/TarJ6FHfEBqwZjD.jpg) 

之后遍历card_list下的'small_descr'和'details' 得到标题和网址

之后通过t.insert 输出到tk.Text

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

除了上面json按层级展开，还有xpath寻找和正则表达式寻找

![img](https://s2.loli.net/2021/12/26/9ESouQeUnOqWLRC.jpg) 

 

 

titles = tree.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div')

为匹配到所用的div词条

![img](https://s2.loli.net/2021/12/26/u1KkLq2TIj5aOMy.jpg) 

 

for i in titles:

再进行逐个遍历输出词条

 

![img](https://s2.loli.net/2021/12/26/xYgz4Q16ltN53Lo.jpg) 

再输出想要的数据到tk.text后

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

操作菜单',    ![img](https://s2.loli.net/2021/12/26/mgrzIyEeOPUaWpX.jpg)

 

 

 

 

Youtube 的结构比较复杂，需要用到正则匹配

 

 

![img](https://s2.loli.net/2021/12/26/pKbM5rZ1O46Gvts.jpg) 

 

youtube_json = re.compile('responseContext".*?"serviceTrackingParams(.*?)function serverContract()', re.S)

(.*?)为需要的内容  .*?为可以变动的内容  其他为固定内容

 

 

因为内容太多，匹配需要很长时间，先进行一次筛选，只留下包含信息的内容

再进行第二次筛选

 

youtube_title= = re.compile(',"title":{"runs":.{"text":"(.*?)"}.,.*?publishedTimeText":{"simpleText":"(.*?)"},.*?accessibilityData":{"label":"(.*?)"}},.*?viewCountText":{"simpleText":"(.*?)"},"navigationEndpoint.*?webCommandMetadata.*?url":"(.*?)".*?ownerText.*?text":"(.*?)","navigationEndpoint.*?操作菜单',re.S)     

 

names = re.findall(youtube_title, json_get)

用youtube_title规则对 json_get 进行筛选

得到 6 条有用信息

![img](https://s2.loli.net/2021/12/26/LqocGaB8IRAkVyh.jpg) 

 

 

再进行输出，得到结果

 

 

![img](https://s2.loli.net/2021/12/26/1pyz49k7CPFdXfb.jpg) 

 

 

 

 

 

 

 

 

 

 

 

 

threadName, delay 是用于多线程的名字和延迟，但我的延迟不由此决定，而是由time.sleep(delay_time)决定

Delay_time是一个全局变量，方便全局控制，无需逐个调试

 

![img](https://s2.loli.net/2021/12/26/lKAIPFv8fgNEYrC.jpg) 

 

 

每个功能都用一个线程调用

 

flag = 'hd_ai'

  while flag == 'hd_ai':

上面的flag用于控制临界资源，就是Tk.text

如果多个线程调用text，则他们抢占text，无法看清内容

如果不用多线程的话，就会出现

如果网页请求超时或无法请求或网页格式改变，程序就会卡死，无响应

####  

#### ***\*程序\*******\*运行界面\****

 

 

 

 



|      |                                                            |
| ---- | ---------------------------------------------------------- |
|      | ![img](https://s2.loli.net/2021/12/26/B34uYHaU7ObvjD5.jpg) |

 



 



|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      | ![img](C:/Users/LHL/AppData/Local/Temp/ksohtml20140/wps39.jpg) |

 



![img](https://s2.loli.net/2021/12/26/3umfX68ZzsQHt2I.jpg) 

 

 

![img](https://s2.loli.net/2021/12/26/xfXEaKrjN93Fp4w.jpg) 

 

 

 

 

 

![img](https://s2.loli.net/2021/12/26/KFq2bC6ojZJgWcl.jpg) 

 

 

##  

## 	结论与感想

 

大数据技术用了多年时间进行演化，才从一种看起来很炫酷的新技术变成了企业在生产经营中实际部署的服务。其中，数据采集产品迎来了广阔的市场前景，无论国内外，市面上都出现了许多技术不一、良莠不齐的采集软件。一款简单易用的网页信息抓取软件,能够抓取网页文字、图表、超链接等多种网页元素。同样可通过简单可视化流程进行采集，服务于任何对数据有采集需求的人群。

一个简单，简洁的信息搜集软件对我生活的改变是巨大的，不用花大量的时间在互联网上寻找新闻与信息，只需要简单的浏览，便可以知道绝大多数想了解的信息，从而提高效率，获得更多的信息。

软件往往无需过度的修饰，斯是陋室，惟实用，为先，简单往往意味着高效。过度的修饰往往破坏获取信息的效率。互联网的信息过于繁杂，往往只需要获取头部的信息，和一些深度分析文章即可。

要主动打破信息茧房，不要让算法左右了我们的人生。
