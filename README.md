# python-text-distance

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) 
[![Generic badge](https://img.shields.io/badge/pypi%20package-0.1.1-blue.svg)](https://pypi.org/project/pytextdist/)
[![Build Status](https://travis-ci.com/ywu94/python-text-distance.svg?branch=master)](https://travis-ci.com/ywu94/python-text-distance)

A python implementation of a variety of text distance and similarity metrics.

---

## Install

Requirements: `py>=3.3`, `pyyaml>=5.1.2`

Install Command: `pip install pytextdist`

---

## Modules

### Edit Distance

All edit distances listed in [Edit Distance on Wikipedia](https://en.wikipedia.org/wiki/Edit_distance) are implemented.

> **[Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)**: edit with insertion, deletion, and substitution

> **[Longest Common Subsequence Distance](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)**: edit with insertion and deletion 

> **[Damerau-Levenshtein Distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)**: edit with insertion, deletion, substitution, and transposition of two adjacent units

> **[Hamming Distance](https://en.wikipedia.org/wiki/Hamming_distance)**: edit with substition

> **[Jaro & Jaro-Winkler Similarity](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)**: edit with transposition

