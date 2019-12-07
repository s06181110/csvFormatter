# csvFormatter

## 概要
ポモドーロテクニックの管理アプリである「Be Focused Pro」で得られる
CSVファイルをGoogleカレンダーにエクスポートできる形式に変更するアプリケーション。

- インストール
```bash
$ git clone https://github.com/s06181110/csvFormatter.git
```


- 実行例
```bash
# 実行
$ make prepare ; make test

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