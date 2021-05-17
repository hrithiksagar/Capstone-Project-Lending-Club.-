# Capstone-Project-- 🏦 Lending-Club 💰

<hr>

Resources Links :- 
<br>
[Learning Git Book](https://technocolabs-internship.gitbook.io/internship-prerequisites-learning-resources/)
<br>
[Dataset Git Book](https://technocolabs-internship.gitbook.io/final-project-march/)

<hr>

# Introduction
Using historical data on loans from Lendig Club - including information on whether or not the borrower defaulted (charge-off) - the main objective of this notebook will be to predict if a potential borrower is likely to pay back the loan.

## Our Goal
In this capstone project, You will going to work on LendingClub Dataset obtained from Kaggle and the goal is to try find a better prediction model to prevent investing on '"bad loans". To do that, First, going to implement some data engineering and preprocessing on LendingClub dataset to prepare data for analysis and modeling. Second, you need to apply explanatory data analysis (EDA) to investigate the features. At the end, you use preprocessed data on LendingClub loans labeled on whether or not the borrower defaulted (charged-off) to develop a model and predict whether or not a borrower will pay back their loan. This way in the future when we get a new potential customer who assigned with higher interest loan, we can assess whether or not they are likely to pay back the loan.


## Step One - EDA
For this we frist need to import necessary packages
```
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
```
So here we have 2 choices for the data so in next few steps we will decide to carry on with which dataset ⚙️<br>
1. We have accepted.csv 
2. We have Lending_club_approval_optimization.csv

**We performed some function listed below to get a quick snap peek of our data to decide with which we will continue our work**
<ol>
  <li>We have imported both the data</li>
  <li>data.head()</li>
  <li>data.tail()</li>
  <li>data.describe</li>
  <li>data.target.unique</li>
</ol>
<p float="left">
  <img src="/images/loan_status.png" width="400" />
  <img src="/images/Target.png" width="400" />
</p>

**So from above steps we can conclude that although fullyPaid and chargedOff in accepted have a huge difference in counts but the data have more features and there is scope of making this balanced and have more features for better accuracy . Whereas in combined data we have likely to similar value counts but we dont have as many features which we need so the model trained in this data will be less accurate in real world scenerio's**<br>
**But Since the new combined dataset is already cleaned we will take it into consideration**

<hr>








