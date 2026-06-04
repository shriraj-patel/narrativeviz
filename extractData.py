import pandas as pd

df = pd.read_csv('time_series_covid19_deaths_US.csv')

date_cols = df.columns[12:]
national = df[date_cols].sum()

result = pd.DataFrame({
    'date': national.index,
    'deaths': national.values
})

result['date'] = pd.to_datetime(result['date'])

result['daily_deaths'] = result['deaths'].diff().fillna(0).astype(int)
result['daily_deaths'] = result['daily_deaths'].clip(lower=0)

result.to_csv('national_deaths.csv', index=False)