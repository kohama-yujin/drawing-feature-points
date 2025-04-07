import cv2
import os

""" 指定したフォルダ内の画像を読み込む関数"""
def load_images(image_folder):
    loaded_images = []
    for image in os.listdir(image_folder):
        # 画像ファイルの拡張子を確認
        if image.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')):
            fullpath = os.path.join(image_folder, image)
            img = cv2.imread(fullpath)
            if img is not None:
                loaded_images.append(img)
    return loaded_images

""" 指定したフォルダ内の特徴点データを読み込む関数 """
def load_points(point_folder):
    loaded_points = []
    for point_file in os.listdir(point_folder):
        # 特徴点データファイルの拡張子を確認
        if point_file.endswith('.txt'):
            fullpath = os.path.join(point_folder, point_file)
            # 特徴点データを読み込む
            with open(fullpath, 'r') as f:
                for line in f:
                    parts = line.split()
                    for part in parts:
                        print(part)
            
                        #points = [tuple(map(float, parts[0].split(','))) ]
    return loaded_points

if __name__ == "__main__":
    # 各フォルダを指定
    image_folder = "images"
    point_folder = "points_data"
    # 画像の読み込み
    loaded_images = load_images(image_folder)
    # 特徴点データの読み込み
    loaded_points = load_points(point_folder)
    print(load_points)