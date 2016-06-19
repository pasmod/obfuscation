# Obfuscation
Evaluation of the Author Masking Task at PAN2016

#### Problem Description
An obfuscation software is called:
* safe, if a forensic analysis does not reveal the original author of its obfuscated texts,
* sound, if its obufscated texts are textually entailed with their originals, and
* proper, if its obfuscated texts are inconspicuous.

This project describes our methodology to evaluate the 3 approaches submitted to PAN 2016, Author Masking competition.

#### Folder Structure
* **corpora**:
    * **pan13-pan15-author-verification-training-corpus-english**: this folder contains all training instances of the author verification task from PAN2013 till PAN2015. Problem named are slightly modified to indicate the competition year. Also a new truth file is added which is simply the concatentation of all truth files from PAN2013 till PAN2015.
    * **pan16-author-masking-training-dataset-2016-02-17**: contains the training instances for author masking task at PAN2015. These instances are just a subset of instances from PAN2013 till PAN2015.
* **glad**: implementation of the paper "GLAD: Groningen Lightweight Authorship Detection". The source code is copied from [here](https://github.com/pan-webis-de/glad). We eliminated some unnecessary files for the evaluation.
* **model**: contains the model trained on PAN2013 till PAN2015. Training is done using the following command:
```python
python3 glad-main.py --training $trainingDataset \
                     -i $inputDataset \
                     --save_model $modelDir
```
* **reconstructor.py**: contains some simple functions to concatenate the submitted obfuscations and write them as a single file to disk.
* **results**: contains the submission of teams A, B and C. Each submission contains a folder **out** consisting of the submitted json files and a file called **answers.txt** generated by us using glad, that contains the evaluation results.
    * author-masking-participantA-2016-05-24-04-49-53
    * author-masking-participantB-2016-05-24-16-57-58
    * author-masking-participantC-2016-06-02-11-02-18

Evaluation is done using the following command:
```python
python3 glad-main.py -i $inputDataset -m $modelDir -o Out
```
#### Results
The participants' answers are evaluated according the c@1 measure.

|     | Team A | Team B | Team C |
|:---:|:------:|:------:|:------:|
| C@1 |  0.443 |  0.512 |  0.468 |
