import cv2
import os
import json

class DrawingFeaturePoints:

    """特徴点を描画するクラス"""
    def __init__(self, image_folder, points_folder,json_folder):
        self.image_folder = image_folder
        self.points_folder = points_folder
        # jsonファイルの読み込み
        self.json_folder = json_folder
        self.colors = self.load_json_model(f"{json_folder}/colors.json")
        self.shapes = self.load_json_model(f"{json_folder}/shapes.json")

    """ jsonのモデルを読み込む関数"""
    def load_json_model(self, json_file):
        # JSONファイルを読み込む
        with open(json_file, 'r') as f:
            json_model = json.load(f)
        return json_model

    """ 指定したフォルダ内の画像をすべて読み込む関数"""
    def load_images(self):
        loaded_all_images = []
        for image in os.listdir(image_folder):
            # 画像ファイルの拡張子を確認
            if image.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')):
                fullpath = os.path.join(image_folder, image)
                img = cv2.imread(fullpath, cv2.IMREAD_UNCHANGED)
                if img is not None:
                    loaded_all_images.append(img)
                    print(img.shape)
        self.loaded_all_images = loaded_all_images

    """ 指定したフォルダ内の特徴点データをすべて読み込む関数 """
    def load_points(self):
        loaded_all_points = [] # すべてのファイルの特徴点データを格納するリスト
        for point_file in os.listdir(point_folder):
            loaded_points = [] # ファイルの特徴点データを格納するリスト
            # 特徴点データファイルの拡張子を確認
            if point_file.endswith('.txt'):
                fullpath = os.path.join(point_folder, point_file)
                # 特徴点データを読み込む
                with open(fullpath, 'r') as f:
                    for line in f:
                        # 各行のパラメータを取得
                        load_point = []
                        parts = line.split()
                        # デフォルトの設定
                        size = '1px'
                        color = '#f00'
                        shape = 'circle'

                        for part in parts:
                            # 座標を取得
                            if ',' in part:
                                point = tuple(map(float,part.split(',')))
                            # サイズを取得
                            if 'px' in part:
                                size = part
                            # 色を取得
                            if '#' in part:
                                color = part
                            elif part in self.colors:
                                color = self.colors[part]
                            # 形状を取得
                            if part in self.shapes:
                                shape = self.shapes[part]
                        # 行ごとの特徴点データをリストに追加
                        load_point=[point, size, color, shape]
                        loaded_points.append(load_point)
            # ファイル全体の特徴点データをリストに追加
            loaded_all_points.append(loaded_points)
        self.loaded_all_points = loaded_all_points
    
    """ 特徴点を描画する関数 """
    def run(self):
        cv2.circle(self.loaded_all_images[0], (100,100), 2, (255, 0, 0, 255), -1)
        cv2.imwrite('1_landmark_plot.png', self.loaded_all_images[0])


if __name__ == "__main__":
    # クラスのインスタンス
    image_folder = "images"
    point_folder = "points_data"
    json_folder = "json_model"
    drawing_feature_points = DrawingFeaturePoints(image_folder, point_folder, json_folder)
    
    # 画像の読み込み
    drawing_feature_points.load_images()
    # 特徴点データの読み込み
    drawing_feature_points.load_points()

    drawing_feature_points.run()