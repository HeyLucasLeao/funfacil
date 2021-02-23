from sklearn import metrics

def clustering_algorithm(n_clusters, dataset):
    SEED = 20
    kmeans = KMeans(n_clusters=n_clusters,
                n_init=10,
                random_state=SEED,
                max_iter=300)
    labels = kmeans.fit_predict(dataset)
    s = metrics.silhouette_score(dataset, labels, metric='euclidean')
    db = metrics.davies_bouldin_score(dataset, labels)
    calinski = metrics.calinski_harabasz_score(dataset, labels)
    return [s, db, calinski]

def grid_search_n_clustering(dataset, start=2, end=30):
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

    return f"""Silhouette: N.º de Clusters: {r1[0]} -------- {r1[1]}, 
    Davies Bouldin: N.º de Clusters: {r2[0]} -------- {r2[1]}, 
    Calinski Harabrasz: N.º de Clusters: {r3[0]} -------- {r3[1]}"""
