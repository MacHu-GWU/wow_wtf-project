# -*- coding: utf-8 -*-

import typing as T
from pathlib import Path
from constants import AccountEnum, RealmEnum, CharacterEnum
from wow_wtf_tree.api import Client, AccountMapping, CharacterMapping


path_default_user_interface = Path()

client = Client(dir=Path("/tmp"), locale="enUS")
all_accounts = [AccountEnum.acc1, AccountEnum.acc2]
all_characters = [CharacterEnum.acc1_realm1_char111, CharacterEnum.acc1_realm1_char112]


mappings: T.List[AccountMapping] = [
    AccountMapping(acc=AccountEnum.acc1, tpl=path_default_user_interface),
    AccountMapping(acc=AccountEnum.acc2, tpl=path_default_user_interface),
]


# path_default_user_interface.write()
# AccountLevel(client=123, account=AccountEnum.acc1).path_config_cache_wtf.write()