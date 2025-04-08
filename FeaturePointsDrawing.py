import cv2
import numpy as np

import HexRGBConverter as hexrgb


#
# 特徴点を描画するクラス
#
class FeaturePointsDrawing:

    def __init__(
        self, image_path, points_path, output_path, shape, radius, color, shift
    ):
        # パスを指定
        self.image_path = image_path
        self.points_path = points_path
        self.output_path = output_path if output_path else "output.png"
        # 形状のリスト
        self.shapes = ["circle", "square", "diamond"]
        # 色のリスト
        self.colors = self.load_colors("color_options/colors.dat")
        # オプションのデフォルト値を設定
        self.shape = shape if shape else "circle"
        self.radius = radius if radius else "3px"
        self.color = color if color else "red"
        # 画像の中心を原点にするかどうか
        self.shift = shift

    #
    # 色の辞書を作成する関数
    #
    def load_colors(self, file_path):
        colors = {}
        with open(file_path, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    color_name = parts[0]
                    color_hex = parts[1]
                    colors[color_name] = color_hex
        return colors

    #
    # 指定した画像を読み込む関数
    #
    def load_images(self):
        # 画像の読み込み
        img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
        if img is not None:
            self.loaded_image = img
        # 画像中心を原点とする場合
        if self.shift:
            height, width = img.shape[:2]
            self.center_position = (width // 2, height // 2)

    #
    # 指定した特徴点データを読み込む関数
    #
    def load_points(self):
        self.loaded_points = []
        # 特徴点データファイルの拡張子を確認
        if self.points_path.endswith(".dat"):
            # 特徴点データを読み込む
            with open(self.points_path, "r") as f:
                for line in f:
                    # 各行のパラメータを取得
                    load_point = []
                    parts = line.split()
                    # 座標を取得
                    point = tuple(map(int, parts[0:2]))
                    # 画像中心を原点とする場合
                    if self.shift:
                        point = tuple(
                            x + y for x, y in zip(point, self.center_position)
                        )

                    # 座標以外のパラメータのデフォルト値を設定
                    shape = self.shape
                    radius = int(self.radius.split("px")[0])
                    color = self.colors[self.color]

                    # 座標以外のパラメータを設定
                    for part in parts:
                        # 形状を取得
                        if part in self.shapes:
                            shape = part
                        # 半径を取得
                        if "px" in part:
                            radius = int(part.split("px")[0])
                        # 色を取得
                        if "#" in part:
                            color = part
                        elif part in self.colors:
                            color = self.colors[part]
                    # 行ごとの特徴点データをリストに追加
                    load_point = [shape, point, radius, color]
                    self.loaded_points.append(load_point)

    #
    # 特徴点を描画する関数
    #
    def run(self):
        # 画像の読み込み
        self.load_images()
        # 特徴点データの読み込み
        self.load_points()
        # 色の変換
        color_converter = hexrgb.HexRGBConverter()

        # 特徴点を描画
        for point_data in self.loaded_points:
            # 色の変換
            rgb = color_converter.hex_to_rgb(point_data[3])

            # 円を描画
            if point_data[0] == "circle":
                cv2.circle(
                    self.loaded_image,
                    point_data[1],  # 座標
                    point_data[2],  # 半径
                    (rgb[2], rgb[1], rgb[0], 255),  # OpenCVはBGR形式
                    -1,  # 塗りつぶし
                )

            # 正方形を描画
            if point_data[0] == "square":
                # 正方形の4つの頂点を計算
                offsets = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]) * point_data[2]
                pts = np.array(point_data[1], dtype=np.int32) + offsets
                # reshapeして4次元配列に変換
                # OpenCVのfillPoly関数は4次元配列を必要とする
                pts = pts.reshape((-1, 1, 2))

                cv2.fillPoly(
                    self.loaded_image,
                    [pts],  # 頂点の配列
                    (rgb[2], rgb[1], rgb[0], 255),  # OpenCVはBGR形式
                )

            # ひし形を描画
            if point_data[0] == "diamond":
                # ひし形の4つの頂点を計算
                offsets = np.array([[0, -1], [1, 0], [0, 1], [-1, 0]]) * point_data[2]
                pts = np.array(point_data[1], dtype=np.int32) + offsets
                # reshapeして4次元配列に変換
                # OpenCVのfillPoly関数は4次元配列を必要とする
                pts = pts.reshape((-1, 1, 2))

                cv2.fillPoly(
                    self.loaded_image,
                    [pts],  # 頂点の配列
                    (rgb[2], rgb[1], rgb[0], 255),  # OpenCVはBGR形式
                )

        cv2.imwrite(self.output_path, self.loaded_image)
        print(f'Output image saved to "{self.output_path}"')
