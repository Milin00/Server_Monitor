# Server Monitor

## 概要

Djangoを用いて開発中のサーバー監視システムです。

現在は監視対象となるWebアプリケーションとして日記アプリを開発しています。
最終的には自作したWebアプリを監視し、稼働状況や応答時間を確認できるシステムの構築を目指しています。

## 開発目的

* Djangoの基礎を習得する
* Webアプリケーション開発の流れを学ぶ
* サーバー監視の仕組みを理解する
* インターンシップ応募用の成果物を作成する

## 使用技術

* Python 3.13
* Django
* SQLite
* Git / GitHub

## 現在実装済み

### Diary App

* 日記モデル作成
* 日記作成フォーム
* 日記保存機能
* テンプレート継承
* Django管理画面対応

## 実装予定

### Diary App

* 日記一覧表示
* 日記詳細表示
* 日記編集
* 日記削除

### Server Monitor

* 監視対象登録
* HTTP監視
* 監視履歴保存
* ダッシュボード表示
* ユーザー認証

## セットアップ

```bash
git clone <repository_url>

cd Server_Monitor

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## 学習記録

本プロジェクトはDjango学習およびポートフォリオ作成を目的として継続的に開発しています。
