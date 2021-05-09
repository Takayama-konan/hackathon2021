# 編成画面

# メニュー画面

#ユーザ定義#
import DrawDisplay
import CommandManager


def run():
    DrawDisplay.clear()  # 画面削除

    # 装備情報取得
    personal_data = []
    with open("./data/save_personal.csv", "r", encoding="utf-8") as f:
        for line in f:
            personal_data.append(line.strip(
                "\n").replace("\u3000", " ").split(","))

    try:
        equipment_shop_name = personal_data[1][1]
    except IndexError:  # データが無いとき
        equipment_shop_name = "所持お店なし"

    # 所持お店情報取得
    shop_data = []
    with open("./data/save_shop.csv", "r", encoding="utf-8") as f:
        for line in f:
            shop_data.append(tuple(line.strip(
                "\n").replace("\u3000", " ").split(",")))
            shop_data = list(set(shop_data))  # 重複削除(実際はお店取得の際に重複を削除すべき)
    shop_name_data = [idx[1] for idx in shop_data]
    shop_dict = dict(zip(shop_name_data, shop_data))
    # print(shop_dict)

    # 描画
    DrawDisplay.initialDiplay([
        "######### 編成 #########",
        "",
        f"\t現在装備中のお店: {equipment_shop_name}",
        "",
        "===== 所持しているお店 =====",
        "",
    ])

    command_number = 0

    command_line = shop_name_data+["もどる"]

    DrawDisplay.commandDisplay(command_line, command_number=command_number,
                               cursol="▶ ", line_end="\n", end="\n")

    key = ""
    while True:
        key = CommandManager.CommandManager().pressKey()  # 入力キー取得
        DrawDisplay.clear()  # 画面を消す

        #コマンド操作#
        if key in CommandManager.ENTER:
            if command_number == len(command_line)-1:  # もどる
                # print("return")
                return

            equipment_shop_name = shop_name_data[command_number]  # 装備

            # 装備情報登録
            personal_data[1] = list(shop_dict[equipment_shop_name])
            with open("./data/save_personal.csv", "w", encoding="utf-8") as f:
                for idx in personal_data:
                    f.write(",".join(idx)+"\n")

        # 描画
        DrawDisplay.initialDiplay([
            "######### 編成 #########",
            "",
            f"\t現在装備中のお店: {equipment_shop_name}",
            "",
            "===== 所持しているお店 =====",
            "",
        ])

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

"""
編成画面のUI 例


== 編成 ==

<甲南大学学食>
HP: 00
技:
\t・うどん ATK: 00
\t・天津飯 ATK: 00
電話番号: 0000-0000-0000

= 所持しているお店 =
・甲南大学学食
・甲南大学生協 13号館

"""
