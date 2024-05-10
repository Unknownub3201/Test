install.packages("readxl")
library(readxl)
LungCap <- read_excel("/home/abhi/Downloads/LungCap.xls")
View(LungCap)
attach(LungCap)
names(LungCap)
class('LungCap(cc)')
class('Age(years)')
class('Height(inches)')
class('Smoke')
class('Gender')
class('Caesarean')

plot('Age(years)', 'LungCap(cc)', main="Scatterplot")
cor('Age(years)', LungCap$'LungCap(cc)')
mod <- lm(LungCap$'LungCap(cc)' ~ 'Age(years)')
summary(mod)
