# @Time   : 2019-03-26 23:49:06
# @Author : lemon_xiuyu
# @Email  : 5942527@qq.com
# @File   : study_requests.py

# 笔记
"""
request
HTTP 协议两大部分
1、Request:  入参
请求方法：
GET   查--获取资源
POST  改--修改资源
PUT   增加
DELETE 删除
OPTION 获取你可以支持的请求方式，常常黑客始终，试探你的接口有哪些方式、资源
HEADER 没有返回体，有请求的头信息和 返回头部信息
请求URL： 协议://服务器IP地址:端口号/接口路径 (协议://域名/接口地址  https://ke.qq.com/course)
请求参数： 传参方式？ url传参 和 表单传参
header 请求头： Content-type ，请求端信息，浏览器、手机版本、request版本、伪装
cookie  放在客户端 保存在本地电脑，服务器地址，最常见登陆的时候，只传cookie不用 传密码了。有时效性。

2、Response: 出参
状态码:
1XX--信息类（Information），表示收到Web浏览器请求，正在进一步的处理中。
2XX--成功类（Successful），表示用户请求被正确接收，理解和处理例如：200 OK
3XX--重定向（Redirection），表示请求没有成功，客户必须采取进一步的动作。
4XX--客户端错误（Client Error）,表示客户端提交的请求有错误 例如： 404 NOT
5XX--服务器错误（Server Error），表示服务器不能完成对请求的处理：如 500

响应信息：服务端返回信息 告诉客户端处理的结果 响应body里
接口校验3步：1、判断状态，2、判断响应信息，3、判断数据库。
cookie：客户端发起的请求到服务端，服务端产生的信息放在cookie里面
header：与Request里面的header有区别：告诉客户端返回来的信息的格式要求，客户端的是想要什么格式。
"""

# 代码
"""
import requests

# 构造请求
# 调用GET请求
# def get(url, params=None, **kwargs): 进入get 第二三个可以不传值
resp = requests.get('http://cn.python-requests.org/zh_CN/latest/')
resp.encoding = 'utf-8'  # 解决乱码
print('响应码', resp.status_code)
# 打印：响应码 200
print('响应信息', resp.text)
# 输出的是html的内容，而且有乱码。
# 再输出到文件里查看一下
with open('index.html', 'w+', encoding='utf-8') as file:  # 上下文管理器，输出到文本。
    file.write(resp.text)
# 注意：with 里面不加encoding='utf-8'依然会乱码。
# ？？？为什么要同时加两个encoding='utf-8'才不会乱码？？
# 通过这四句代码可以快速获取网站上的信息
"""

# 笔记
"""
request支持上面的所有方法

def get(url, params=None, **kwargs):
进入 get 查看里面源码。 get实际调用的是request方法，request就在api.py里面第一个

进入pycharm- View- Iool Windows- Structure里面看左侧，api.py除了支持requests还支持其它好几种http协议的请求方式，这些都调用request方法。

def request(method, url, **kwargs):
    '''Constructs and sends a :class:`Request <Request>`.'''
request是构造了一个Request()对象，Request()对象里面包含发送接口的各种信息参数
第一个是：method --必传:方法
第二个是：url --必传：地址
第三个是：之后有很多 --不必传：传参数。params、data、json必须传dic字典。
data：传参
json：传参
headers:
cookies:带上cookie请求服务端
files：某个接口上传和下载
auth：认证
timeout：客户端需要等待多长时间返回数据 超过N百毫秒就不等了，返回超时。
type timeout：与上面成对出现 指定类型。
allow_redirects：是否允许重定向，类型。了解，少用。
proxies：设置代理 
verify：分http和https，是否做校验
stream：返回response源文件形式，类似Raw
cert：证书，与 verify成对出现
return：：整个request方法要有一个返回值 返回是<Reponse> 对象

def get(url, params=None, **kwargs):
get、post等请求 传参时
除了第一个url是位置传参，后面的一律用=等号 关键字传参。否则位置错乱报错。
"""

# get 下一个是post
"""
import requests

# 登陆接口 get ---url传参 ---params调用
data = {'mobilephone': '15810447656', 'pwd': '123456'}
resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', params=data)
print('请求url', resp.request.url)  # resp.request查看你的请求信息，先看url
print('请求参数', resp.request.body)
print('响应码', resp.status_code)
print('响应信息', resp.text)
# 打印：请求url http://test.lemonban.com/futureloan/mvc/api/member/login?mobilephone=15810447656&pwd=123456
# 打印：请求参数 None
# 打印：响应码 200
# 打印：响应信息 {"status":1,"code":"10001","data":null,"msg":"登录成功"}
# 注意：get只能用params不能用data，否则url不能拼接、响应信息不对。params是模拟url传参的过程，拼接路径。
"""

"""
import requests

# 登陆接口 post ---表单传参 ---data调用
data = {'mobilephone': '15810447656', 'pwd': '123456'}
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
print('请求url', resp.request.url)  # 查看请求信息url
print('请求参数', resp.request.body)  # 查看请求信息body
print('响应码', resp.status_code)
print('响应信息', resp.text)  # json格式的字典，取值不方便，需再转字典，麻烦。
print('响应信息 类型', type(resp.text))
print('响应信息 字典', resp.json())  # 取值方便，直接取字典，无需再转。
print('响应信息 字典取值', resp.json()['code'])  # 直接取字典，直接key取值。不需要先拿resp.text再做序列化。
print('响应信息 字典类型', type(resp.json()))
# 打印：请求url http://test.lemonban.com/futureloan/mvc/api/member/login
# 打印：请求参数 mobilephone=15810447656&pwd=123456
# 打印：响应码 200
# 打印：响应信息 {"status":1,"code":"10001","data":null,"msg":"登录成功"}  # json格式的字典
# 打印：响应信息 类型 <class 'str'>
# 打印：响应信息 字典 {'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}  # 字典
# 打印：响应信息 字典取值 10001
# 打印：响应信息 字典类型 <class 'dict'>
# 注意：post可以用params，但我们这是阉割版，既支持get又支持post。实际项目记死post就用data不用params。

# 我们这个resp里面的信息超级多了，不仅仅上面的两个请求、响应，还有：
print('请求headers', resp.request.headers)
print('请求cookies', resp.request._cookies)  # 注意：这里cookies是protect属性前面要加_下划线
print('响应headers', resp.headers)
print('响应cookies', resp.cookies)
# 总结 request就是这么好用
# 怎么才能知道属性呢？如加_下划线。在不想调用方法情况下，最简单的方法是debug。
# 在第一个print()上打一个断点，右键debug- 打开resp对象里面看到前面加_下划线的都是protect属性，调用都需加_下划线。
# 找到request打开，看我的请求信息里面返回哪些如：_cookies、body表单传参、headers、method、path_url接口请求路径(后面半段)、url整个全路径。
# 除了request，resp里面还包括哪些常见的：status_code返回码、reason代表成功、raw响应(原文件类型)、cookies、encoding编码方式、headers。
# 打印：请求headers {'User-Agent': 'python-requests/2.20.1', ......}
# 打印：请求cookies <RequestsCookieJar[]>
# 打印：响应headers {'Server': 'nginx/1.13.7', 'Date': ......}
# 打印：响应cookies <RequestsCookieJar[<Cookie JSESSIONID=027EF1C5071071E7CC28105C3CC9FEA4 for test.lemonban.com/futureloan>]>
# resp.cookies输出的格式代表什么？--对象。所以思考今后如何传对象进入
"""

# 考出第三方库
"""
导出原来工程里面的第三方库：
方法1、pycharm打包：
进入pycharm- 左上角 View- Tool Windows- Terminal- 在下方工作台进入要保存的目录- 输入pip freeze > req.txt- 回车
方法2、命令行里打包：
通过命令行进入python36的Scripts 里面输入pip freeze > requirements.txt
或进入项目文件夹下的Scripts目录里面输入

放入到新建的工程根目录下：
方法1、pycharm自动识别，直接点顶部提示的  Install requirements
方法2、pycharm没提醒，进入requirements.txt所在目录敲pip install -r requirements.txt

request是做什么的？ 答：是请求http接口的
官方介绍：cn.python-requests.org/zh_CN/latest/
"""

