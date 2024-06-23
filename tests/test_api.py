# -*- coding: utf-8 -*-

from wow_wtf import api


def test():
    _ = api


if __name__ == "__main__":
    from wow_wtf.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf.api", preview=False)
