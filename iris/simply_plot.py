import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
# If you don't have the dataset, you can download it from UCI or use seaborn's built-in dataset
# iris_data = pd.read_csv('path/to/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
iris_data = sns.load_dataset('iris')

# Create a pairplot
sns.pairplot(iris_data, hue='species', markers=["o", "s", "D"])

# Show the plot
plt.show()