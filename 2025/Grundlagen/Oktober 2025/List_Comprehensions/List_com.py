# Python List Comprehensions – Das Wichtigste
# 1. Definition

# Eine List Comprehension ist eine kurze, elegante Möglichkeit, neue Listen aus bestehenden Iterables zu erzeugen.
# Sie ersetzt oft normale for-Schleifen und macht den Code lesbarer.

# 2. Grundsyntax
# [ Ausdruck for Element in Iterierbares if Bedingung ]


# Ausdruck → Wert, der in die neue Liste kommt (z. B. x*2)

# Element → Variable für jedes Element im Iterierbaren

# Iterierbares → Liste, String, Range, etc.

# if Bedingung → optional, filtert Elemente nach einem Kriterium

# Beispiel:

# zahlen = [1, 2, 3, 4, 5]
# quadrate = [x**2 for x in zahlen if x % 2 == 0]  # Nur gerade Zahlen
# print(quadrate)  # [4, 16]

# 3. Typische Anwendungen

# Transformationen

# namen = ["alice", "bob", "carol"]
# gross = [name.upper() for name in namen]


# Filtern

# zahlen = range(10)
# gerade = [x for x in zahlen if x % 2 == 0]


# Kombinationen / Verschachtelte Schleifen

# liste1 = [1, 2]
# liste2 = [3, 4]
# kombis = [(x, y) for x in liste1 for y in liste2]


# Strings in Listen umwandeln

# wort = "python"
# buchstaben = [b for b in wort]

# 4. Vorteile

# Kürzer und übersichtlicher als klassische for-Schleifen

# Kombiniert Transformation + Filterung + Iteration in einer Zeile

# Oft schneller in der Ausführung

# 5. Tipps zum Lernen

# Schreibe erst die normale Schleife, dann die List Comprehension → Verständnis steigt

# Übe Filter, Transformation, verschachtelte Schleifen

# Denke: [<was in die Liste kommt> for <jede Variable> in <iterierbares> if <Bedingung>]

# 💡 Merksatz:

# „List Comprehensions = Schleife + Ausdruck + optionaler Filter in einer Zeile“



# List Comprehensions sind im Prinzip nur eine Kurzschreibweise für Schleifen.