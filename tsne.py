import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Tsne Plot
def tsneplot(embeddings,labels,fig_path):
    print("********************* tSNE Plot*********************")
    X = TSNE(n_components=2,perplexity=100,n_iter=1000).fit_transform(embeddings)
    colors = ['#FF0000', '#06D506', '#0931F7', '#00FFFF', '#FFE500', '#F700FF', '#9300FF', '#FFD700','#10DADE']   # Red , Green, Blue
    for c in range(len(colors)):
        points = []
        for j in range(len(labels)):
            if (labels[j] == c):
                points.append(list(X[j]))
        x = []
        y = []
        for z in points:
            x.append(z[0])
            y.append(z[1])
        plt.plot(x, y, 'ro', c=colors[c], markersize=20, marker='.')
    plt.axis('off')
    plt.savefig(fig_path)
    plt.close()