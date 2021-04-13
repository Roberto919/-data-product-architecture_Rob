import bulwark.decorators as dc
import pandas as pd

@dc.IsShape((-1, 3))
@dc.IsMonotonic(strict=True)
@dc.HasNoNans()
def compute(df):
    return df

df = pd.DataFrame({'a': [1,2,3,4,5], 'b': [None,0,4,1,0]})
compute(df)