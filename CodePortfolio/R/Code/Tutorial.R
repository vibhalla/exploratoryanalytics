# Tutorial Week 12
#compiled by Joane Luciano I-590 Spring 2018
###
# Setup and exploration

auto <- read.table("data/auto-mpg.data",
                   col.names = c("MPG","cylinders","displacement","horsepower",
                                  "weight","acceleration","year","origin","name"))
str(auto)
summary(auto)
auto$horsepower <- as.integer(auto$horsepower)
hist(auto$horsepower)
auto$fuelEfficient <- as.logical(auto$MPG>30)
table(auto$fuelEfficient)
pie(table(auto$fuelEfficient), main="Fuel Efficient or Not")

###
# Split into train/test sets.
smp_size <- floor(.8 * nrow(auto))
set.seed(seed=2018)
ti <- sample(seq_len(nrow(auto)), size=smp_size) 
train.auto <- auto[ti,]
test.auto <- auto[-ti,]
str(train.auto)
str(test.auto)

###
# Linear Regression
mylm <- lm(MPG~weight+year+horsepower, train.auto)
res <- predict.lm(mylm, test.auto)
summary(abs(res - test.auto$MPG))

###
# K-Means Clustering
mykm <- kmeans(auto[c("weight","year")], 2)
plot(auto[c("weight","year")], col=mykm$cluster, pch=as.integer(auto$fuelEfficient))
mykm <- data.frame(auto, mykm$cluster)
with(mykm, table(fuelEfficient, mykm.cluster))

###
# Classification Tree
library("rpart")
ctree <- rpart(fuelEfficient ~ cylinders+horsepower+weight+acceleration+year,
              data = train.auto,
              method = 'class')
ctree.test <- data.frame(test.auto,predict(ctree,test.auto))
summary(ctree.test[which(ctree.test$fuelEfficient==T), c(10,11,12)])
summary(ctree.test[which(ctree.test$fuelEfficient==F), c(10,11,12)])

###
# Regression Tree
rtree <- rpart(MPG ~ cylinders+horsepower+weight+acceleration+year,
              data = train.auto,
              method = 'anova')
rtree.test <- data.frame(test.auto, predict(rtree,test.auto))
summary(abs(rtree.test[1]-rtree.test[11]))
cor(rtree.test[1], rtree.test[11], method = "pearson")

