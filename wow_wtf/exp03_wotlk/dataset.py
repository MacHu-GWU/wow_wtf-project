# -*- coding: utf-8 -*-

"""
这个模块可以生成一个对所有的 WTF config 文件模板的枚举 Python 模块.
详情请看 :func:`to_module` 函数的文档.
"""

import dataclasses
from pathlib_mate import Path


@dataclasses.dataclass
class Folder:
    """
    代表着一类 WTF 配置的模板集合的文件夹. 例如 ``11_account_user_interface`` 就是
    所有账号的用户界面配置文件的文件夹.

    :param name: 文件夹的名字, 例如 ``11_account_user_interface``
    :param classname: 生成的 Python 枚举类的名字, 例如它是 ``AccountUserInterface``
        的话, 最终生成的 Python 枚举类就是 ``class AccountUserInterfaceEnum:``
    :param file_ext: 模板文件的扩展名, 例如 ``.txt``, 我们会用这个来筛选出被视为 "模板" 的文件.
    """

    name: str = dataclasses.field()
    classname: str = dataclasses.field()
    file_ext: str = dataclasses.field()


folder_list = [
    Folder(
        name="01_client_config",
        classname="ClientConfig",
        file_ext=".txt",
    ),
    Folder(
        name="11_account_user_interface",
        classname="AccountUserInterface",
        file_ext=".txt",
    ),
    Folder(
        name="12_account_macros",
        classname="AccountMacros",
        file_ext=".txt",
    ),
    Folder(
        name="13_account_saved_variables",
        classname="AccountSavedVariables",
        file_ext=".lua",
    ),
    Folder(
        name="21_character_user_interface",
        classname="CharacterUserInterface",
        file_ext=".txt",
    ),
    Folder(
        name="22_character_chat",
        classname="CharacterChat",
        file_ext=".txt",
    ),
    Folder(
        name="23_character_keybindings",
        classname="CharacterKeybindings",
        file_ext=".txt",
    ),
    Folder(
        name="24_character_layout",
        classname="CharacterLayout",
        file_ext=".txt",
    ),
    Folder(
        name="25_character_addons",
        classname="CharacterAddons",
        file_ext=".txt",
    ),
    Folder(
        name="26_character_macros",
        classname="CharacterMacros",
        file_ext=".txt",
    ),
    Folder(
        name="27_character_saved_variables",
        classname="CharacterSavedVariables",
        file_ext=".lua",
    ),
]
"""
列出了所有 WTF 配置模板文件夹的规则.
"""

def slugify(s: str) -> str:
    """
    将字符串转换成一个合法的 Python 变量名.
    """
    return s.replace(" ", "_").replace("-", "_").replace("/", "__")


def get_var_name(
    dir: Path,
    path: Path,
):
    """
    从文件路径生成一个合法的 Python 变量名作为 Enum 枚举值的变量名. ``path`` 是这个模板文件
    的路径, 而 ``dir`` 则是 :class:`Folder` 文件夹的路径.
    例如我们有一个 ``${HOME}/11_account_user_interface/default.txt`` 文件, 而 ``dir`` 是
    ``${HOME}/11_account_user_interface``. 那么这个模板文件的变量名就会是 ``default``.

    :param dir:
    :param path:
    """
    relpath = path.relative_to(dir)
    var_name = slugify(str(relpath)).split(".")[0]
    if var_name[0].isalpha() is False: # 如果第一个字符不是字母, 那么加上一个 f_ (file)
        var_name = "f_" + var_name
    return var_name


def to_module(
    dir: Path,
) -> str:
    """
    根据前面 ``folder_list`` 中的设定, 扫描 ``dir`` 文件夹下的所有文件, 生成一个
    Python 模块的字符串. 这个模块包含了所有的 WTF 模板文件的枚举.

    例如你有这样的文件结构:

    .. code-block::

        /{dir}/01_client_config
            ...
        /{dir}/11_account_user_interface
            default.txt
            ...
        /{dir}/12_account_macros
            ...
        /{dir}/13_account_saved_variables
            ...
        /{dir}/21_character_user_interface
            default.txt
            ...
        /{dir}/22_character_chat
            ...
        /{dir}/23_character_keybindings
            ...
        /{dir}/24_character_layout
            ...
        /{dir}/25_character_addons
            ...
        /{dir}/26_character_macros
            ...
        /{dir}/27_character_saved_variables
            ...

    那么最终生成的 Python 模块请参考 TODO

    :param dir: WTF 配置模板文件的根目录.
    """
    lines = [
        "# -*- coding: utf-8 -*-",
        "",
        "from pathlib_mate import Path",
        "",
        "dir_home = Path.home()",
        "",
        "# fmt: off",
        "",
    ]
    tab = " " * 4
    dir_home = Path.home()
    for folder in folder_list:
        dir_folder = dir / folder.name
        lines.append(f"class {folder.classname}Enum:")
        paths = list(dir_folder.select_by_ext(folder.file_ext, recursive=True))
        paths.sort()
        if len(paths):
            for path in paths:
                var_name = get_var_name(dir_folder, path)
                relpath = path.relative_to(dir_home)
                lines.append(f'{tab}{var_name} = dir_home.joinpath("{relpath}") # file://{path}')
        else:
            lines.append(f"{tab}pass")
        lines.append("")
        lines.append("")
    lines.append("# fmt: on")
    lines.append("")
    return "\n".join(lines)
