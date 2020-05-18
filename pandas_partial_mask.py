import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(4, size=(10, 3)),
                   columns=list('abc'))
# partial mask
mask = df.iloc[:, [0, 2]] > 1
# set values
df[mask] = -1
# check result
res0 = (df >= 0).sum()

# partial mask with same shape, but different columns
mask['d'] = mask['c']
df[mask] = -1
res1 = (df >= 0).sum()
assert (res1 == res0).all()

# partial mask with greater shape
mask['f'] = mask['c']
mask.loc[12] = mask.loc[1]
df[mask] = -1
res1 = (df >= 0).sum()
assert (res1 == res0).all()
