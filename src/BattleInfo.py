def shop_battle_info(shop_info=None):
    """
    店名技名など取得
    """
    if shop_info == None:
        return {"店名": None, "技名": "", "攻撃力": 0, "HP": 0}
    shop_name = shop_info[1]  # 店名
    shop_waza = shop_info[-2]  # 技名(メニュー)
    shop_attack = shop_info[-1]  # 攻撃力 (メニュー価格)
    shop_hp = shop_info[3][:-1].split("～")[0]  # HP(価格帯)
    return {"店名": shop_name, "技名": shop_waza, "攻撃力": shop_attack, "HP": shop_hp}
