# Competitor Analysis Application
# Description
L'application Competitor Analysis a été développée dans le cadre d'un projet visant à comparer les prix de l'entreprise Blueline à ceux de Jumia. Nous avons collecté des données de Jumia dans quatre catégories spécifiques (hygiène-santé, électronique, ordinateur-accessoire, téléphone-tablette) et les avons chargées dans la base de données de l'application. Maintenant, l'application permet de rechercher des produits similaires de Blueline en entrant le nom d'un produit spécifique.

# Méthode de Collecte
Les données ont été collectées en suivant les étapes suivantes :

Sélection des Catégories : Choix des catégories spécifiques à partir desquelles les données de prix seront collectées (hygiène-santé, électronique, ordinateur-accessoire, téléphone-tablette).

Beautiful Soup : Utilisation de la bibliothèque Beautiful Soup pour extraire les informations de prix des pages web de Jumia de manière structurée.

Stockage des Données : Les données collectées ont été stockées dans la base de données de l'application pour permettre une analyse ultérieure.

# Modèle Utilisé pour la Recherche d'Images Similaires
L'application utilise le modèle CLIP-ViT-B-32-multilingual-v1 pour la recherche d'images similaires. Ce modèle permet de prendre du texte en entrée et de renvoyer une image correspondante, facilitant ainsi la recherche de produits similaires entre Blueline et Jumia.

# Caractéristiques du Modèle
Nom du Modèle : CLIP-ViT-B-32-multilingual-v1

Fonctionnalité : Recherche d'images basée sur du texte et d'image.

Utilisation : L'utilisateur peut entrer le nom d'un produit Blueline, et le modèle renverra une image correspondante provenant de Jumia

L'intégration du modèle dans l'application permet une expérience utilisateur améliorée en fournissant une visualisation rapide des produits similaires entre les deux entreprises.

# Fonctionnalités

Chargement des Données : Les données collectées sont stockées dans la base de données de l'application pour une analyse ultérieure.

Comparaison de Prix : Les prix des produits collectés sont comparés à ceux de Blueline, permettant une analyse détaillée des écarts de prix.

Recherche de Produits Similaires : L'utilisateur peut entrer le nom d'un produit Blueline, et l'application renverra les produits similaires de Jumia.

Interface Conviviale : L'interface utilisateur est conviviale, offrant une expérience utilisateur agréable lors de l'exploration des résultats de l'analyse.
