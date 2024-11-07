import numpy as np

np.random.seed(42)
pup = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

print("Means of puppies is", pup.mean())
print("Standard Deviation of puppies is", pup.std())
print("Variance of puppies is", pup.var())

meansofpup = []
for i in range(10000):
    sample = np.random.choice(pup, (5), replace=True)
    meansofpup.append(sample.mean())
meansofpup = np.array(meansofpup)
print("Showing the stats of puppies data with sample size as 5")
print("Means of puppies is", meansofpup.mean())
print("Standard Deviation of puppies is", meansofpup.std())
print("Variance of puppies is", meansofpup.var())

meansofpup = []
for i in range(10000):
    sample = np.random.choice(pup, (20), replace=True)
    meansofpup.append(sample.mean())
meansofpup = np.array(meansofpup)
print("Showing the stats of puppies data with sample size as 20")
print("Means of puppies is", meansofpup.mean())
print("Standard Deviation of puppies is", meansofpup.std())
print("Variance of puppies is", meansofpup.var())
