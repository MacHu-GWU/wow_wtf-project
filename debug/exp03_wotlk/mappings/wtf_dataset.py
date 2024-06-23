# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf.api import exp03_wotlk

if __name__ == "__main__":
    dir_here = Path(__file__).absolute().parent
    content = exp03_wotlk.to_module(dir_here)
    dir_here.joinpath("wtf_enum.py").write_text(content)
