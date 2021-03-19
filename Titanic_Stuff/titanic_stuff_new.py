import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


train_data = pd.read_csv('/Users/James/Desktop/lunchtime_spp_python/Titanic_Machine_Learning/titanic/train.csv')
test_data = pd.read_csv('/Users/James/Desktop/lunchtime_spp_python/Titanic_Machine_Learning/titanic/test.csv')
gender_data = pd.read_csv('/Users/James/Desktop/lunchtime_spp_python/Titanic_Machine_Learning/titanic/gender_submission.csv')

#Do e.g. train_data.head() to see data structure
#Do train_data.columns to see columns
#To access individual arrays do e.g.: passenger_ids = train_data['PassengerId']
#https://github.com/Lancaster-Space-and-Planetary-Physics/Python-Projects/tree/master/Titanic%20-%20Machine%20Learning%20from%20Disaster



#We need to choose the best type of Machine learning algorithm to work out who survives and who dies
#The model needs training on the 'train' dataset, then given the 'test' dataset needs to predict the outcomes


#----------------


#Let's examine some basic trends between the data.

#For those who survived, plot number of survivors (Male/Female) as bars

survived = np.array(train_data['Survived'])

survivors = np.where(survived == 1) #this returns the indices where someone survived

non_survivors = np.where(survived == 0) #this returns the indices where someone died

sexes = np.array(train_data['Sex'])

males = np.where(sexes == 'male')

females = np.where(sexes == 'female')


sexes_of_survivors = sexes[survivors]

male_survivors = np.where(sexes_of_survivors == 'male')

female_survivors = np.where(sexes_of_survivors == 'female')

percentage_of_male_survivors = str(round(len(male_survivors[0])/len(males[0])*100.,1))+'%'
#As a fraction of the total number of males

percentage_of_female_survivors = str(round(len(female_survivors[0])/len(females[0])*100.,1))+'%'
#As a fraction of the total number of females

ax = plt.subplot(111)

ax.bar('Male', len(males[0]), align='center',alpha=0.2)
ax.bar('Male', len(male_survivors[0]), align='center')
ax.bar('Female', len(females[0]), align='center',alpha=0.2)
ax.bar('Female', len(female_survivors[0]), align='center')
ax.set_xlabel('Sex')
ax.set_ylabel('Number')

ax.text('Male',50,'{}'.format(percentage_of_male_survivors),fontsize=16)
ax.text('Female',50,'{}'.format(percentage_of_female_survivors),fontsize=16)




#----------------

#For those who survived and died, plot the relative numbers in the different classes


classes = np.array(train_data['Pclass'])



classes_of_survivors = classes[survivors]
classes_of_non_survivors = classes[non_survivors]

first_class_survivors = np.where(classes_of_survivors == 1)
second_class_survivors = np.where(classes_of_survivors == 2)
third_class_survivors = np.where(classes_of_survivors == 3)

first_class_non_survivors = np.where(classes_of_non_survivors == 1)
second_class_non_survivors = np.where(classes_of_non_survivors == 2)
third_class_non_survivors = np.where(classes_of_non_survivors == 3)


labels = ['Survived','Died']
x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars (as a fraction of distance to next bar)

# So each 'group' (Survived/Died) has 3 bars (for 1st, 2nd and 3rd class)


# Set position of bar on X axis
r1 = np.arange(len(labels))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

fig, ax = plt.subplots()

#We need to group the survivors/non-survivors into a single array for plotting under each 'Class'
first_class_survive_die = [len(first_class_survivors[0]),len(first_class_non_survivors[0])]
second_class_survive_die = [len(second_class_survivors[0]),len(second_class_non_survivors[0])]
third_class_survive_die = [len(third_class_survivors[0]),len(third_class_non_survivors[0])]


rects1 = ax.bar(r1, first_class_survive_die, width, label='1st')
rects2 = ax.bar(r2, second_class_survive_die, width, label='2nd')
rects3 = ax.bar(r3, third_class_survive_die, width, label='3rd')



ax.set_ylabel('Number')
ax.set_title('Number of people who survived or died by class')
ax.set_xticks(x+width) #this makes sure the 'Survived' or 'Died' labels are aligned with the centre bar

ax.set_xticklabels(labels)
ax.legend()



fig.tight_layout()
plt.show()

