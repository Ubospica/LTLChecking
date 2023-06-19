## LTL formula checking system

*A CS3959 course project*

### Usage
```
echo ... > TS.txt          # the transition system
echo ... > benchmark.txt   # LTL formulas
python3 -m pip install antlr4-python3-runtime
python3 main.py
```

### Structure

#### LTL parser
The project uses Antlr4 to parse the given LTL formula. It will transform the LTL formula into an
AST whose structured is defined in `ltl_ast.py`. Then the AST will be simplified by the following
rules:
- Double negation is eliminated
- `a \/ b` -> `!(!a /\ !b)`
- `a -> b` -> `!(a /\ !b)`
- `[]a` -> `!<>!a` -> simplified using the next rule
- `<>a` -> `True U a`

The AST can be printed in a recursive manner. The printed string is regarded as the key when
comparing two LTL nodes.

The negation of the parsed LTL node will be used in the remaining code as we need to find the
violating circumstances of the given LTL formula.

#### LTL to GNBA

In `ltl2nba.py`, we will use the algorithm discribed in P278 of *Principles of Model Checking* to
convert the LTL node into a generalized NBA. Firstly the closure of the formula is found as:
- `(a, !a)` for every non-negative, non-constant subformula a of $\phi$
- `True` if it is a subformula of $\phi$
- `(a, !a)` for all literals in AP and not existing in $\phi$


Then we will find the element set. For `(a, !a)` above, exactly one in `a` and `!a` can exist in one
consistant. If True exists in $\phi$, the consistant set must contain `True`. Then all such sets
are checked if they sastify other consistancy rules.

Then we will construct the GNBA according the given algorithm.

#### GNBA to NBA

The generalized NBA will be converted into NBA with the algorithm in P195. The algorithm is
implemented in `nba.py`.

#### Cross Product of NBA and TS

The cross product of transition system and NBA is implemented in `verification.py`, which
is described in P200.

#### Persistance Checking

The persistence checking is implemented in `verification.py`. This checking implements the algorithm
described in P211.
