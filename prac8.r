# Load necessary packages
install.packages("ggplot2")
install.packages("cluster")
library(ggplot2)
library(cluster)

# Load the iris dataset (it's already available in R)
df <- iris

# Plot the data using ggplot2
ggplot(df, aes(Petal.Length, Petal.Width)) +
  geom_point(aes(col=Species), size=4)

# Perform k-means clustering
set.seed(101)
irisCluster <- kmeans(df[,1:4], center=3, nstart=20)

# Display cluster centers
irisCluster

# Cross-tabulation between cluster and species
table(irisCluster$cluster, df$Species)

# Plot clusters using clusplot
clusplot(iris, irisCluster$cluster, color=T, shade=T, labels=0, lines=0)

# Calculate total within-cluster sum of squares for different k values
tot.withinss <- vector(mode="numeric", length=10)
for (i in 1:10){
  irisCluster <- kmeans(df[,1:4], center=i, nstart=20)
  tot.withinss[i] <- irisCluster$tot.withinss
}

# Plot the elbow curve
plot(1:10, tot.withinss, type="b", pch=19)
