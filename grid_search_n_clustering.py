from sklearn import metrics

def clustering_algorithm(n_clusters, dataset):
    kmeans = KMeans(n_clusters=n_clusters,
                n_init=10,
                random_state=SEED,
                max_iter=300)
    labels = kmeans.fit_predict(dataset)
    s = metrics.silhouette_score(dataset, labels, metric='euclidean')
    db = metrics.davies_bouldin_score(dataset, labels)
    calinski = metrics.calinski_harabasz_score(dataset, labels)
    return [s, db, calinski]

def grid_search_n_clustering(dataset):
    result_grid_search = []
    for i in range(2, 30):
        result_grid_search.append([i, clustering_algorithm(i, dataset)])
    result = result_grid_search[0][1]
    for x in result_grid_search:
        if x[1] > result:
            result = x
    return result
