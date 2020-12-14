# LB_2020.11.01
This repository contains Class_Notes & Python_Tryouts

1. Class_Notes : These are snippets from my Python Introduction Classes.
2. Python_Tryouts : These are full code implementation.
	01_Polygon_Define_Rotate_Plot: Defines a Regular Polygon & Rotates it by a specified angle.
	02_Temperature Converter: Accepts user input temperature scale and converts it into the other 3 scales.
	03_Transient_Forces: This module computes the unbalance, oscillating, tangential and centrifugal forces due to rotational acceleration of an initial unabalance and orientation


pd.options.display.max_columns = None

df = pd.read_csv(f"{PATH}{FNAME}")
ds = df.describe() # Descriptive Statistics
cs = df.corr(method = 'kendall') # Correlation Coefficients: Method pearson, kendall

print(f"Shape & Size of Dataframe: {df.shape} & {df.size}\n")
print(ds.to_string(FOUT), sep ='\n')
print(cs.to_string(FOUT), sep = '\n')
FOUT.close()

mask = np.zeros(cs.shape, dtype=bool)
mask[np.tril_indices(len(mask))] = False
plt.subplots(figsize=(20,15))
sns.heatmap(cs, annot = True, vmin = -1, vmax = 1, center = 0, cmap = 'coolwarm', square = True, mask = mask)
