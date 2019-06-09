from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

# 「事前準備」で取得したAPI KeyとSecret Keyを設定
key = "XXXXXXXXXX"
secret = "XXXXXXXXXX"

# 1秒間隔でデータを取得(サーバー側が逼迫するため)
wait_time = 1

# 検索キーワード(実行時にファイル名の後に指定)
keyword = sys.argv[1]
# 保存用ディレクトリ
savedir = "./" + keyword

# 接続クライアントの作成とサーチの実行
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,           # 検索キーワード
    per_page = 100,           # 取得データ数
    media = 'photos',         # 写真を集める
    sort = 'relevance',       # 最新のものから取得
    safe_search = 1,          # 暴力的な画像を避ける
    extras = 'url_q, license' # 余分に取得する情報(ダウンロード用のURL、ライセンス)
)

# 結果の取り出しと格納
photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
