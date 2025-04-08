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

### 1. 特徴点データの準備
特徴点データを`.dat`ファイルとして準備します。各行には、特徴点の座標を記載します。
例 (`points.dat`):

### 2. ツールの実行

以下のコードを使用して、特徴点を画像に描画します。

```python
from DrawingFeaturePoints import DrawingFeaturePoints

# DrawingFeaturePointsインスタンスを作成
drawer = DrawingFeaturePoints(
    image_path="input_image.jpg",  # 入力画像ファイルのパス
    points_path="points.dat",      # 特徴点データのパス
    output_path="output_image.png", # 出力画像のパス
    shape="circle",                # 描画する形状（circle, square, diamond）
    radius="5px",                  # 半径（例："5px"）
    color="blue",                  # 色（色名または16進数カラーコード）
    shift=True                     # 画像中心を原点にするかどうか
)

# 特徴点を描画
drawer.run()
