install.packages("ggplot2")
install.packages("GGally")
library(datasets)
library(ggplots2)
library(GGally)
Iris <- read_csv("")
View(Iris)
ir_data <- Iris
head(ir_data)
str(ir_data)
levels(ir_data$Species)
sum(is.na(ir_data))
ir_data <- ir_data[1:100,]
set.seed(100)
samp <- sample(1:100, 80)
ir_test <- ir_data[samp,]
ir_ctrl <- ir_data[samp,]
ggpairs(ir_test)
y <- ir_test$Species 
x <- ir_test$Sepal.Length
glfit <- flm(y ~ x, family='binomial')
summary(glfit)
new_data <- data.frame(x = ir_ctrl$Sepal.Length)
predicted_val <- predict(glfit, new_data, type="response")
prediction <- data.frame(ir_ctrl$Sepal.Length, ir_ctrl$Species, predicted_val)
prediction
qplot(prediction[,1], round(prediction[,3]), col=prediction[,2], xlab='Sepal Length', ylab='Prediction Using Logistic Reg')
