data <- read.csv("/home/abhi/Downloads/WholesaleCustomerData.csv")

data$Region <- factor(data$Region)

one.way <- aov(Grocery ~ Region, data = data)

summary(one.way)

TukeyHSD(one.way)
