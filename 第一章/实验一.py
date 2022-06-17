import requests

from urllib import parse

# 该实验可能会受到运行环境网络环境影响，失败请检查代理服务器、路由等设置

def get_html(url, time=10):
    head = {
        "User-Agent": "Moill/5.0o (Windows NT 10.0; Win64; x64)" \
                      "AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/79.0.3945.88 Safari/537.36"
    }
    # 设置用户代理，应对简单反爬虫
    try:
        r = requests.get(url, headers=head, timeout=time)
        # 发送请求
        r.encoding = r.apparent_encoding
        # 设置字符编码集
        r.raise_for_status()
        # 返回状态码不为200抛出异常
        return r.text
    except Exception as error:
        print(error)


if __name__ == "__main__":
    parm = {
        "mobile": "18725868135",
        "action": "mobile"
    }
    # 设置参数
    p = parse.urlencode(parm)
    url = "https://www.ip138.com/mobile.asp?"
    url = url + p
    # 字符串拼接
    print(get_html(url))
