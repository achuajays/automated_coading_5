
import matplotlib.pyplot as plt

def visualize_segments(kmeans_results):
    labels, centroids = kmeans_results
    
    # Example colors for different clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    
    for i in range(len(centroids)):
        # Scatter plot for each cluster
        plt.scatter(data_handler.load_and_preprocess_data()[:, 0][labels == i], 
                    data_handler.load_and_preprocess_data()[:, 1][labels == i], 
                    s=100, 
                    c=colors[i], 
                    label=f'Cluster {i+1}')
    
    # Plot centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='black', marker='X', label='Centroids')
    
    plt.title('Customer Segments')
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.legend()
    plt.grid(True)
    plt.show()
