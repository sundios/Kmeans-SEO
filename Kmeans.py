#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:08:29 2019

@author: kburch1
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#Opening xlsx
df = pd.read_excel (r'www.uselessthingstobuy.com.xlsx')


#### CTR Vs Title Length ####
X2 = pd.DataFrame(df, columns = ['Title Length','CTR'])

#Finding the right number of clusters for Kmeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X2)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Kmeans
kmeans = KMeans(n_clusters=3).fit(X2)
centroids = kmeans.cluster_centers_
print(centroids)

#Plotting

plt.title('Title Lenght vs CTR for UberEats London')
plt.scatter(df['Title Length'], df['CTR'], c= kmeans.labels_.astype(float), s=50, alpha=0.5,label = 'URLs')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50,label='Centroid')
plt.xlabel('Title Length')
plt.ylabel('CTR')
plt.legend()


#### CTR VS Rankings ####

X3 = pd.DataFrame(df, columns = ['Position','CTR'])

#Removing Nan Values
X3 = np.nan_to_num(X3)


#Finding the right number of clusters for Kmeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X3)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Kmeans
kmeans = KMeans(n_clusters=3).fit(X3)
centroids = kmeans.cluster_centers_
print(centroids)

#Plotting

plt.title('Rank vs CTR for UberEats London')
plt.scatter(df['Position'], df['CTR'], c= kmeans.labels_.astype(float), s=50, alpha=0.5,label = 'URLs')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50,label='Centroid')
plt.ylabel('CTR')
plt.xlabel('Rank')
plt.legend()


#### CTR VS Impressions ####

X4 = pd.DataFrame(df, columns = ['Impressions','CTR'])



#Finding the right number of clusters for Kmeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X4)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Kmeans
kmeans = KMeans(n_clusters=3).fit(X4)
centroids = kmeans.cluster_centers_
print(centroids)

#Plotting

plt.title('Impressions vs CTR for UberEats London')
plt.scatter(df['Impressions'], df['CTR'], c= kmeans.labels_.astype(float), s=50, alpha=0.5,label = 'URLs')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50,label='Centroid')
plt.ylabel('CTR')
plt.xlabel('Impressions')
plt.legend()


