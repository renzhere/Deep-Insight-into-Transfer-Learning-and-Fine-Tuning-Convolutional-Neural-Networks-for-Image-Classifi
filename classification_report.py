#Predicting the class and classification report and confusion matrix

from sklearn.metrics import classification_report, confusion_matrix
Y_pred1 = model1.predict(x_test, verbose=2)
y_pred1 = np.argmax(Y_pred1, axis=1)
 
for ix in range(10):
    print(ix, confusion_matrix(np.argmax(y_test,axis=1),y_pred)[ix].sum())
cm = confusion_matrix(np.argmax(y_test,axis=1),y_pred)
print(cm)
 
# Visualizing of confusion matrix
import seaborn as sn
import pandas  as pd
 
df_cm = pd.DataFrame(cm, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()

print(classification_report(y_test, y_pred1))

#################################################################

from sklearn.metrics import classification_report, confusion_matrix
Y_pred2 = model1.predict(x_test, verbose=2)
y_pred2 = np.argmax(Y_pred2, axis=1)
 
for ix in range(10):
    print(ix, confusion_matrix(np.argmax(y_test,axis=1),y_pred2)[ix].sum())
cm2 = confusion_matrix(np.argmax(y_test,axis=1),y_pred2)
print(cm2)
 
# Visualizing of confusion matrix
import seaborn as sn
import pandas  as pd
 
df_cm = pd.DataFrame(cm2, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()

print(classification_report(y_test, y_pred2))

###############################################

#Predicting the class and classification report for Model3 and confusion matrix

from sklearn.metrics import classification_report, confusion_matrix
Y_pred3 = model1.predict(x_test, verbose=2)
y_pred3 = np.argmax(Y_pred3, axis=1)
 
for ix in range(10):
    print(ix, confusion_matrix(np.argmax(y_test,axis=1),y_pred3)[ix].sum())
cm3 = confusion_matrix(np.argmax(y_test,axis=1),y_pred3)
print(cm3)
 
# Visualizing of confusion matrix
import seaborn as sn
import pandas  as pd
 
df_cm = pd.DataFrame(cm3, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()

print(classification_report(y_test, y_pred3))

########################################################

#Predicting the class and classification report for Model4 and confusion matrix

Y_pred4 = model1.predict(x_test, verbose=2)
y_pred4 = np.argmax(Y_pred4, axis=1)
 
for ix in range(10):
    print(ix, confusion_matrix(np.argmax(y_test,axis=1),y_pred4)[ix].sum())
cm4 = confusion_matrix(np.argmax(y_test,axis=1),y_pred4)
print(cm4)
 
# Visualizing of confusion matrix
import seaborn as sn
import pandas  as pd
 
df_cm = pd.DataFrame(cm4, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()

print(classification_report(y_test, y_pred4))

#############################################################

Y_pred5 = model1.predict(x_test, verbose=2)
y_pred5 = np.argmax(Y_pred5, axis=1)
 
for ix in range(10):
    print(ix, confusion_matrix(np.argmax(y_test,axis=1),y_pred5)[ix].sum())
cm5 = confusion_matrix(np.argmax(y_test,axis=1),y_pred5)
print(cm5)
 
# Visualizing of confusion matrix
import seaborn as sn
import pandas  as pd
 
df_cm = pd.DataFrame(cm5, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()

print(classification_report(y_test, y_pred5))

##################################################################


Y_pred6 = model1.predict(x_test, verbose=2)
y_pred6 = np.argmax(Y_pred6, axis=1)
 
for ix in range(10):
    print(ix, confusion_matrix(np.argmax(y_test,axis=1),y_pred6)[ix].sum())
cm6 = confusion_matrix(np.argmax(y_test,axis=1),y_pred6)
print(cm6)
 
# Visualizing of confusion matrix
import seaborn as sn
import pandas  as pd
 
df_cm = pd.DataFrame(cm6, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()

print(classification_report(y_test, y_pred6))
