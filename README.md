# ClusterPathways
# Language: Python
# Input: TXT
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6
# Dependency: Pathway-Tools Database

PluMA plugin to take a cluster of taxa and search reactions from the PathwayTools
database (Karp et al, 2015) for taxa in the cluster.  It returns pathways in TXT format.

The input is a parameters TXT file of tab-delimited keyword-value pairs:
noafile: Cluster of taxa (NOA)
pathways: TXT file of pathways from PathwayTools

Note: The example folder only contains the cluster NOA file and the parameters TXT file,
but not the pathways file as this contains information from the PathwayTools database.

However if you have PathwayTools installed, the "PathwayTools" plugin
(http://github.com/PathwayTools) will produce this TXT file for the pathways.
