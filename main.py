from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
       <body>
    <h1>自己紹介</h1>

    <section>
        <h2>基本情報</h2>
        <ul>
            <li>名前：非公開</li>
            <li>誕生日：2003年10月10日</li>
            <li>趣味：
                <ul>
                    <li>旅行に行くこと</li>
                    <li>星空を見ること</li>
                    <li>写真を撮ること</li>
                    <li>ドライブ</li>
                </ul>
            </li>
            <li>おすすめの旅行先：岐阜</li>
            <li>バイト：
                <ul>
                    <li>焼き肉屋</li>
                    <li>和食</li>
                </ul>
            </li>
            <li>好きなアイドル：KAT-TUN</li>
        </ul>
    </section>

    <section>
        <h2>おすすめのYouTubeチャンネル</h2>
        <p><a href="https://www.youtube.com/@yoninochannel">yoninochannel</a></p>
    </section>

    <section>
        <h2>今日5回聞いた歌</h2>
        <p>timelesz ｢Anthem｣</p>
        <p><a href="https://www.youtube.com/watch?v=omk3tMOIJZo&list=RDomk3tMOIJZo&start_radio=1">YouTubeで聴く</a></p>
    </section>

    <section>
        <h2>HTMLサンプル</h2>
        <pre>
            &lt;html&gt;
                &lt;head&gt;
                    &lt;title&gt;Some HTML in here&lt;/title&gt;
                &lt;/head&gt;
                &lt;body&gt;
                    &lt;h1&gt;Look ma! HTML!&lt;/h1&gt;
                &lt;/body&gt;
            &lt;/html&gt;
        </pre>
    </section>

</body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def new_naming(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}