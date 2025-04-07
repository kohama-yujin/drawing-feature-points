import cv2
import os
import json


#
# 特徴点を描画するクラス
#
class DrawingFeaturePoints:

    def __init__(
        self, image_path, points_path, output_path, shape, radius, color, shift
    ):
        # パスを指定
        self.image_path = image_path
        self.points_path = points_path
        self.output_path = output_path
        # オプション入力
        self.shape = shape
        self.radius = radius
        self.color = color
        # 画像の中心を原点にするかどうか
        self.shift = shift
        # 形状のリスト
        self.shapes = ["circle"]
        # 色のリスト
        self.colors = self.load_colors("color_options/colors.dat")

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
        # 画像ファイルの拡張子を確認
        if self.image_path.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")):
            # 画像の読み込み
            img = cv2.imread(self.output_path, cv2.IMREAD_UNCHANGED)
            if img is not None:
                self.loaded_image = img

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
                    print(point)

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
        print(self.loaded_image)
        print(self.loaded_points)

        # # 特徴点を描画
        # for index, img in enumerate(self.loaded_all_images):
        #     for points_data in self.loaded_all_points[index]:
        #         # 円を描画
        #         if points_data[0] == "circle":
        #             cv2.circle(
        #                 img,
        #                 points_data[1],
        #                 points_data[2],
        #                 (255, 0, 0, 255),
        #                 -1,
        #             )
        #     cv2.imwrite(f"{self.output_folder}/{self.image_names[index]}", img)
