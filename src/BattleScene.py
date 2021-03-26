# バトル画面
# メニュー画面

#ユーザ定義#
import DrawDisplay
import CommandManager
import random

my_hp = 89
my_name = "ﾊﾊｯ"
waza_1 = "ハイドロポンプ"
waza_2 = "たいあたり"
enemy_hp = 600
enemy_name = "ゆめのくに"


def run():
    global enemy_hp
    global my_hp
    while enemy_hp > 0:
        DrawDisplay.clear()  # 画面削除

        # 描画
        DrawDisplay.initialDiplay([
            "-----------------",
            "hp : {}".format(my_hp),
            "name : {}".format(my_name),
            "-----------------",
        ])

        command_number = 0
        command_line = [
            """たたかう""",
            """にげる""",
        ]

        DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                   cursol="▶ ", line_end="\n", end="\n")

        key = ""
        while True:
            key = CommandManager.CommandManager().pressKey()  # 入力キー取得
            DrawDisplay.clear()  # 画面を消す

            DrawDisplay.initialDiplay([
                "-----------------",
                "hp : {}".format(my_hp),
                "name : {}".format(my_name),
                "-----------------",
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

        DrawDisplay.clear()  # 画面削除

        if command_number == 1:  # 逃げる処理
            print("{}は逃げ出した...".format(my_name))
            a = input()
            break

        if command_number == 0:  # 戦う処理
            DrawDisplay.clear()
            DrawDisplay.initialDiplay([
                "-----------------",
                "hp : {}".format(my_hp),
                "name : {}".format(my_name),
                "-----------------",
                "どの技でたたかう？",
            ])

            command_line = [  # 技選択(一番上に技の変数、HPなど置いてある)
                """{}""".format(waza_1),
                """{}""".format(waza_2),
            ]

            DrawDisplay.commandDisplay(command_line, command_number=command_number,
                                       cursol="▶ ", line_end="\n", end="\n")

            key = ""
            while True:
                key = CommandManager.CommandManager().pressKey()  # 入力キー取得
                DrawDisplay.clear()  # 画面を消す

                DrawDisplay.initialDiplay([
                    "-----------------",
                    "hp : {}".format(my_hp),
                    "name : {}".format(my_name),
                    "-----------------",
                    "どの技でたたかう？",
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

            DrawDisplay.clear()  # 画面削除

            if command_number == 0:  # ハイドロポンプの処理
                print("{}は{}をはなった！".format(my_name, waza_1))
                a = input()
                damage = random.randint(100, 120)  # ダメージの下限、上限
                enemy_hp = enemy_hp - damage
                print("{}は{}のダメージ！".format(enemy_name, damage))
                print("現在の敵のHP : {}".format(enemy_hp))
                a = input()

            if command_number == 1:  # たいあたりの処理
                print("{}は{}をはなった！".format(my_name, waza_2))
                a = input()
                damage = random.randint(80, 120)  # ダメージの下限、上限
                enemy_hp = enemy_hp - damage
                print("{}は{}のダメージ！".format(enemy_name, damage))
                print("現在の敵のHP : {}".format(enemy_hp))
                a = input()

    return 1  # 異常終了


if __name__ == '__main__':
    run()
