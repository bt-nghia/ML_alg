import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
X = np.array([1,2,3,8,4])

sns.histplot(data = pd.DataFrame(X))
plt.show()
