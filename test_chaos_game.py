import chaos_game as cg
import pytest as pt


def test_chaos_constructor():
    g = cg.ChaosGame(1)
    assert g._n == 3

def test_show_exception():
    with pt.raises(Exception):
        g = cg.ChaosGame()
        g.show(True)

def test_savepng_exception():
    with pt.raises(Exception):
        g = cg.ChaosGame()
        g.savepng("bigmanting")

def test_plot_exception():
    with pt.raises(Exception):
        g = cg.ChaosGame()
        g.plot("bigmanting")

