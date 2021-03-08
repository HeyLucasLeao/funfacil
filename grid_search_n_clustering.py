from sklearn import metrics
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def grid_search_n_clustering(dataset, start=2, end=30):
    
    def clustering_algorithm(n_clusters, dataset, SEED=20):
        SEED = SEED
        kmeans = KMeans(n_clusters=n_clusters,
                    n_init=10,
                    random_state=SEED,
                    max_iter=300)
        labels = kmeans.fit_predict(dataset)
        s = metrics.silhouette_score(dataset, labels, metric='euclidean')
        db = metrics.davies_bouldin_score(dataset, labels)
        calinski = metrics.calinski_harabasz_score(dataset, labels)
        return [s, db, calinski]
    
    result_grid_search = []
    
    for i in range(start, end):
        result_grid_search.append([i, clustering_algorithm(i, dataset)])

    r1 = result_grid_search[0]
    r2 = result_grid_search[0]
    r3 = result_grid_search[0]

    for i in range(len(result_grid_search)):
        if result_grid_search[i][1][0] > r1[1][0]:
            r1 = result_grid_search[i]

        if result_grid_search[i][1][1] < r2[1][1]:
            r2 = result_grid_search[i]

        if result_grid_search[i][1][2] > r3[1][2]:
            r3 = result_grid_search[i]
            
    df = pd.DataFrame(data=(r1[1], r2[1], r3[1]), columns=['Silhouette Score', 'Davies Bouldin', 'Calinski Harabasz'], index=[r1[0], r2[0], r3[0]])
    return df
