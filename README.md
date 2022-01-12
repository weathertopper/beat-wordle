# Beat WORDLE

## Running it

```
python3 ./beat-wordle.py <known_wordle> <included_letters> <excluded_letters>
```

### `known_wordle`

The most recent WORDLE guess with green letters in position and dashes `-` everywhere else.

Example: If I guess the word `BLOAT` and the letters `B` and `A` are green, then the `known_wordle` is `B--A-`

### `included_letters`

All yellow letters in no particular order

### `excluded_letters`

All gray letters in no particular order

### Example

I initially guess the word `FRONT`

The letter `F` is green.

The letters `R` and `O` are yellow.

The letters `N` and `T` are gray.

I run `beat-wordle.py` to receive WORDLE candidates:

```bash
$ python3 ./beat-wordle.py F---- RO TN
 -------------------
| WORDLE CANDIDATES |
 -------------------
FAROS
FAVOR
FIORD
FJORD
FLOOR
FLORA
FLOUR
FLUOR
FORAM
FORAY
FORBS
FORBY
FORCE
FORDO
FORDS
FORES
FORGE
FORGO
FORKS
FORKY
FORME
FORMS
FORUM
FOURS
FOYER
FROCK
FROES
FROGS
FRORE
FROSH
FROWS
FROZE
FUROR
```

*Notice:* Words with yellow letters in their previous yellow letter positions are still listed (in this example, `FROZE` with `R` in the known incorrect position). This is a current limitation.