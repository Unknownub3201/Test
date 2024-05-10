data_iris <- iris[1:4]
cov_data <- cov(data_iris)
Eigen_data <- eigen(cov_data)
PCA_data <- princomp(data_iris,cor = "False")
Eigen_data$values
PCA_data$sdev^2
PCA_data$loadings[,1:4]
Eigen_data$vectors
summary(PCA_data)
biplot(PCA_data)
screeplot(PCA_data,type = 'lines')
model2 = PCA_data$loadings[,1]
model2_scores <- as.matrix(data_iris)%%model2
library(class)
install.packages("e1071")
library(e1071)
mod1 <- naiveBayes(iris[,1:4],iris[,5])
mod2 <- naiveBayes(model2_scores,iris[,5])
table(predict(mod1,iris[,1:4]),iris[,5])
table(predict(mod2,model2_scores),iris[,5])
biplot(PCA_data, main = "Biplot", scale = 0)
