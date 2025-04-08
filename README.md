# 特徴点描画ツール

このツールは、指定した画像に特徴点を描画するためのツールです。
特徴点は、色・形状・大きさ(半径)のカスタマイズが可能です。

## 環境
- Ubuntu 22.04.5 LTS
- Python 3.10.12
- OpenCV
- NumPy

## 概要
- 特徴点は、円、正方形、ひし形のいずれかで描画できます。
- 描画する特徴点の色、半径、形状はファイルから読み込みや、実行時のオプションで指定するなど、柔軟に設定可能です。
- 色は名前（例：`red`）や16進数カラーコード（例：`#FF5733`）で指定できます。
- 画像の中心を原点として座標を補正するオプションもあります。

## インストール

このツールを使用するには、Pythonの環境が必要です。

### 必要なライブラリのインストール

1. このリポジトリをクローンします。
    ```bash
    git clone https://github.com/username/feature-point-drawing-tool.git
    ```

2. 必要なライブラリをインストールします。
    ```bash
    cd feature-point-drawing-tool
    pip install -r requirements.txt
    ```

## 使用方法

### 1. 特徴点データと画像の準備
特徴点データは`.dat`ファイルとして準備します。各行には、特徴点の座標を記載します。

例 (`points.dat`):

	`npm run dev`100 100  150 100 3px red circle
100 150 #2bbaaf
150 150 green
200 200 5px
250 200 5px diamond
200 250 square black 5px
250 250 black square 5px
	`npm run dev`

### 2. 実行例

以下のコードを使用して、特徴点を画像に描画します。

