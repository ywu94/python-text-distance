# python-text-distance

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) 
[![Generic badge](https://img.shields.io/badge/pypi%20package-0.1.3-blue.svg)](https://pypi.org/project/pytextdist/)
[![Build Status](https://travis-ci.com/ywu94/python-text-distance.svg?branch=master)](https://travis-ci.com/ywu94/python-text-distance)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-1abc9c.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

A python implementation of a variety of text distance and similarity metrics.

* [Install](#install)
* [How to Use](#use)
* [Module](#module)
  * [Edit Distance](#edit)
     * [Levenshtein Distance & Similarity](#lev_dis)
     * [Longest Common Subsequence Distance & Similarity](#lcs_dis)
     * [Damerau-Levenshtein Distance & Similarity](#dam_dis)
     * [Hamming Distance & Similarity](#ham_dis)
     * [Jaro & Jaro-Winkler Similarity & Similarity](#jaro_dis)
  * [Vector Similarity](#vec)
     * [Cosine Similarity](#cos_sim)
     * [Jaccard Similarity](#jac_sim)
     * [Sorensen Dice Similarity](#sor_sim)
     * [Q-Grams Similarity](#qgr_sim)
* [Customize Preprocess](#preprocessing)

---

<a id='install'></a>
## Install

Requirements: `py>=3.3`, `pyyaml>=5.1,<=5.2`

Install Command: `pip install pytextdist`

---

<a id='use'></a>
## How to use

The functions in this package takes two strings as input and return the distance/similarity metric between them. The preprocessing of the strings are included in the functions with default recommendation. If you want to change the preprocessing see [Customize Preprocessing](#preprocessing).

---
<a id='module'></a>
## Modules

<a id='edit'></a>
### Edit Distance

By default functions in this module consider single character as the unit for editting.

<a id='lev_dis'></a>
**[Levenshtein Distance & Similarity](https://en.wikipedia.org/wiki/Levenshtein_distance)**: edit with insertion, deletion, and substitution

```python
import pytextdist

str_a = 'kitten'
str_b = 'sitting'
dist = pytextdist.edit_distance.levenshtein_distance(str_a,str_b)
simi = round(pytextdist.edit_distance.levenshtein_similarity(str_a,str_b),2)
print(f"Levenshtein Distance:{dist}\nLevenshtein Similarity:{simi}")

>> Levenshtein Distance:3
>> Levenshtein Similarity:0.57
```
<a id='lcs_dis'></a>
**[Longest Common Subsequence Distance & Similarity](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)**: edit with insertion and deletion 

```python
import pytextdist

str_a = 'kitten'
str_b = 'sitting'
dist = pytextdist.edit_distance.lcs_distance(str_a,str_b)
simi = round(pytextdist.edit_distance.lcs_similarity(str_a,str_b),2)
print(f"LCS Distance:{dist}\nLCS Similarity:{simi}")

>> LCS Distance:5
>> LCS Similarity:0.62
```


<a id='dam_dis'></a>
> **[Damerau-Levenshtein Distance & Similarity](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)**: edit with insertion, deletion, substitution, and transposition of two adjacent units


<a id='ham_dis'></a>
> **[Hamming Distance & Similarity](https://en.wikipedia.org/wiki/Hamming_distance)**: edit with substition


<a id='jaro_dis'></a>
> **[Jaro & Jaro-Winkler Similarity](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)**: edit with transposition

<a id='vec'></a>
### Vector Similarity

<a id='cos_sim'></a>
> **[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)**

<a id='jac_sim'></a>
> **[Jaccard Similarity](https://en.wikipedia.org/wiki/Jaccard_index)**

<a id='sor_sim'></a>
> **[Sorensen Dice Similarity](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)**

<a id='qgr_sim'></a>
> **[Q-Grams Similarity](https://www.sciencedirect.com/science/article/pii/0304397592901434)**

<a id='preprocessing'></a>
## Customize Preprocessing

All functions will perform `pytextdist.preprocessing.phrase_preprocessing` to clean the input strings and convert them to a list of tokens.

* **When grain="char" - remove specific characters from the string and convert it to a list of characters**

   The following boolean parameters control what characters to remove/change from the string (all True by default):

   *- ignore_non_alnumspc*: whether to remove all non-numeric/alpha/space characters <br/>
   *- ignore_space*: whether to remove all space <br/>
   *- ignore_numeric*: whether to remove all numeric characters <br/>
   *- ignore_case*: whether to convert all alpha charachers to lower case <br/>

   Example:
  ```python
  import pytextdist
  
  before = 'AI Top-50'
  after = pytextdist.preprocessing.phrase_preprocessing(before, grain='char')
  print(after)
  
  >> ['a', 'i', 't', 'o', 'p']
  ```

* **When grain="word" - convert the string to a list of words and remove specific characters from the words**

   The string is firstly converted to a list of words assuming all words are separated by one space, then the following boolean parameters control what characters to remove/change from the string (all True by default):
   
   *- ignore_non_alnumspc*: whether to remove all non-numeric/alpha/space characters <br/>
   *- ignore_numeric*: whether to remove all numeric characters <br/>
   *- ignore_case*: whether to convert all alpha charachers to lower case <br/>
   
  Example:
  ```python
  import pytextdist
  
  before = 'AI Top-50'
  after = pytextdist.preprocessing.phrase_preprocessing(before, grain='word')
  print(after)

  >> ['ai', 'top']
  ```

Functions under the vector similarity module will also perform `pytextdist.preprocessing.ngram_counter` on the list return from `pytextdist.preprocessing.phrase_preprocessing`.

* **Convert a list of tokens to a counter of the n-grams**

   The following parameter control the n to use for n-grams (1 by default):
   
   *- n*: number of contiguous items to use to form a sequence
   
   Example:
  ```python
  import pytextdist
  
  before = 'AI Top-50 Company'
  after = pytextdist.preprocessing.phrase_preprocessing(before, grain='word')
  print(after)
  ngram_cnt_1 = pytextdist.preprocessing.ngram_counter(after, n=1)
  print(ngram_cnt_1)
  ngram_cnt_2 = pytextdist.preprocessing.ngram_counter(after, n=2)
  print(ngram_cnt_2)

  >> ['ai', 'top', 'company']
  >> Counter({'ai': 1, 'top': 1, 'company': 1})
  >> Counter({'ai top': 1, 'top company': 1})
  ```
