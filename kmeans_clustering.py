
from sklearn.cluster import KMeans

def perform_kmeans(data, n_clusters=5):
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    
    # Return cluster labels and centroids
    return kmeans.labels_, kmeans.cluster_centers_
