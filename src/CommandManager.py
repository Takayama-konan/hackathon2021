# コマンドを押したり引いたりすることを感知する
"""

参考:
ASCII https://theasciicode.com.ar/ascii-control-characters/escape-ascii-code-27.html
"""

from msvcrt import getch


class CommandManager:
    def __init__(self):
        """
        ASCIIコードでKeyを指定
        {ASCII:押されたときの名前}
        """

        self.setKey = {
            119: "w",
            115: "s",
            97: "a",
            98: "b",
            100: "d",
            13: "Enter",
            27: "Esc",
        }

    def pressKey(self):
        """
        キーボードを押したときに実行される関数
        @return:
            key name， e.g. [e]キーを押されたときは"e"と返る．
            変数: setKeyで登録されていない場合は"NOT_SET_KEY"と返る．
        """
        key = ord(getch())

        if key in self.setKey:
            return self.setKey[key]
        else:
            return "NOT_SET_KEY"
