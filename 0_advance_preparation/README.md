## python3
本講義ではpython3(version3.5以降)を使用します。各自の環境に合わせてインストールしておいてください。（インストール方法は検索すると色々でてきますが、個人的には[公式サイト](https://www.python.jp/install/install.html)が良くまとまっていると思います）

ターミナルやコマンドプロンプトで`python3`と入力し以下のようにインタプリタが表示されればOKです。

```bash
$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

なおインタプリタは`quit()`と入力すれば終了することができます。

```
$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> quit()
 $
```

### pythonの必要パッケージ
講義で使用するモジュールを`pip`でインストールします。

```bash
$ python3 -m pip install --upgrade pip
$ python3 -m pip install pycryptodome 
Collecting pycryptodome
  Downloading pycryptodome-3.16.0-cp35-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (2.3 MB)
     |████████████████████████████████| 2.3 MB 4.1 MB/s
Installing collected packages: pycryptodome
Successfully installed pycryptodome-3.16.0
```

pythonインタプリタ内でインストールできているか、適当な関数を呼び出し確認してみます。特にエラーなどが表示されなければ成功です。

```bash
$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Util.number import *
>>> bytes_to_long(b"Hello world!!!")
1468369091346691773900635290804513
```

## opensslのインストール
openssl(version 1.1.1)のインストールを行います。macなら`brew`で、Windowsなら[slproweb.com](https://slproweb.com/products/Win32OpenSSL.html)からインストーラーをダウンロードできると思います。

`openssl version`で`1.1.1`と表示されればOKです。

```bash
$ openssl version
OpenSSL 1.1.1f  31 Mar 2020
```

## 演習ファイルのダウンロード
演習データもろもろはこのリポジトリに配置する予定です。`git clone`でお好きな場所に配置して、適宜`git pull`で更新してもらえればなと思います。

```bash
$ git clone https://github.com/ushigai/security_minicamp_tokyo_2022_SSL-TLS.git
Cloning into 'security_minicamp_tokyo_2022_SSL-TLS'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```

