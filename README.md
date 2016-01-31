# hackCambridge

# A Small Research Hack: Clustering and Visualisation of Protein Interaction Networks (and other cool networks)

Protein interaction networks are an incredible bed for hypothesis generation for potential studies into interactions of specific proteins whose interactions are unknown by looking at the way they are clustered, as this can hint towards protein complexes or functional interactions. The challenging part of this hack was implementing clustering methods that are not typically taught at the undergraduate level, topographical/graphical clustering methods (unlike the usual k-means which has a notion of distance), so I am essentially clustering binary conections. This small reseach hack implements five modern topographical clustering methods applied onto a protein interaction network extracted from high throughput studies performed on Sacchoromyces Cerevisiae.

Moreover the clustering algorithms can be applied to many more different datasets such as interaction graphs in transportation, literature, social networks, etc. 