# python-text-distance

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) 
[![Generic badge](https://img.shields.io/badge/pypi%20package-0.1.3-blue.svg)](https://pypi.org/project/pytextdist/)
[![Build Status](https://travis-ci.com/ywu94/python-text-distance.svg?branch=master)](https://travis-ci.com/ywu94/python-text-distance)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-1abc9c.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Generic badge](https://img.shields.io/badge/contact-yw693@cornell.edu-blue.svg)]()

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
     * [Q-Gram Similarity](#qgr_sim)
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
from pytextdist.edit_distance import levenshtein_distance, levenshtein_similarity

str_a = 'kitten'
str_b = 'sitting'
dist = levenshtein_distance(str_a,str_b)
simi = levenshtein_similarity(str_a,str_b)
print(f"Levenshtein Distance:{dist:.0f}\nLevenshtein Similarity:{simi:.2f}")

>> Levenshtein Distance:3
>> Levenshtein Similarity:0.57
```
<a id='lcs_dis'></a>
**[Longest Common Subsequence Distance & Similarity](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)**: edit with insertion and deletion 

```python
from pytextdist.edit_distance import lcs_distance, lcs_similarity

str_a = 'kitten'
str_b = 'sitting'
dist = lcs_distance(str_a,str_b)
simi = lcs_similarity(str_a,str_b)
print(f"LCS Distance:{dist:.0f}\nLCS Similarity:{simi:.2f}")

>> LCS Distance:5
>> LCS Similarity:0.62
```

<a id='dam_dis'></a>
**[Damerau-Levenshtein Distance & Similarity](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)**: edit with insertion, deletion, substitution, and transposition of two adjacent units

```python
from pytextdist.edit_distance import damerau_levenshtein_distance, damerau_levenshtein_similarity

str_a = 'kitten'
str_b = 'sitting'
dist = damerau_levenshtein_distance(str_a,str_b)
simi = damerau_levenshtein_similarity(str_a,str_b)
print(f"Damerau-Levenshtein Distance:{dist:.0f}\nDamerau-Levenshtein Similarity:{simi:.2f}")

>> Damerau-Levenshtein Distance:3
>> Damerau-Levenshtein Similarity:0.57
```

<a id='ham_dis'></a>
**[Hamming Distance & Similarity](https://en.wikipedia.org/wiki/Hamming_distance)**: edit with substition; note that hamming metric only works for phrases of the same lengths

```python
from pytextdist.edit_distance import hamming_distance, hamming_similarity

str_a = 'kittens'
str_b = 'sitting'
dist = hamming_distance(str_a,str_b)
simi = hamming_similarity(str_a,str_b)
print(f"Hamming Distance:{dist:.0f}\nHamming Similarity:{simi:.2f}")

>> Hamming Distance:3
>> Hamming Similarity:0.57
```

<a id='jaro_dis'></a>
**[Jaro & Jaro-Winkler Similarity](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)**: edit with transposition

```python
from pytextdist.edit_distance import jaro_similarity, jaro_winkler_similarity

str_a = 'sitten'
str_b = 'sitting'
simi_j = jaro_similarity(str_a,str_b)
simi_jw = jaro_winkler_similarity(str_a,str_b)
print(f"Jaro Similarity:{simi_j:.2f}\nJaro-Winkler Similarity:{simi_jw:.2f}")

>> Jaro Similarity:0.85
>> Jaro-Winkler Similarity:0.91
```

<a id='vec'></a>
### Vector Similarity

By default functions in this module use unigram (single word) to build vectors and calculate similarity. You can change `n` to other numbers for n-gram (n contiguous words) vector similarity. 

<a id='cos_sim'></a>
**[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)**

```python
from pytextdist.vector_similarity import cosine_similarity

phrase_a = 'For Paperwork Reduction Act Notice, see your tax return instructions. For Paperwork Reduction Act Notice, see your tax return instructions.'
phrase_b = 'For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040'
simi_1 = cosine_similarity(phrase_a, phrase_b, n=1)
simi_2 = cosine_similarity(phrase_a, phrase_b, n=2)
print(f"Unigram Cosine Similarity:{simi_1:.2f}\nBigram Cosine Similarity:{simi_2:.2f}")

>> Unigram Cosine Similarity:0.65
>> Bigram Cosine Similarity:0.38
```

<a id='jac_sim'></a>
**[Jaccard Similarity](https://en.wikipedia.org/wiki/Jaccard_index)**

```python
from pytextdist.vector_similarity import jaccard_similarity

phrase_a = 'For Paperwork Reduction Act Notice, see your tax return instructions. For Paperwork Reduction Act Notice, see your tax return instructions.'
phrase_b = 'For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040'
simi_1 = jaccard_similarity(phrase_a, phrase_b, n=1)
simi_2 = jaccard_similarity(phrase_a, phrase_b, n=2)
print(f"Unigram Jaccard Similarity:{simi_1:.2f}\nBigram Jaccard Similarity:{simi_2:.2f}")

>> Unigram Jaccard Similarity:0.47
>> Bigram Jaccard Similarity:0.22
```

<a id='sor_sim'></a>
**[Sorensen Dice Similarity](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)**

```python
from pytextdist.vector_similarity import sorensen_dice_similarity

phrase_a = 'For Paperwork Reduction Act Notice, see your tax return instructions. For Paperwork Reduction Act Notice, see your tax return instructions.'
phrase_b = 'For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040'
simi_1 = sorensen_dice_similarity(phrase_a, phrase_b, n=1)
simi_2 = sorensen_dice_similarity(phrase_a, phrase_b, n=2)
print(f"Unigram Sorensen Dice Similarity:{simi_1:.2f}\nBigram Sorensen Dice Similarity:{simi_2:.2f}")

>> Unigram Sorensen Dice Similarity:0.64
>> Bigram Sorensen Dice Similarity:0.36
```

<a id='qgr_sim'></a>
**[Q-Gram Similarity](https://www.sciencedirect.com/science/article/pii/0304397592901434)**

```python
from pytextdist.vector_similarity import qgram_similarity

phrase_a = 'For Paperwork Reduction Act Notice, see your tax return instructions. For Paperwork Reduction Act Notice, see your tax return instructions.'
phrase_b = 'For Disclosure, Privacy Act, and Paperwork Reduction Act Notice, see separate instructions. Form 1040'
simi_1 = qgram_similarity(phrase_a, phrase_b, n=1)
simi_2 = qgram_similarity(phrase_a, phrase_b, n=2)
print(f"Unigram Q-Gram Similarity:{simi_1:.2f}\nBigram Q-Gram Similarity:{simi_2:.2f}")

>> Unigram Q-Gram Similarity:0.32
>> Bigram Q-Gram Similarity:0.15
```

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
  from pytextdist.preprocessing import phrase_preprocessing
  
  before = 'AI Top-50'
  after = phrase_preprocessing(before, grain='char')
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
  from pytextdist.preprocessing import phrase_preprocessing
  
  before = 'AI Top-50'
  after = phrase_preprocessing(before, grain='word')
  print(after)

  >> ['ai', 'top']
  ```

Functions under the vector similarity module will also perform `pytextdist.preprocessing.ngram_counter` on the list return from `pytextdist.preprocessing.phrase_preprocessing`.

* **Convert a list of tokens to a counter of the n-grams**

   The following parameter control the n to use for n-grams (1 by default):
   
   *- n*: number of contiguous items to use to form a sequence
   
   Example:
  ```python
  from pytextdist.preprocessing import phrase_preprocessing, ngram_counter
  
  before = 'AI Top-50 Company'
  after = phrase_preprocessing(before, grain='word')
  print(after)
  ngram_cnt_1 = ngram_counter(after, n=1)
  print(ngram_cnt_1)
  ngram_cnt_2 = ngram_counter(after, n=2)
  print(ngram_cnt_2)

  >> ['ai', 'top', 'company']
  >> Counter({'ai': 1, 'top': 1, 'company': 1})
  >> Counter({'ai top': 1, 'top company': 1})
  ```
