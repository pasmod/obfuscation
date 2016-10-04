# Obfuscation
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/pasmod/obfuscation/blob/master/License.md)

Evaluation of the Author Masking Task at PAN2016

#### Motivation
Author masking is the task of paraphrasing a document so that its writing style no longer matches that of its original author. This task was introduced
as part of the 2016 PAN Lab on Digital Text Forensics, for which a total of three research teams submitted their results. This work describes our methodology to
evaluate the submitted obfuscation systems based on their safety, soundness and sensibleness. For the first two dimensions, we introduce automatic evaluation
measures and for sensibleness we report our manual evaluation results.

An obfuscation software is called:
* safe, if a forensic analysis does not reveal the original author of its obfuscated texts,
* sound, if its obufscated texts are textually entailed with their originals, and
* sensible, if its obfuscated texts are inconspicuous.

#### Folder Structure
```
+--
+-- corpora (contains the training instances of the competition)
|   +-- pan13-pan15-author-verification-training-corpus-english/
|   +-- pan16-author-masking-training-dataset-2016-02-17/
+-- safeness (results obtained for safeness)
|   +-- glad (implementation of the GLAD algorithm)
|   +-- model (trained GLAD model)
+-- scripts (scripts to evaluate the submissions)
+-- sensibleness (results obtained for sensibleness)
+-- soundness (results obtained for soundness)
+-- submissions (submissions of the teams)
```

#### Results Safeness
The results of applying GLAD on the 2016 training set. Notice that all problems
have postive labels, meaning that known documents and unknown documents all have
the same author.

C@1: 0.656

The participants' answers are evaluated according the c@1 measure.

|     | Team A | Team B | Team C |
|:---:|:------:|:------:|:------:|
| C@1 |  0.411 |  0.467 |  0.477 |

#### Results Soundness
We measured the semantic textual similarity (STS) between the original text segments and their paraphrases with the *Overlap* method from http://m-mitchell.com/NAACL-2016/SemEval/pdf/SemEval92.pdf

The best possible score would be a mean of 5. The worst possible score is 0.

Results:

|          | Team A | Team B | Team C |
|----------|:--------:|:--------:|:--------:|
| Mean STS | 4.87   | 4.04   | 4.48   |

#### Results Sensibleness
We manually annotated a subset of 20 problems (3 paraphrases from each problem) for each team. We used 3 labels: 2 (comprehensible), 1 (partially comprehensible), and 0 (incomprehensible)

The following table reports the mean of all scores. The highest possible score is 2, the lowest 0.


|          | Team A | Team B | Team C |
|----------|:--------:|:--------:|:--------:|
| Average score | 1.94   | 0.57   | 1.20   |

# Citation
I you want to cite us in your work, please use the following bibtex entry:
``` bash
@inproceedings{DBLP:conf/clef/LiebeckM016,
  author    = {Matthias Liebeck and
               Pashutan Modaresi and
               Stefan Conrad},
  title     = {Evaluating Safety, Soundness and Sensibleness of Obfuscation Systems},
  booktitle = {Working Notes of {CLEF} 2016 - Conference and Labs of the Evaluation
               forum, {\'{E}}vora, Portugal, 5-8 September, 2016.},
  pages     = {920--928},
  year      = {2016},
  crossref  = {DBLP:conf/clef/2016w},
  url       = {http://ceur-ws.org/Vol-1609/16090920.pdf},
  timestamp = {Thu, 11 Aug 2016 15:07:52 +0200},
  biburl    = {http://dblp.uni-trier.de/rec/bib/conf/clef/LiebeckM016},
  bibsource = {dblp computer science bibliography, http://dblp.org}
}
```
