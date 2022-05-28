# Python Time Manager
Tkinterの練習用に作成した時間管理ツール<br>
main.pyと同じディレクトリに*.xlsxファイルを置くことで
ローカルでタスクや勤怠の時間管理を行う<br>
PostgreSQLによるDB操作練習も兼ねている<br>
Mac OSにPostgreSQLをインストールすることで
ローカル環境内にデータベースを立ててやり取りする<br>
(ネットワークのやり取りを介さないアプリを想定)


# 環境
PostgreSQL 14.3

# About PostgreSQL
## Install PostgreSQL on MacOS
homebrewからinstallする
```
brew install postgresql
```
## launch the PostgreSQL service
brewによるサービスの起動
```
brew services start postgresql
//check status
brew services list | grep postgresql
```

## cheat sheet
### データベースに入る前
データベースに入る
```
psql -U 'ユーザ名' 'データベース名'
```
### データベースに入った後
データベース一覧
```
\l
```
テーブル一覧(今入っていデータベース)
```
\d
```