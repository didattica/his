import pandas as pd
import numpy as np
import random
num = 10000
df = pd.DataFrame()
df['age'] = np.random.choice(70, num) + 18
df['sex'] = [random.choice(['male','female']) for i in df['age']]


def get_sport_h(i):
  if df['age'].iloc[i] < 30:
    return np.random.choice(15)
  if df['age'].iloc[i] < 40:
    return np.random.choice(12)
  if df['age'].iloc[i] < 50:
    return np.random.choice(8)
  if df['age'].iloc[i] < 60:
    return np.random.choice(6)
  return np.random.choice(4)

def get_height(i):
  mu = 160
  if df['sex'].iloc[i] == 'male':
    mu = 175
  mu = mu - df['age'].iloc[i] * .1 - df['sport_h'].iloc[i] * 0.01
  return round(np.random.normal(mu, 10), 2)

def get_weight(i):
  mu = 61
  if df['sex'].iloc[i] == 'male':
    mu = 72
    mu = mu + df['age'].iloc[i] * .3	
  return round(np.random.normal(mu, 5), 2)

def get_sex_n(i):
  if df['sex'].iloc[i] == 'male':
    return 1
  return 0
  
df['sport_h'] = [get_sport_h(i) for i in df.index]
df['height'] = [get_height(i) for i in df.index]
df['weight'] = [get_weight(i) for i in df.index]
df['sex_n'] = [get_sex_n(i) for i in df.index]

sns.heatmap(df.corr(), annot=True, fmt='.2f')
plt.show()
df.to_csv('/tmp/open_health_data.csv')