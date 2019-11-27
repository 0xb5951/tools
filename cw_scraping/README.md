## 目的
CWの仕事レコメンド機能の調査
https://blog.crowdworks.jp/?p=2732

## 実施すること
「あなたの好みアンケート」の差分による仕事のリコメンド対象を調べる

対象ページ
https://crowdworks.jp/public/jobs/recommendations/recommend_for_you

このページを見るには、サイトにログインする必要がある。
処理の最初でログインして、対象ページをファイルに吐き出したら、ログアウトするような処理を実施する。

ログイン対象ページ
https://crowdworks.jp/login

*Chroniumのバージョンとブラウザのバージョンを合わせる必要がある。対応表は以下を参照*
http://chromedriver.chromium.org/downloads

スクレイピング対象ページに表示される依頼要素一覧をcsvで保存する。
`カテゴリ_難易度_期間_継続性_日付.csv`

取得した情報は./scrap_data 配下に格納する

## 構造化データ解析
recommended-job-offers : 全体の囲み
この配下にul, liで各依頼が格納されている

依頼には`data-job_offer_id`という要素が付与されている。
このidに仕事IDが格納されている。

タイトル側のdiv要素クラス名 : class="job_data_column summary"
タイトルはh3タグ配下にa linkのバリューとして存在
カテゴリはタイトルのa linkと並列に、div要素(class:sub_category meta_column)配下のa linkとして存在。
タイトル側のa linkはタイトル部分とカテゴリ部分しか存在しない。

単価と価格帯、応募状況、締め切り情報が存在。
価格側のdiv要素クラス名 : class="job_data_column entry"
仕事方式 : span class="cw-label payment_label"
価格 : b class="amount" 配下のspan要素のvalue 一つ目
応募人数 : b 内部の要素 二つ目
締め切り : b 内部の要素 三つ目
