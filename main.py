import argparse
import DrawingFeaturePoints as dfp


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Draws feature points on the image.",
    )

    #
    # 引数の設定
    #

    # 必須入力
    parser.add_argument("-i", required=True, help="Input image path")
    parser.add_argument("-p", required=True, help="Input points path")
    # オプション入力
    parser.add_argument(
        "-s",
        help="Shape of points (circle)",
    )
    parser.add_argument(
        "-r",
        help="Radius of points (in pixels)",
    )
    parser.add_argument(
        "-c",
        help="Color of points (hex or name)",
    )
    # 画像の中心を原点にするかどうか
    parser.add_argument(
        "--shift",
        action="store_true",
        help="Using the center of the image as the origin",
    )
    # 出力画像のパス
    parser.add_argument("--o", help="Output image path")

    # 引数解析
    args = parser.parse_args()

    # 描画クラスのインスタンス
    drawer = dfp.DrawingFeaturePoints(
        args.i, args.p, args.o, args.s, args.r, args.c, args.shift
    )
    # 描画を実行
    drawer.run()


if __name__ == "__main__":
    main()
