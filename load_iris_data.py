from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris(as_frame=True)

# Convert to DataFrame
print(iris.keys())
df_iris = iris['frame']

# Save to csv
df_iris.to_csv('iris_dataset.csv')
