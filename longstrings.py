maintexbeginning = r"""\documentclass[a4paper,12pt,oneside]{book}
\usepackage[utf8]{inputenc}
\usepackage[T2A]{fontenc} % T2A encoding for Cyrillic fonts.
\usepackage[russian]{babel} % Support for Russian language.
\usepackage{graphicx}

\begin{document}

\author{А.П.Чехов}
\title{Рассказы}
\date{}

\frontmatter
\maketitle
\tableofcontents

\mainmatter
"""

maintexending = r"""\backmatter
% bibliography, glossary and index would go here.

\end{document}"""
