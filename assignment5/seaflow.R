library(caret)
library(rpart)
library(ggplot2)
library(randomForest)
library(e1071)

setwd("C:/Home/Courses/Data Science at Scale/datasci_course_materials/assignment5")

# task 1: read file and summary

seaflow <- read.csv("seaflow_21min.csv")
summary(seaflow)

# task 2: split data

train_index <- createDataPartition(seaflow$pop, p=.5, times=1, list=F)
train_data <- seaflow[train_index, ]
test_data <- seaflow[-train_index, ]
summary(train_data)

# task 3: plot pe against chl_small and color by pop

ggplot(train_data, aes(x=chl_small, y=pe, color=pop)) + geom_point(size=5)

# task 4: train a decision tree

obj_func <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
dt_model <- rpart(obj_func, method="class", data=train_data)
print('DT model')
print(dt_model)

# task 5: evaluate the decision tree

dt_results <- predict(dt_model, test_data, type="class")
print('DT accuracy')
print(sum(dt_results == test_data$pop) / nrow(test_data))

# task 6: build and evaluate a random forest

rf_model <- randomForest(obj_func, data=train_data)
rf_results <- predict(rf_model, test_data, type="class")
print('RF accuracy')
print(sum(rf_results == test_data$pop) / nrow(test_data))
print('RF model importance')
print(importance(rf_model))

# task 7: train and evaluate a SVM

svm_model <- svm(obj_func, data=train_data)
svm_results <- predict(svm_model, test_data, type="class")
svm_accuracy <- sum(svm_results == test_data$pop) / nrow(test_data)
print('SVM accuracy')
print(svm_accuracy)

# task 8: generate confusion matrices

table(pred = dt_results, true = test_data$pop)
table(pred = rf_results, true = test_data$pop)
table(pred = svm_results, true = test_data$pop)

# task 9: sanity check

plot(seaflow$fsc_big)
ggplot(train_data, aes(x=chl_big, y=time, color=pop)) + geom_point(size=5)
fixed_data = seaflow[seaflow$file_id != '208', ]
fixed_train_index <- createDataPartition(seaflow$pop, p=.5, times=1, list=F)
fixed_train_data <- fixed_data[fixed_train_index, ]
fixed_test_data <- fixed_data[-fixed_train_index, ]
fixed_svm_model <- svm(obj_func, data=fixed_train_data)
fixed_svm_results <- predict(fixed_svm_model, fixed_test_data, type="class")
fixed_svm_accuracy <- sum(fixed_svm_results == fixed_test_data$pop) / nrow(fixed_test_data)
print('SVM accuracy on fixed data')
print(fixed_svm_accuracy)
print('accuracy improvment')
print(fixed_svm_accuracy - svm_accuracy)
