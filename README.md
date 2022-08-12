# PaperSimilairty
## Background
TAIPEI (Taiwan News) — National Taiwan University on Tuesday (August 9) announced a decision to rescind a master's degree it gave to Lin Chih-chien (林智堅) in 2017, citing plagiarism after a meeting by the school's academic ethics committee.

The review meeting was held in late July and committee members decided to conduct a probe into plagiarism allegations against Lin, Taoyuan candidate of the Democratic Progressive Party (DPP) for the local elections in November. The committee members advised that Lin should be stripped of his master's degree, a decision later approved by the school's Office of Academic Affairs, according to the statement.

The school explained it received multiple plagiarism complaints against Lin since early July and the committee later convened to launch the probe, "in due process with no delay." The committee also collaborated with a third party comprised of scholars and experts in the field and hosted interviews with stakeholders, including Lin himself and the victim, before making the conclusion.

"The act sullied the reputation of National Taiwan University...and the school will reinforce the importance of academic integrity and ethics, not letting it happen again."

In this study, we proposed machine learning method to analyze the similarity between Mr. Lin and Mr. Yu's papers. Provide an objective indicator for your reference.

News: https://news.pts.org.tw/article/594307

## Method
```Jaccard Similarity``` ref: https://medium.com/data-science-bootcamp/understand-jaccard-index-jaccard-similarity-in-minutes-25a703fbf9d7

```Cosine Similarity``` ref: https://medium.com/geekculture/cosine-similarity-and-cosine-distance-48eed889a5c4

```Persion Similarity``` ref: https://medium.com/@cavaldovinos/human-pose-estimation-pose-similarity-dc8bf9f78556


## Install dependencies

```
python -m pip install -r requirements.txt
```

This code was tested with python 3.7

## Code
```Paper_Similarity.ipynb``` is the detailed program explanation, including data exporatlion, data preprocess, model.
```demo.py``` is the demo file of 3 type of similarity search. Please follow the below scrips. ```Lin.txt``` and ```Yu.txt``` can be replaced with the papers you want to review. But please follow the " Paper_Similarity.ipynb " first to convert the file type from pdf to txt.

```
sim = TextSimilarity('/Lin.txt','/Yu.txt')
sim.JaccardSim(a.str_a,a.str_b)
# Out[20]: 0.38188640627665016

sim.splitWordSimlaryty(a.str_a,a.str_b,sim=a.cos_sim)
# Out[21]: 0.9356422914890785

sim.splitWordSimlaryty(a.str_a,a.str_b,sim=a.pers_sim)
# Out[22]: 0.5226242123605999
```

## Result
| Methodology | 林志堅跟余正煌的論文相似度 |
| :--: | :--: |
| Jaccard Similarity | 38.19% |
| Cosine Similarity | 93.56% |
| Persion Similarity | 52.26% |
