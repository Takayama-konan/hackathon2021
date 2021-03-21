# 最初に表示される画面

#ユーザ定義#
import DrawDisplay
import CommandManager
import MenuScene


def run():
    DrawDisplay.clear() #画面削除

    # 描画
    DrawDisplay.initialDiplay([
        "####################################",
        "######### HOT PEPPER WALK! #########",
        "####################################",
        "",
        "         - PRESS ENTER KEY -"
    ])

    key = ""
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        if key == "Enter":
            print("OK")
            ret = MenuScene.run()
            if ret == 0:  # ESC終了
                break
        elif key == "Esc":
            print("Info: ESC終了!(InitialScene, draw())")
            return 0

    return 0


if __name__ == '__main__':
    draw()
