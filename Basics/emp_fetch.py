import numpy as np
import pandas as pd

#create 1 million employees using np
emp=np.arange(0,1000000)

#fired top 10 highest paid employees
highest=pd.DataFrame(emp.reshape(100000,10))
print(highest.tail(1))

#Top 10 lowest paid employees + 500
lowest= highest.head(1) + 500
print(lowest)
