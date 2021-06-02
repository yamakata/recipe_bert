# recipe_bert
## 環境構築

試してませんがおそらくこんな手順ではないかと思っています。
Cancel changes
#### 1. Python仮想環境の作成
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
#### 2. Google Cloud SDK のインストール
[Google Cloud SDK のインストール](https://cloud.google.com/sdk/docs/install?hl=ja)に従ってSDKをインストール。
```gcloud```がインストールされる。

### 3. gcloudの初期化
```
gcloud init
```
ブラウザが立ち上がるので、Google認証でrecipe-bertの編集権限を持つアカウントでログイン。

### 4. モデルのダウンロード
`model/`に原くんが学習してくれた以下のモデルをダウンロード。

サイズが大きいのでgithubには上げていません。GoogleDriveからダウンロードしてください。<br>
[共有アイテム>cookpad_nlp](https://drive.google.com/drive/u/1/folders/1SCHwvx8YNIYnUARjCrxyeOU2g3nIIoe9)
- bert_base_32k_config.json
- model.ckpt-580000_pytorch.bin
- special_tokens_map.json
- tokenizer.zip
- tokenizer_config.json
- vocab.txt

## 実行とデプロイ
### ローカルで実行
Flaskでローカルサーバを起動
```
sh run_local.sh
```
実行テスト<br>
[http://localhost:8000/sent?text=水で洗ったほうれん草を[MASK]]()

### サーバにデプロイ
デプロイのスクリプトを編集。以下は、GCPのプロジェクト名が`webapi-python`の例。もしプロジェクト名が`recipe-classification`ならそのように変更してください。
```
gcloud app deploy --project webapi-python --version main2
```
デプロイのスクリプトを実行。
```
sh deploy.sh
```

```Do you want to continue (Y/n)?```で`Y`を入力。あとは放置。

## コード説明
### main.py
WebAPIのインタフェース

### mybert.py
BERTによる処理部分

### app.yaml
メモリを増やしたかったため、フレックスモードを設定。フレックスモードだと無料で使用できるリソースは無いので注意。<br>
CPU,メモリ、ストレージのサイズを調整。これによってお値段が変わります。料金表は[こちら](https://cloud.google.com/appengine/pricing?hl=ja)<br>
小さすぎるとエラーを返して動かないし、大きいとお値段が高いので注意。<br>
２０２１年４月２４日現在の設定は、以下の通り。これで２７０円/日くらい。
- cpu: 1
- memory_gb: 2.5
- disk_size_gb: 20

## その他
### モデルの学習
学習済みモデルは[共有アイテム>cookpad_nlp](https://drive.google.com/drive/u/1/folders/1SCHwvx8YNIYnUARjCrxyeOU2g3nIIoe9)<br>
モデルの学習コードは[原くんのgithub](https://github.com/y60/cookbert/)


