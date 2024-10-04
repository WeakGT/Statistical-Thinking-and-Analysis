# Statistical Thinking and Analysis
This is "2024 Spring GEC111502 Statistical Thinking and Analysis (統計思維與分析)" course project at National Tsing Hua University (NTHU).

---

This project involves analyzing BMI data and dietary habits.

Data Collection:
- We used Google Forms to collect the data, which was shared publicly on social platforms such as Instagram and Facebook.
- The dataset includes information on sex, height, weight, food group 1, food group 2, fast food consumption frequency, convenience store visit frequency, average daily food intake, and satiety level (fullness).
- Google Forms Link: [Survey Form](https://docs.google.com/forms/d/e/1FAIpQLSdq-oks8Aq22QGXMsD5ZUybYXUXLfIXjrV0VTpRNJsySzbn_w/viewform)

Data Programming:
- Data Cleaning: Missing values in dietary input data were removed.
- Outlier Removal: Outliers are removed based on the interquartile range (IQR) method.
- Statistical Analysis: Levene’s test is used to check for equality of variances, followed by ANOVA to identify significant differences between groups based on dietary habits.
