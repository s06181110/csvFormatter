# csvFormatter

## 概要

ポモドーロテクニックの管理アプリである「Be Focused Pro」で得られる
CSVファイルをGoogleカレンダーにエクスポートできる形式に変更するアプリケーション。
メインプログラムは[ココ](https://github.com/s06181110/csvFormatter/blob/master/jp/ac/kyoto_su/g1744221/Formatter.py)

- 入力形式

| Start Date            | Duration | Assigned task | Task state |
| ----------            | -------- | ------------- | ---------- |
| Jul 12  2019 22:24:46 | 25       | 読書           |To Do       |

- 出力形式

| Subject | Start Date | Start Time | End Date   | End Time |
| ------- | --------   | ---------- | ---------- | -------- |
| 読書     | 2019-07-12 | 22:24:46   | 2019-07-12 | 22:49:46 |


## インストール
```bash
$ git clone https://github.com/s06181110/csvFormatter.git
```


## 実行例
```bash
# 実行
$ make test

# アプリケーションにして開く
$ make install ; open Formatter.app

# 実行によって生成されたものをなくす
$ make clean

# ドキュメントを見る
$ make doc

# ドキュメントをpydocとして見る
$ make pydoc

# プログラムをリントにかける
$ make lint

```
