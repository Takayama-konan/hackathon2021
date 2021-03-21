# メニュー画面

#ユーザ定義#
import DrawDisplay
import CommandManager


def run():
    DrawDisplay.clear()  # 画面削除

    # 描画
    DrawDisplay.initialDiplay([
        "######### メインメニュー #########",
        ""
    ])

    command_number = 0
    command_line = [
        """ステージ選択""",
        """編成""",
        """ガチャ""",
        """ヘルプ""",
        """タイトルへ戻る"""
    ]

    DrawDisplay.commandDisplay(command_line, command_number=command_number,
                               cursol="▶ ", line_end="\n", end="\n")

    key = ""
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        DrawDisplay.initialDiplay([
            "######### メインメニュー #########",
            ""
        ])

        #コマンド操作#
        if key in CommandManager.ENTER:
            print("OK")
            break
        if key in CommandManager.UP:  # 上キー
            command_number -= 1
        if key in CommandManager.DOWN:  # 下キー
            command_number += 1
        elif key in CommandManager.ESC:
            print("Info: ESC終了!(MenuScene, run())")
            return 0

        #コマンド#
        if command_number < 0:  # 一番上ならば一番下に
            command_number = len(command_line)-1
        elif len(command_line)-1 < command_number:  # 一番下ならば一番上に
            command_number = 0

        DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                   cursol="▶ ", line_end="\n", end="\n")

    return 1  # 異常終了


if __name__ == '__main__':
    run()
