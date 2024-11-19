# Executive Summary

Salifort Motors is a fictional electric energy vehicle manufacturer. It has a global workforce of over 100,000 employees involved in the research, design, construction, validation, and distribution of electric vehicles. Salifort’s end-to-end vertical integration model has made it a global leader at the intersection of alternative energy and automobiles. After receiving the results of a recent employee survey, senior leadership at Salifort Motors is seeking to increase employee retention. This analysis will involve two major phases:

1. Perform exploratory data analysis to identify the factors driving employees to leave the company.
2. Construct a predictive model to identify employees that are likely to leave the company.

Exploratory data analysis revealed that the likelihood of whether an employee will leave is largely represented by their satisfaction level. This does not appear to vary much between departments at Salifort Motors. Employees are overworked, averaging over 200 hours per month, and in many cases over 250 hours per month. This is enforced through employee evaluation scores; however, these employees are not rewarded with salary increases or promotions.

Performing a binary logistic regression on the data resulted in an accuracy of 83%. However, when looking at the specific case when the model would successfully predict whether an employee would leave the company, all metrics were significantly lower, below 50%.

Modeling the data with a random forest yielded much more accurate predictions, all metrics scored 98%. The most important features, in decreasing order of importance, were satisfaction level, number of projects, tenure, evaluation score, and average monthly hours.

Recommendations made to Salifort Motors aim to directly address the issues found by the EDA. Management should require fewer hours from employees, or reward employees who work exceptionally long hours.
