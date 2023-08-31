import base64 as b64
from typing import Union
from collections.abc import Mapping

DIT = "."
DAH = "-"
# charsep = " "
# wordsep = " / "
# a dict is obligatory
# https://en.wikipedia.org/wiki/Morse_code
# warning: contains identical values - non-latin extensions
# manually typed in so er
_rev = lambda _d: {_v: _k for _k, _v in _d.items()}

def _morse(_dit=".", _dah="-") -> Mapping[Union[str, int], str]:\
    # https://en.wikipedia.org/wiki/Morse_code
    # warning: contains identical values - non-latin extensions
    # manually typed in so errors could inevitably occur
    _d = {
        # letters
        "a": _dit + _dah,
        "b": _dah + _dit * 3,
        "c": (_dah + _dit) * 2,
        "d": _dah + _dit * 2,
        "e": _dit,
        "f": _dit * 2 + _dah + _dit,
        "g": _dah * 2 + _dit,
        "h": _dit * 4,
        "i": _dit * 2,
        "j": _dit + _dah * 3,
        "k": _dah + _dit + _dah,
        "l": _dit + _dah + _dit * 2,
        "m": _dah * 2,
        "n": _dah + _dit,
        "o": _dah * 3,
        "p": _dit + _dah * 2 + _dit,
        "q": _dah * 2 + _dit + _dah,
        "r": _dit + _dah + _dit,
        "s": _dit * 3,
        "t": _dah,
        "u": _dit * 2 + _dah,
        "v": _dit * 3 + _dah,
        "w": _dit + _dah * 2,
        "x": _dah + _dit * 2 + _dah,
        "y": _dah + _dit + _dah * 2,
        "z": _dah * 2 + _dit * 2,
        # numbers
        0: _dah * 5,
        1: _dit + _dah * 4,
        2: _dit * 2 + _dah * 3,
        3: _dit * 3 + _dah * 2,
        4: _dit * 4 + _dah * 1,
        5: _dit * 5,
        6: _dah + _dit * 4,
        7: _dah * 2 + _dit * 3,
        8: _dah * 3 + _dit * 2,
        9: _dah * 4 + _dit,
        # punctuations
        ".": (_dit + _dah) * 3,
        ",": _dah * 2 + _dit * 2 + _dah * 2,
        "?": _dit * 2 + _dah * 2 + _dit * 2,
        "'": _dit + _dah * 4 + _dit,
        "!": (_dah + _dit) * 2 + _dah * 2,
        "/": _dah + _dit * 2 + _dah + _dit,
        "(": _dah + _dit + _dah * 2 + _dit,
        ")": _dah + _dit + _dah * 2 + _dit + _dah,
        "&": _dit + _dah + _dit * 3,
        ":": _dah * 3 + _dit * 3,
        ";": (_dah + _dit) * 3,
        "=": _dah + _dit * 3 + _dah,
        "+": (_dit + _dah) * 2 + _dit,
        "-": _dah + _dit * 4 + _dah,
        "_": _dit * 2 + _dah * 2 + _dit + _dah,
        '"': _dit + _dah + _dit * 2 + _dah + _dit,
        "$": _dit * 3 + _dah + _dit * 2 + _dah,
        "@": _dit + _dah * 2 + _dit + _dah + _dit,
        # prosigns (purposefully omitted)
        # "sk": _dit * 3 + _dah + _dit + _dah,
        # ...
        # non-latin extensions (purposefully omitted)
        # "à": _dit + _dah * 2 + _dit + _dah,
        # "ä": (_dit + _dah) * 2,
        # "å": _dit + _dah * 2 + _dit + _dah,
        # "ą": (_dit + _dah) * 2,
        # "æ": (_dit + _dah) * 2,
        # "ć": _dah + _dit + _dah + _dit * 2,
        # "ĉ": _dah + _dit + _dah + _dit * 2,
        # "ç": _dah + _dit + _dah + _dit * 2,
        # # "ch": _dah * 4,
        # "đ": _dit * 2 + _dah + _dit * 2,
        # "ð": _dit * 2 + _dah * 2 + _dit,
        # "é": _dit * 2 + _dah + _dit * 2,
        # "è": _dit + _dah + _dit * 2 + _dah,
        # "ę": _dit * 2 + _dah + _dit * 2,
        # "ĝ": _dah * 2 + _dit + _dah + _dit,
        # "ĥ": _dah * 4,
        # "ĵ": _dit + _dah * 3 + _dit,
        # "ł": _dit + _dah + _dit * 2 + _dah,
        # "ń": _dah * 2 + _dit + _dah * 2,
        # "ñ": _dah * 2 + _dit + _dah * 2,
        # "ó": _dah * 3 + _dit,
        # "ö": _dah * 3 + _dit,
        # "ø": _dah * 3 + _dit,
        # "ś": _dit * 3 + _dah + _dit * 3,
        # "ŝ": _dit * 3 + _dah + _dit,
        # "š": _dah * 4,
        # "þ": _dit + _dah * 2 + _dit * 2,
        # "ü": _dit * 2 + _dah * 2,
        # "ŭ": _dit * 2 + _dah * 2,
        # "ź": _dah * 2 + _dit * 2 + _dah + _dit,
        # "ż": _dah * 2 + _dit * 2 + _dah,
    }
    return _d

def morse(s: str, _dit=".", _dah="-", _char_sep=" ", _word_sep=" / ") -> str:
    _d = _morse(_dit, _dah)
    return _word_sep.join([_char_sep.join([_d[str(_chr)] if _chr in _d else _chr for _chr in word]).strip(_char_sep) for word in [list(i) for i in s.lower().split()]]).strip(_word_sep)   # it is what it is

def morse_rev(s: str, _dit=".", _dah="-", _char_sep=" ", _word_sep=" / ", _null_repr="#") -> str:
    _d = _rev(_morse(_dit, _dah))
    return " ".join(["".join([_d[_chr] if _chr in _d else _null_repr for _chr in word]) for word in [i.split(_char_sep) for i in s.split(_word_sep)]])


print(morse("hey!"))