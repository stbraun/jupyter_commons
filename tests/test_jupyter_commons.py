# -*- coding: utf-8 -*-

"""Tests for `jupyter_commons` package."""
import jupyter_commons.output as jc_out


def test_colorize():
    """Test colorization of string."""
    assert "lightblue" in jc_out.colorize("some message", color="lightblue")
    assert "darkgreen" in jc_out.colorize("some message", color="darkgreen")
