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

更进一步地, 你可以按照逻辑对这些账号和角色的 enum 进行分组, 这样在之后引用的时候就可以批量引用而不用一个个的手打了. `acc_group.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/acc_group.py>`_ 模块是一个很好的例子.

.. dropdown:: wow_wtf/tests/exp03_wotlk/acc_group.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/acc_group.py
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


.. _generate-wtf-config-enum-module:

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

更进一步地, 你可以按照逻辑对这些 enum 进行分组, 这样在之后引用的时候就可以批量引用而不用一个个的手打了. `wtf_group.py <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/wtf_group.py>`_ 模块是一个很好的例子.

.. dropdown:: wow_wtf/tests/exp03_wotlk/wtf_group.py

    .. literalinclude:: ../../../wow_wtf/tests/exp03_wotlk/wtf_group.py
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
- :func:`~wow_wtf.utils.concat_lists` 方法可以方便地让你将多个 list 连接起来.


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


Manage Multiple Servers and Mappings
------------------------------------------------------------------------------
本节介绍了在你同时玩多个服务器的时候, 有多个客户端, 有多套人物角色和配置的组合的时候, 如何组织你的文件目录来管理数量庞大的 WTF 配置.

首先我们要知道一些规范:

- 用不同的客户端玩不同的服务器. 例如你在用一个客户端玩 2 个私服. 那么建议把你的游戏客户端拷贝一份, 每一个客户端玩不同的私服. 因为不同的私服的服务器名和游戏角色名可能会出现冲突.
- 不要用多个 mapping 来分别管理一个账号下的不同角色. 举例来说, 你一个账号下有 10 个角色, 你用一套 mapping 管理其中的 5 个, 另一套 mapping 管理另外 5 个. 这样是不可以的. 因为很多插件的 lua 文件需要知道你账号下全部的角色名. 如果你切换到其中的 5 个, 那么另外 5 个角色名对于插件来说就是不可知的, 就会损害另外 5 个角色的配置.
- 跟上一条对应, 你可以用多个 mapping 来管理一个服务器上的不同账号. 例如用一套 mapping 管理 5 个账号, 用另一套 mapping 管理另外 5 个账号, 这样做是可以的.

根据这些规范, 我们可以创建下面的目录结构. 在 workspace 下的每一个子目录都应该是一套独立的 mapping. 子目录的文件夹名可以是 ``${server_name}_${description}``. 其中 ``server_name`` 是服务器的名字, ``description`` 是你这套 mapping 的描述. 而这些子目录的结构就跟 `exp03_wotlk <https://github.com/MacHu-GWU/wow_wtf-project/blob/main/wow_wtf/tests/exp03_wotlk/>`_ 目录下的结构一样了.

.. code-block:: bash

    workspace/
    workspace/myserver1_mapping1/
    workspace/myserver1_mapping1/01_client_config/
    workspace/myserver1_mapping1/11_account_user_interface/
    workspace/myserver1_mapping1/12_account_macros/
    workspace/myserver1_mapping1/13_account_saved_variables/
    workspace/myserver1_mapping1/21_character_user_interface/
    workspace/myserver1_mapping1/22_character_chat/
    workspace/myserver1_mapping1/23_character_keybindings/
    workspace/myserver1_mapping1/24_character_layout/
    workspace/myserver1_mapping1/25_character_addons/
    workspace/myserver1_mapping1/26_character_macros/
    workspace/myserver1_mapping1/27_character_saved_variables/
    workspace/myserver1_mapping1/acc_dataset.py
    workspace/myserver1_mapping1/acc_dataset.yml
    workspace/myserver1_mapping1/acc_enum.py
    workspace/myserver1_mapping1/README.rst
    workspace/myserver1_mapping1/wtf_apply.py
    workspace/myserver1_mapping1/wtf_dataset.py
    workspace/myserver1_mapping1/wtf_enum.py
    workspace/myserver1_mapping1/wtf_mapping.py
    workspace/myserver1_mapping1/
    workspace/myserver1_mapping2/
    workspace/myserver2_mapping1/
    workspace/myserver2_mapping2/
