How to Use
==============================================================================
下面我们将介绍如何使用这个项目. 我们假设我们刚来到一个 WotLK 巫妖王之怒版本的服务器, 我们建立了 10 个游戏账号, 每个账号上有 1 个角色. 每个职业我们都有一个角色.

.. note::

    这个项目支持多个不同的 WOW 版本, 因为它们的客户端 WTF 目录结构大同小异. 虽然这篇文档是以人气较高的 WotLK 版本为例, 但是你在使用其他版本时依然可以参考本文.

    - :mod:`wow_wtf.exp03_wotlk`

.. note::

    在 `wow_wtf/tests/exp03_wotlk <https://github.com/MacHu-GWU/wow_wtf-project/tree/main/wow_wtf/tests/exp03_wotlk>`_ 目录有一个完整的如何使用这个库项目来管理你的 WTF 配置的例子. 请在阅读本文时跟这个例子互相印证.


.. _account-and-character-configuration:

1. Account and Character Configuration
------------------------------------------------------------------------------
.. note::

    这部分的功能由另一个库 `wow_acc <https://pypi.org/project/wow-acc/>`_ 提供. 你可以参考 `这篇文档 <https://github.com/MacHu-GWU/wow_acc-project>`_ 来了解如何枚举你的账号和角色.

**首先你要枚举你的账号和角色**.

我们在 `acc_dataset.yml <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/acc_dataset.yml>`_ 文件中定义了我们的游戏账号和角色.

.. dropdown:: wow_wtf/tests/exp03_wotlk/acc_dataset.yml

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/acc_dataset.yml
       :language: yaml
       :linenos:

然后我们编写了一个 `acc_dataset.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/acc_dataset.py>`_ 脚本用于生成对所有账号和角色的 enum 模块.

.. dropdown:: wow_wtf/tests/exp03_wotlk/acc_dataset.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/acc_dataset.py
       :language: python
       :linenos:

现在我们就得到了一个可以用 Python 变量引用我们的账号和角色的 `acc_enum.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/acc_enum.py>`_ 模块了.

.. dropdown:: wow_wtf/tests/exp03_wotlk/acc_enum.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/acc_enum.py
       :language: python
       :linenos:


2. Craft Your WTF Config Template
------------------------------------------------------------------------------
**下面我们就需要准备好一些 WTF 配置模板文件了**. 一般你是通过登录游戏, 将游戏内的配置调整到你满意的状态, 然后将对应的配置文件拷贝出来, 作为你的配置模板.

`exp03_wotlk <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/>`_ 目录下有一些文件夹. 每个文件夹都保存了你的一些 WTF 配置模板文件. 例如在 `01_client_config <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/01_client_config/>`_ 中就保存了用多个不同的分辨率, 图像和音频来运行你的客户端的配置文件. 这个目录的结构必须跟 :func:`~wow_wtf.exp03_wotlk.dataset.to_module` 中的定义严格一致, 不然后续的自动化操作就无法进行了.

我建议你查看 `exp03_wotlk <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/>`_ 下面那些以数字开头的文件夹中的配置文件, 了解如何组织你自己的配置文件. 特别是对于 AddOns 插件配置的 lua 文件部分. 例如 `13_account_saved_variables/AtlasLoot.lua <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/13_account_saved_variables/AtlasLoot.lua>`_ 文件, 它不是简单的把你客户端中的 lua 文件拷贝过来就可以的, 而是要用 `jinja2 <https://jinja.palletsprojects.com/en>`_ 模板语言来将原始 lua 文件模板化, 以便随着你的 account 和 character 数量的增加而动态更新.

.. dropdown:: wow_wtf/tests/exp03_wotlk/13_account_saved_variables/AtlasLoot.lua

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/13_account_saved_variables/AtlasLoot.lua
       :language: lua
       :linenos:


3. Generate You WTF Config Enum Module
------------------------------------------------------------------------------
和 :ref:`account-and-character-configuration` 类似, **我们也要将我们的配置文件数据转化成一个 Python 模块, 使得每一个配置文件都是一个 enum**.

我们编写了一个 `wtf_dataset.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/wtf_dataset.py>`_ 脚本用于生成对所有配置文件的 enum 模块.

.. dropdown:: wow_wtf/tests/exp03_wotlk/wtf_dataset.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/wtf_dataset.py
       :language: python
       :linenos:

现在我们就得到了一个可以用 Python 变量引用我们的配置文件的 `wtf_enum.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/wtf_enum.py>`_ 模块了.

.. dropdown:: wow_wtf/tests/exp03_wotlk/wtf_enum.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/wtf_enum.py
       :language: python
       :linenos:


4. Define Your Account / Character and WTF Config Mapping
------------------------------------------------------------------------------
**我们有了 Account / Character 的 Enum, 也有了 WTF Config 的 Enum, 下面就是要指定哪些账号和角色应该使用哪些配置了**. 这个映射关系叫做 mapping.

我们需要编写一个 `wtf_mapping.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/wtf_mapping.py>`_ 模块, 里面导入了我们之前定义的 `acc_enum.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/acc_enum.py>`_ 和 `wtf_enum.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/wtf_enum.py>`_ Enum.

.. dropdown:: wow_wtf/tests/exp03_wotlk/wtf_mapping.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/wtf_mapping.py
       :language: python
       :linenos:

接下来就是定义 :class:`~wow_wtf.exp03_wotlk.mapping.WtfMapping` 对象, 它是一个 mapping 数据的容器. 里面定义了例如针对 account 级别的 UI 设置, 哪些账号使用哪些配置文件, 以及针对 character 级别的 UI 设置, 哪些角色使用哪些配置文件, 等等.

``wow_wtf`` 库还提供了一些函数能让你更方便地定义这些 mapping 数据. 例如:

- :meth:`~wow_wtf.exp03_wotlk.mapping.AccLvlMapping.make_many` 和 :meth:`~wow_wtf.exp03_wotlk.mapping.CharLvlMapping.make_many` 方法可以方便地让你将多个账户或角色和多个配置文件建立映射关系.
- :func:`~wow_wtf.utils.get_values` 方法可以方便地让你获得一个 enum 类的所有 member 的集合. 注意这里是集合, 也就是说你可以用 ``difference`` (取差异), ``intersection`` (取交集), ``union`` (取并集) 这些集合操作进行筛选.


5. Apply WTF Configuration
------------------------------------------------------------------------------
有了 :class:`~wow_wtf.exp03_wotlk.mapping.WtfMapping` 对象之后, **你就可以将你的配置批量应用到你的客户端了**. 你可以使用下面这些方法来将你的配置写入到你的客户端的 WTF 目录中:

- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_client_config`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_account_user_interface`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_account_macros`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_account_saved_variables`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_user_interface`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_chat`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_keybinding`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_layout`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_addons`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_macros`
- :meth:`wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_saved_variables`

`wtf_apply.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/wtf_apply.py>`_ 文件是一个例子, 它展示了如何将我们的配置应用到我们的客户端.

.. dropdown:: wow_wtf/tests/exp03_wotlk/wtf_apply.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/wtf_apply.py
       :language: python
       :linenos:

**How to debug before you apply**

由于 ``apply`` 操作会覆盖 WTF 中已有的文件. 所以在你还不确定你的代码是否正确之前, 你希望能提前进行验证, 或是确保出现问题时能够回滚到之前的状态. 我推荐下面几种方法:

1. 备份你客户端中的 WTF 文件夹, 以备不时之需.
2. 在定义 :class:`~wow_wtf.exp03_wotlk.mapping.Client` 时将目录指向到一个临时目录, 而不是真正的魔兽世界客户端目录. 这样你可以检查生成后的文件, 然后拷贝一小部分到客户端中看看是否惯用.
3. 在调用 ``apply_xyz(...)`` 这些方法时, 将 ``real_run`` 参数设为 ``False``. 这样它只会渲染最终要写入的内容而不会真正写入. 这样可以确定你至少你的 lua 文件没有问题.

.. important::

    有些配置是无法通过回滚 WTF 文件来恢复的. 例如 macro 宏命令, 以及你的动作条数据在你每次进入游戏的时候会将数据保存在服务器端. 而如果你覆盖了原来的 macro 之后又登录游戏导致宏命令丢失或是动作条按钮丢失, 那么你即使回滚了 WTF 文件你再次登录游戏时也无法恢复到之前的状态.

    所以我个人不会用这个工具来管理 macros (虽然它可以), 我更倾向于用 SDM (SupderDopeMacro) 和 MySlots 这样的插件来管理我的宏命令和动作条.
