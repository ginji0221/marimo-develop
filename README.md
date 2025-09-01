# uv × marimo 開発環境

## 目次

- [uv × marimo 開発環境](#uv--marimo-開発環境)
  - [目次](#目次)
  - [概要](#概要)
  - [環境情報](#環境情報)
  - [ディレクトリ構成](#ディレクトリ構成)
  - [uv による仮想環境構築](#uv-による仮想環境構築)
    - [uv のインストール](#uv-のインストール)
    - [Githubからプロジェクトをクローン](#githubからプロジェクトをクローン)
    - [Pythonのバージョンを変更する場合 (不要であればスキップ)](#pythonのバージョンを変更する場合-不要であればスキップ)
    - [使用ライブラリの追加 (不要であればスキップ)](#使用ライブラリの追加-不要であればスキップ)
    - [仮想環境の同期](#仮想環境の同期)
    - [Pythonのテスト実行](#pythonのテスト実行)
  - [marimo によるノートブックの起動と実行](#marimo-によるノートブックの起動と実行)
    - [ノートブックの起動](#ノートブックの起動)
    - [アプリケーションとして起動](#アプリケーションとして起動)

## 概要

- uv : Python の仮想開発環境構築を実現するツール
- marimo : Python 向けのオープンソースのリアクティブノートブック
- uvを使用して仮想環境を構築し、marimoを使用したノーブック開発環境を構築する
- デフォルトの仮想環境では、Python3.12を使用している

## 環境情報

- Windows 11 Home
- CPU：13th Gen Intel(R) Core(TM) i7-1355U (1.70 GHz)
- RAM：16.0 GB
- WSL バージョン 2 以上で Ubuntu22.04
- 前提知識として
  - テキストエディタが使えること（VSCode 等、種類は何でもよい）
  - 基本的な linux コマンド（開発は WSL で ubuntu を使うので最低限のコマンドがわかればよい）
  - git のコマンドを使える

## ディレクトリ構成

```bash
root
├── src                         # ソースコード格納フォルダ
│   ├── sample_notebooks                  
│   │   └── sample_notebook.py  # サンプルのノートブックファイル
│   └── sample_program
│       └── main.py             # サンプルプログラム ("Hello World!"と表示するだけ)
├── .gitignore                  # GithubにPushしないファイルとフォルダ群の記述ファイル
├── .python-version             # 仮想環境で使用するPythonのバージョンを指定する
├── pyproject.toml              # プロジェクトに関する設定ファイル
├── README.md                   # 本ドキュメント
├── requirements.txt            # 使用するライブラリに関するファイル
└── uv.lock                     # ライブラリ依存関係, バージョンの管理ファイル
```

## uv による仮想環境構築

### uv のインストール

- Linux / macOS の場合

```bash
# uvのインストール
curl -LsSf https://astral.sh/uv/install.sh | sh

# Pathを通す
source $HOME/.local/bin/env
```

- windowsの場合は[こちら](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)を参考にインストールを行い、以降の作業も適宜Windowsに沿った方法で進めること

### Githubからプロジェクトをクローン

[リモートリポジトリへのリンク](https://github.com/ginji0221/marimo-environment/tree/main#)

```bash    
git clone https://github.com/ginji0221/marimo-environment.git
```

### Pythonのバージョンを変更する場合 (不要であればスキップ)

- デフォルトのPythonのバージョンは3.12となる
- 修正する場合は下記の2点を実施する
  - .python-versionフォルダのバージョンを書き換える (例 : 3.11)
  - pyproject.tomlファイルの`requires-python`が設定したバージョンの範囲内かを確認する (必要であれば修正する)

.python-version

```text
3.11
```  

pyproject.toml (今回は3.10以上の設定なので修正の必要はなし)

```toml
[project]
name = "marimo-environment"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []
```

### 使用ライブラリの追加 (不要であればスキップ)

- ライブラリを追加する場合は `uv add <library>` で追加可能
- まとめてライブラリを追加する場合は下記の2点を実施する
  - requirements.txtにライブラリを追記
  - `uv add -r requirements.txt` を実行
- 不要なライブラリがある場合は、一度pyproject.tomlを `dependencies=[]` としてから再度、`uv add -r requirements.txt` を実行する
- marimoを使用する場合は必ずrequirements.txtにmarimoを含めてください

requirements.txt (下記は追加する際の記入例)

```text
marimo==0.15.1
requests==2.32.5
numpy==2.3.2
```

仮想環境にライブラリのインストール
```bash
uv add -r requirements.txt
```

### 仮想環境の同期

```bash
uv sync
```

### Pythonのテスト実行

- サンプルプログラムを用意しているため、そちらを実行し動作確認をする
- `uv run python <program_name.py>`で仮想環境上でプログラムを実行可能

```bash
uv run python src/sample_program/main.py
```

## marimo によるノートブックの起動と実行

### ノートブックの起動

- marimoを起動するには `uv run marimo edit <program_name.py>` で実行可能
- プログラム名には、既存のファイル名 or 新規ファイル名を指定
- 起動後、下記のように生成されたURLにアクセス
- sample_notebook.py は指数関数の入力値をスライダーで調節できる簡単なものである

サンプルノートブックの起動

```bash
uv run marimo edit src/sample_notebooks/sample_notebook.py
```

URLへのアクセス (下記図のURLリンクをクリック)

![URL Access Image](/images/marimo_url.png)

sample_notebook.py のノートブック

![Sample Notebook](/images/marimo_notebook.png)

### アプリケーションとして起動

- 作成したノートブックをアプリケーションとして起動する
- アプリケーションとして起動する場合、`uv run marimo run <program_name.py>`を実行する

サンプルノートブックをアプリケーションとして起動

```bash
uv run marimo run src/sample_notebooks/sample_notebook.py
```

sample_notebook.py のアプリケーション

![Sample Notebook](/images/marimo_app.png)
