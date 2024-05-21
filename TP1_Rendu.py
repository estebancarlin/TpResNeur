# ## 7. To Do : Mise au point d'un classifieur profond sur les données Mnist (Passer en première lecture)

# https://www.kaggle.com/c/digit-recognizer

# Vous devez :

# - Vous enregistrer sur Kaggle
# - Récupérer les données de la compétition digit-recognizer
# - Soumettre des prédictions sur les données de test.
# - Me fournir par mail d'ici la prochaine séance votre login Kaggle et la performance que vous avez obtenue.

# Pour cela vous pourrez suivre, notamment, les pistes évoquées ci-dessous (non exclusives).

# Dans tous les cas vous ferez attention à avoir une bonne estimation de la performance en généralisation avant de soumettre un RUN sur Kaggle.
# ### Piste 1 : Accroître la quantité de données et leur variabilité  

# - En bruitant les données (bruit à définir)
# - En rajoutant les images miroirs
# - En utilisant les pistes décrites ici  http://leon.bottou.org/projects/infimnist
# Vous pourrez utiliser [ImageDataGenerator](https://keras.io/preprocessing/image/) de Keras.
# ### Piste 2 : Exploiter la technique du dropout

# En vous inspirant de résultats et d'indications publiés dans
# https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf

# La couche de Dropout de Keras est définie [ici](https://keras.io/layers/core/).

