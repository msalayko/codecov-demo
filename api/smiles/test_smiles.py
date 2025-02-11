from .smiles import Smiles

def test_smile():
    assert Smiles().smile() == ":)"
    assert Smiles().frown() == ":("