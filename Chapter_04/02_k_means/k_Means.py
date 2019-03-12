# Unsupervised Learning

# Part A - k-means clustering WITHOUT PCA transformation

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# instantiate kmeans model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=2)

# fit model
model.fit(scaled_features)

# get the cluster centroids
centroids = model.cluster_centers_ 
print(centroids)

# get the inertia
inertia = model.inertia_ 
print('The within-group sum of squares (i.e., inertia) with 2 clusters is {0:0.2f}'.format(inertia))

# get predicted labels
labels = model.labels_
print(labels)

# see how many of each label we have
import pandas as pd
pd.value_counts(labels)

# add label to df_shuffled
df_shuffled['Predicted_Cluster'] = labels
print(df_shuffled.head(5))

###############################################################################

# ensemble of kmeans

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# instantiate an empty dataframe
import pandas as pd
labels_df = pd.DataFrame()

# Build 100 models
from sklearn.cluster import KMeans
for i in range(1, 101):
    # k-means ensemble
    model = KMeans(n_clusters=2)
    # fit model
    model.fit(scaled_features)
    # get predicted labels
    labels = model.labels_
    # put the labels into the empty df
    labels_df['Model_{}_Labels'.format(i)] = labels
print('There are {} rows and {} columns in the labels_df data frame'.format(labels_df.shape[0], labels_df.shape[1]))

# now, we will get predictions across columns
labels_df['row_mode'] = labels_df.mode(axis=1)

# check out the frequency of each cluster
import pandas as pd
pd.value_counts(labels_df['row_mode'])



###############################################################################

# 2. Tuning n_clusters

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# get inertia for every cluster
from sklearn.cluster import KMeans
inertia_list = []
for i in range(10):
    # instantiate pipeline
    model = KMeans(n_clusters=i+1)
    # fit pipeline
    model.fit(scaled_features)
    # get inertia
    inertia = model.inertia_
    # append inertia to inertia_list
    inertia_list.append(inertia)
print(inertia_list)
    
# plot inertia by n_clusters
import matplotlib.pyplot as plt
import numpy as np
x = list(np.arange(1,11))
y = inertia_list
plt.plot(x, y)
plt.title('Inertia by n_clusters')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.show()

# get the inertia values for 3
print('When n_clusters = 3, inertia = {:0.2f}'.format(y[2]))

# now, let's get average inertia
avg_inertia = np.mean(inertia_list)
print('The mean inertia for the k-means analysis is {0:0.2f}'.format(avg_inertia))

###############################################################################

# tuning inertia by n_clusters using an ensemble

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

from sklearn.cluster import KMeans
import numpy as np
# create a list for the average inertia at each n_clusters
mean_inertia_list = []
# loop through n_clusters 1-10
for x in range(10):
    # create a list for each individual inertia value at n_cluster
    inertia_list = []
    for i in range(100):
        # instantiate pipeline
        model = KMeans(n_clusters=x+1)
        # fit pipeline
        model.fit(scaled_features)
        # get inertia
        inertia = model.inertia_
        # append inertia to inertia_list
        inertia_list.append(inertia)
    # get mean of inertia list
    mean_inertia = np.mean(inertia_list)
    # append mean_inertia to mean_inertia_list
    mean_inertia_list.append(mean_inertia)
print(mean_inertia_list)    

# plot inertia by n_clusters
import matplotlib.pyplot as plt
import numpy as np
x = list(np.arange(1,11))
y = mean_inertia_list
plt.plot(x, y)
plt.title('Inertia by n_clusters')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.show()

# get the inertia values for 3
print('When n_clusters = 3, inertia = {:0.2f}'.format(y[2]))

# now, let's get average inertia
avg_inertia = np.mean(mean_inertia_list)
print('The mean inertia for the k-means analysis is {0:0.2f}'.format(avg_inertia))



###############################################################################
# k Means clustering with PCA transformation
###############################################################################

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# instantiate pca model
from sklearn.decomposition import PCA
# build model
model = PCA(n_components=2)

# fit model
model.fit(scaled_features)

# get explained variance ratio
explained_var_ratio = model.explained_variance_ratio_
print(explained_var_ratio)

# get the total explained variance with these 2 components
print('The total percentage of explained variance for the first 2 principal components is {0:0.2f}%'.format(sum(explained_var_ratio)*100))

# transform X into X_pca
df_pca = model.transform(scaled_features)

###############################################################################

# 2. Tuning n_components

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# explore dimensions of data
n_rows = df.shape[0]
n_columns = df.shape[1]
print('There are {} rows and {} columns in the Iris data set'.format(n_rows, n_columns))

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# instantiate pca model
from sklearn.decomposition import PCA
model = PCA()

# fit model
model.fit(scaled_features)

# transform into principle components
df_pca = model.transform(scaled_features)

# get the explained variance ratio for each component
explained_var_ratios = model.explained_variance_ratio_
print(explained_var_ratios)

# get the cumulative sum of explained variance by each component
import numpy as np
cum_sum_explained_var = np.cumsum(explained_var_ratios)
print(cum_sum_explained_var)

# set a threshold for % of variance in the data to preserve
threshold = 95
# programmatically check at which component we reach or surpass the threshold
for i in np.arange(0, len(cum_sum_explained_var)):
    if cum_sum_explained_var[i] >= (threshold/100):
        best_n_components = i+1
        break
    else:
        pass
print('The best n_components is {}'.format(best_n_components))

# plot cumulative xplained variance by n_components
import matplotlib.pyplot as plt
plt.plot([x for x in np.arange(1, len(explained_var_ratios)+1)], cum_sum_explained_var, color='blue', label='Explained Variance')
plt.title('{0} n_components are suggested to preserve {1}% of the variance'.format(best_n_components, threshold))
plt.ylabel('Proportion of Explained Variance')
plt.xlabel('n_components')
plt.xticks(np.arange(1, len(explained_var_ratios)+1))
plt.axhline(y=(threshold/100), color='gray', linestyle='--', label = '{}% Explained Variance'.format(threshold))
plt.legend(loc='best')
plt.show()

# now, we can fit it to the k-means algorithm
from sklearn.decomposition import PCA
model = PCA(n_components=best_n_components) # remember, best_n_components = 2

# fit model
model.fit(scaled_features)

# transform into principal components
df_pca = model.transform(scaled_features)

# fit 100 models for each n_clusters 1-10
from sklearn.cluster import KMeans
import numpy as np
# create a list for the average inertia at each n_clusters
mean_inertia_list_PCA = []
# loop through n_clusters 1-10
for x in range(10):
    # create a list for each individual inertia value at n_cluster
    inertia_list = []
    for i in range(100):
        # instantiate pipeline
        model = KMeans(n_clusters=x+1)
        # fit pipeline
        model.fit(df_pca)
        # get inertia
        inertia = model.inertia_
        # append inertia to inertia_list
        inertia_list.append(inertia)
    # get mean of inertia list
    mean_inertia = np.mean(inertia_list)
    # append mean_inertia to mean_inertia_list
    mean_inertia_list_PCA.append(mean_inertia)
print(mean_inertia_list_PCA)  
    
# plot inertia by n_clusters
import matplotlib.pyplot as plt
import numpy as np
x = list(np.arange(1,len(mean_inertia_list_PCA)+1))
y = mean_inertia_list_PCA
plt.plot(x, y)
plt.title('Inertia by n_clusters')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.show()

# print both lines on the same plot

# plot inertia by n_clusters
import matplotlib.pyplot as plt
import numpy as np
x = list(np.arange(1,len(mean_inertia_list_PCA)+1))
y = mean_inertia_list_PCA
y2 = mean_inertia_list 
plt.plot(x, y, label='PCA')
plt.plot(x, y2, label='No PCA')
plt.title('Inertia by n_clusters')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.legend()
plt.show()









