from __future__ import absolute_import

from enum import Enum


class ModeName(str, Enum):
    """Makes it easier to list and select a mode.

    One can use auto-completion ModeName.MIXOLYDIAN can be used instead
    of the 'Mixolydian' literal string.
    """

    AEOLIAN = "Aeolian"
    ALTERED = "Altered"
    AUGMENTED_LYDIAN = "Augmentedlydian"
    DOMINANT_BEBOP = "Dominantbebop"
    DORIAN = "Dorian"
    DORIAN_B9 = "Dorianb9"
    DORIAN_SHARP11 = "Doriansharp11"
    HALF_TONE_WHOLE_TONE = "Halftonewholetone"
    HARMONIC_MINOR = "Harmonicminor"
    IONIAN = "Ionian"
    IONIAN_SHARP5 = "Ioniansharp5"
    LOCRIAN = "Locrian"
    LOCRIAN_BEC13 = "Locrianbec13"
    LOCRIAN_BEC9 = "Locrianbec9"
    LYDIAN = "Lydian"
    LYDIAN_B7 = "Lydianb7"
    LYDIAN_BEC9 = "Lydianbec9"
    MAJOR = "Ionian"  # For convenience
    MAJOR_BEBOP = "Majorbebop"
    MAJOR_BLUE = "Majorblue"
    MAJOR_PENTATONIC = "Majorpentatonic"
    MELOD_ICMINOR = "Melodicminor"
    MINOR_BLUES = "Minorblues"
    MINOR_PENTATONIC = "Minorpentatonic"
    MIXOLYDIAN = "Mixolydian"
    MIXOLYDIAN_B13 = "Mixolydianb13"
    MIXOLYDIAN_B9_B13 = "Mixolydianb9b13"
    NATURAL_MINOR = "Aeolian"
    PHRYGIAN = "Phrygian"
    SUPER_LOCRIAN_BB7 = "Superlocrianbb7"
    WHOLE_TONE = "Wholetone"
    WHOLE_TONE_HALF_TONE = "Wholetonehalftone"


SCALES_DICT = {
    "Ionian": [0, 2, 4, 5, 7, 9, 11],
    "Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Lydian": [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "Aeolian": [0, 2, 3, 5, 7, 8, 10],
    "Locrian": [0, 1, 3, 5, 6, 8, 10],
    "Melodicminor": [0, 2, 3, 5, 7, 9, 11],
    "Dorianb9": [0, 1, 3, 5, 7, 9, 10],
    "Augmentedlydian": [0, 2, 4, 6, 8, 9, 11],
    "Lydianb7": [0, 2, 4, 6, 7, 9, 10],
    "Mixolydianb13": [0, 2, 4, 5, 7, 8, 10],
    "Locrianbec9": [0, 2, 3, 5, 6, 8, 10],
    "Altered": [0, 1, 3, 4, 6, 8, 10],
    "Harmonicminor": [0, 2, 3, 5, 7, 8, 11],
    "Locrianbec13": [0, 1, 3, 5, 6, 9, 10],
    "Ioniansharp5": [0, 2, 4, 5, 8, 9, 11],
    "Doriansharp11": [0, 2, 3, 6, 7, 9, 10],
    "Mixolydianb9b13": [0, 1, 4, 5, 7, 8, 10],
    "Lydianbec9": [0, 3, 4, 6, 7, 9, 11],
    "Superlocrianbb7": [0, 1, 3, 4, 6, 8, 9],
    "Wholetone": [0, 2, 4, 6, 8, 10],
    "Majorpentatonic": [0, 2, 4, 7, 9],
    "Minorpentatonic": [0, 3, 5, 7, 10],
    "Majorblue": [0, 2, 3, 4, 7, 9],
    "Minorblues": [0, 3, 5, 6, 7, 10],
    "Halftonewholetone": [0, 1, 3, 4, 6, 7, 9, 10],
    "Wholetonehalftone": [0, 2, 3, 5, 6, 8, 9, 11],
    "Dominantbebop": [0, 2, 4, 5, 7, 9, 10, 11],
    "Majorbebop": [0, 2, 3, 5, 7, 8, 9, 10],
}


class ChordName(str, Enum):
    """Makes it easier to list and select a chord.

    One can use auto-completion ChordName.MAJOR can be used instead of the 'M'
    literal string.

    Not every defined ChordName from CHORDS_DICT_ESSENTIAL is defined as an
    enum here, only the most common ones.
    """

    MAJOR = "M"
    ELEVENTH = "11"
    THIRTEENTH = "13"
    FIFTH = "5"
    POWER = "5"  # For convenience
    SIXTH = "6"
    SEVENTH = "7"
    DOMINANT_SEVENTH = "7"  # For convenience
    NINTH = "9"
    AUGMENTED = "aug"
    DIMINISHED = "dim"
    DIMINISHED_SEVENTH = "dim7"
    MINOR = "m"
    MINOR_ELEVENTH = "m11"
    MINOR_THIRTEENTH = "m13"
    MINOR_SIXTH = "m6"
    MINOR_SEVENTH = "m7"
    MINOR_NINTH = "m9"
    MAJOR_SEVENTH = "maj7"
    SUSPENDED_FOURTH = "sus4"
    SUSPENDED_SECOND = "sus2"


CHORDS_DICT_ESSENTIAL = {
    "M": [0, 4, 7],
    "(b5)": [0, 4, 6],
    "11": [0, 4, 5, 7, 10],
    "11#5": [0, 4, 5, 8, 10],
    "11b5": [0, 4, 5, 6, 10],
    "13": [0, 4, 7, 10, 9],
    "13#5": [0, 4, 8, 9, 10],
    "13b5": [0, 4, 6, 9, 10],
    "5": [0, 7],
    "6": [0, 4, 7, 9],
    "6b5": [0, 4, 6, 9],
    "7": [0, 4, 7, 10],
    "7#5": [0, 4, 8, 10],
    "7b5": [0, 4, 6, 10],
    "7sus2": [0, 2, 7, 10],
    "7sus4": [0, 5, 7, 10],
    "9": [0, 4, 7, 10, 2],
    "9#5": [0, 4, 8, 10, 2],
    "9b5": [0, 4, 6, 10, 2],
    "9sus2": [0, 2, 7, 10, 2],
    "9sus4": [0, 5, 7, 10, 2],
    "aug": [0, 4, 8],
    "aug6": [0, 4, 8, 9],
    "dim": [0, 3, 6],
    "dim(maj11)": [0, 3, 5, 6, 11],
    "dim(maj13)": [0, 3, 6, 9, 11],
    "dim(maj7)": [0, 3, 6, 11],
    "dim(maj9)": [0, 2, 3, 6, 11],
    "dim11": [0, 3, 5, 6, 10],
    "dim13": [0, 3, 6, 9, 10],
    "dim6": [0, 3, 6, 9],
    "dim7": [0, 3, 6, 9],
    "dim9": [0, 2, 3, 6, 10],
    "m": [0, 3, 7],
    "m#5": [0, 3, 8],
    "m(maj11)": [0, 3, 5, 7, 11],
    "m(maj11)#5": [0, 3, 5, 8, 11],
    "m(maj13)": [0, 3, 7, 9, 11],
    "m(maj13)#5": [0, 3, 8, 9, 11],
    "m(maj7)": [0, 3, 7, 11],
    "m(maj7)#5": [0, 3, 8, 11],
    "m(maj9)": [0, 2, 3, 7, 11],
    "m(maj9)#5": [0, 2, 3, 8, 11],
    "m11": [0, 3, 7, 10, 5],
    "m11#5": [0, 3, 5, 8, 10],
    "m13": [0, 3, 7, 10, 9],
    "m13#5": [0, 3, 8, 9, 10],
    "m6": [0, 3, 7, 9],
    "m6#5": [0, 3, 8, 9],
    "m7": [0, 3, 7, 10],
    "m7#5": [0, 3, 8, 10],
    "m7b5": [0, 3, 6, 10],
    "m9": [0, 3, 7, 10, 2],
    "m9#5": [0, 2, 3, 8, 10],
    "maj11": [0, 4, 5, 7, 11],
    "maj11#5": [0, 4, 5, 8, 11],
    "maj11b5": [0, 4, 5, 6, 11],
    "maj13": [0, 4, 7, 11, 9],
    "maj13#5": [0, 4, 8, 9, 11],
    "maj13b5": [0, 4, 6, 9, 11],
    "maj7": [0, 4, 7, 11],
    "maj7#5": [0, 4, 8, 11],
    "maj7b5": [0, 4, 6, 11],
    "maj9": [0, 4, 7, 11, 2],
    "maj9#5": [0, 2, 4, 8, 11],
    "maj9b5": [0, 2, 4, 6, 11],
    "sus2": [0, 2, 7],
    "sus2(#5)": [0, 2, 8],
    "sus2(b5)": [0, 2, 6],
    "sus4": [0, 5, 7],
    "sus4(#5)": [0, 5, 8],
    "sus4(b5)": [0, 5, 6],
}


class NoteName(str, Enum):
    """Makes it easier to list and select a note.

    One can use auto-completion NoteName.A_SHARP instead of the 'A#'
    literal string.
    """

    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"


class Interval(str, Enum):
    """Makes it easier to list and select an interval.

    One can use auto-completion Interval.DIMINISHED_FIFTH instead of the
    'b5' literal string.
    """

    ROOT = "1"
    SECOND = "2" 
    THIRD = "3"
    FOURTH = "4"
    FIFTH = "5"
    SIXTH = "6"
    SEVENTH = "7"
    EIGHTH = "8"
    NINTH = "9"
    TENTH = "10"
    ELEVENTH = "11"
    TWELFTH = "12"


class LongInterval(str, Enum):
    """Makes it easier to list and select a long interval.

    One can use LongInterval.MINOR_SECOND instead of the 'minor_second'
    literal string.
    """

    ROOT = "root"
    SECOND = "second"
    THIRD = "third"
    FOURTH = "fourth"
    FIFTH = "fifth"
    SIXTH = "sixth"
    SEVENTH = "seventh"
    EIGHTH = "eighth"
    NINTH = "ninth"
    TENTH = "tenth"
    ELEVENTH = "eleventh"
    TWELFTH = "twelfth"


CHROMATICS_NOTES = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
CHROMATICS_INTERVALS = [str(i) for i in range(1, 13)]  # ["1", "2", ..., "12"]

FLAT_ALTERATIONS = {
    "P": "P",  # Bb → P
    "S": "S",  # Db → S
    "U": "U",  # Eb → U
    "X": "X",  # Gb → X
    "Z": "Z"   # Ab → Z
}

SHARP_ALTERATIONS = {value: key for (key, value) in FLAT_ALTERATIONS.items()}
FULL_ALTERATIONS = {**FLAT_ALTERATIONS, **SHARP_ALTERATIONS}

# Update ENHARMONICS and alterations to match O-Z notation:
ENHARMONICS = {
    "P": "P",  # A#/Bb → P
    "Q": "Q",  # B → Q
    "R": "R",  # C → R
    "S": "S",  # C#/Db → S
    "T": "T",  # D → T
    "U": "U",  # D#/Eb → U
    "V": "V",  # E → V
    "W": "W",  # F → W
    "X": "X",  # F#/Gb → X
    "Y": "Y",  # G → Y
    "Z": "Z"   # G#/Ab → Z
}

INTERVAL_MAPPING = {
    "root": "1",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "ninth": "9",
    "tenth": "10",
    "eleventh": "11",
    "twelfth": "12"
}

DOTS_FRETBOARD_POSITIONS = [0, 3, 5, 7, 9, 12]
NUMBER_OF_DOTS = [2, 1, 1, 1, 1, 2]

STANDARD_TUNING = ["V", "O", "T", "Y", "Q", "V"]  # E→V, A→O, D→T, G→Y, B→Q

WHITE = "rgb(255,255,255)"
BLACK = "rgb(0,0,0)"
GRAY = "rgb(150,150,150)"
DARK_GRAY = "rgb(200,200,200)"
NO_COLOR = "none"

DOTS_POSITIONS = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
