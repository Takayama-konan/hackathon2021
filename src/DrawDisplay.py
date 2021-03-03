# ディスプレイする方法とかを記したファイル


class DrawDisplay:
    def __init__(self):
        pass

    def initialDiplay(self, disp_data, end="\n"):
        """
        初期部分を表示

        @param
            dips_data,list          : 表示するデータ
            end,str,default='\n'    : 最後に出力する文字列
        """
        def disp(line, end):
            if not line:
                pass
            if isinstance(line, list):  # リストが続いている場合
                return disp(line, end)
            else:
                print(line, end="")
                return 0

        print(disp_data)
        for lines in disp_data:
            for idx in lines:
                print(idx, end="")
            print("\n")

        print(end)

    def commandDisplay(self, disp_data, end):
        """
        画面描画のコマンド部分
        """


if __name__ == '__main__':
    drawDisplay = DrawDisplay()
    data = ["Hello", " world"]
    drawDisplay.initialDiplay(data)
