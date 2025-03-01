
import data_handler
import kmeans_clustering
import visualizer

def main():
    # Load and preprocess data
    data = data_handler.load_and_preprocess_data()

    # Perform K-means clustering
    kmeans_results = kmeans_clustering.perform_kmeans(data)

    # Visualize results
    visualizer.visualize_segments(kmeans_results)

if __name__ == "__main__":
    main()
