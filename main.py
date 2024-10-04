import pandas as pd
import scipy.stats as stats

def check_invalid_vals(df):
    invalid_vals = {
        '食物1': df[(df['食物1'] < 0) | (df['食物1'] > 10)],
        '食物2': df[(df['食物2'] < 0) | (df['食物2'] > 10)]
    }
    return invalid_vals

def rm_outliers(df, cols):
    outliers_dict = {}
    for col in cols:
        Q1, Q3 = df[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        outliers_dict[col] = outliers
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df, outliers_dict

def do_levene_anova(data, cols):
    levene_res, anova_res = {}, {}
    
    for col in cols:
        groups = [data['BMI'][data[col] == level] for level in data[col].unique()]
        levene_res[col] = stats.levene(*groups)
        
        if levene_res[col].pvalue > 0.05:
            anova_res[col] = stats.f_oneway(*groups)
        else:
            anova_res[col] = None
    
    return levene_res, anova_res

def main():
    data = pd.read_excel('data/BMI飲食習慣.xlsx')
    data = data.dropna(subset=['BMI'])

    # Check for invalid values and remove them
    invalid_vals = check_invalid_vals(data)
    for col, vals in invalid_vals.items():
        if not vals.empty:
            data = data.drop(vals.index)

    # Remove outliers
    cols = ['身高', '體重', '食物1', '食物2', '攝取次數', '速食頻率', '便利商店頻率']
    data, outliers_dict = rm_outliers(data, cols)

    data['便利商店頻率'].fillna(data['便利商店頻率'].mean(), inplace=True)

    # Save updated data and outliers to Excel files
    data.to_excel('data/updated_BMI_飲食習慣.xlsx', index=False)

    for col, outliers in outliers_dict.items():
        if not outliers.empty:
            outliers.to_excel(f'data/removed_outliers_{col}.xlsx', index=False)

    # Perform Levene's Test and ANOVA
    factors = ['食物1', '食物2', '攝取次數', '速食頻率', '便利商店頻率']
    levene_res, anova_res = do_levene_anova(data, factors)

    for factor in factors:
        print(factor, ':')
        print(f"Levene's Test -> W = {levene_res[factor].statistic}, p = {levene_res[factor].pvalue}")
        if anova_res[factor]:
            print(f"ANOVA -> F = {anova_res[factor].statistic}, p = {anova_res[factor].pvalue}")
        else:
            print("ANOVA not performed due to unequal variances.")
        print()

if __name__ == "__main__":
    main()