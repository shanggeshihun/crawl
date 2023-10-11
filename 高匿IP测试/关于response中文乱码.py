# _*_coding:utf-8 _*_
# @Time     :2019/8/19   22:10
# @Author   : 
# @ File　　:test_1.py
# @Software :PyCharm
# @Desc     :判断使用的代理IP是否有用 https://blog.csdn.net/eye_water/article/details/78864071

# 查ip网站 https://www.ipqi.co、http://www.ip111.cn/、http://www.ip138.com/

#  [WinError 10061] 由于目标计算机积极拒绝，无法连接。解决方法，更换代理，将Proxy换一个能够使用的代理。

# timeout 连接超时指的是在你的客户端实现到远端机器端口的连接时（对应的是 connect() ），Request 会等待的秒数。一个很好的实践方法是把连接超时设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口 (TCP packet retransmission window) 的默认大小是 3。

# 关于response中文乱码
"""
第一个问题是，为什么会有ISO-8859-1这样的字符集编码？

iso-8859是什么？  他又被叫做Latin-1或“西欧语言” .  对于我来说，这属于requests的一个bug，在requests库的github里可以看到不只是中国人提交了这个issue.  但官方的回复说是按照http rfc设计的。

下面通过查看requests源代码，看这问题是如何造成的 !

requests会从服务器返回的响应头的 Content-Type 去获取字符集编码，如果content-type有charset字段那么requests才能正确识别编码，否则就使用默认的 ISO-8859-1. 一般那些不规范的页面往往有这样的问题.

第二个问题， 那么如何获取正确的编码？

requests的返回结果对象里有个apparent_encoding函数, apparent_encoding通过调用chardet.detect()来识别文本编码. 但是需要注意的是，这有些消耗计算资源.
至于为毛，可以看看chardet的源码实现.

第三个问题，requests的text() 跟 content() 有什么区别？

requests在获取网络资源后，我们可以通过两种模式查看内容。 一个是r.text，另一个是r.content，那他们之间有什么区别呢？

分析requests的源代码发现，r.text返回的是处理过的Unicode型的数据，而使用r.content返回的是bytes型的原始数据。也就是说，r.content相对于r.text来说节省了计算资源，r.content是把内容bytes返回. 而r.text是decode成Unicode. 如果headers没有charset字符集的化,text()会调用chardet来计算字符集，这又是消耗cpu的事情.

对于requests中文乱码解决方法有这么几种.

方法一:

由于content是HTTP相应的原始字节串，可以根据headers头部的charset把content decode为unicode，前提别是ISO-8859-1编码.

另外有一种特别粗暴方式，就是直接根据chardet的结果来encode成utf-8格式.

如果在确定使用text，并已经得知该站的字符集编码时，可以使用 r.encoding = ‘xxx’ 模式， 当你指定编码后，requests在text时会根据你设定的字符集编码进行转换.

方法二:

根据我抓几十万的网站的经验，大多数网站还是很规范的，如果headers头部没有charset，那么就从html的meta中抽取.

python requests的utils.py里已经有个完善的从html中获取meta charset的函数. 说白了还是一对的正则表达式.

最后，针对requests中文乱码的问题总结:

统一编码，要不都成utf-8, 要不就用unicode做中间码 !

国内的站点一般是utf-8、gbk、gb2312  , 当requests的encoding是这些字符集编码后，是可以直接decode成unicode.

但当你判断出encoding是 ISO-8859-1 时，可以结合re正则和chardet判断出他的真实编码. 可以把这逻辑封装补丁引入进来.
"""


