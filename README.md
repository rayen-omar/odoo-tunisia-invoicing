<div align="center">
  <img src="static/description/icon.png" alt="FODEC & Timbre Fiscal Icon" width="150"/>
  <h1>FODEC & Timbre Fiscal (l10n_tn_invoice)</h1>
  <p><em>Module Odoo 19 de conformité à la facturation tunisienne</em></p>
</div>

---

## 📌 Description

Ce module ajoute des fonctionnalités essentielles pour assurer la conformité de vos factures avec la réglementation fiscale tunisienne. Il gère automatiquement et manuellement l'intégration du **FODEC** (Fonds de Développement de la Compétitivité) et du **Timbre Fiscal**.

## ✨ Fonctionnalités Principales

*   **Gestion du FODEC (1%)** : Application d'une taxe parafiscale de 1% sur certains produits et calcul adapté sur les factures clients.
*   **Droit de Timbre Fiscal (1 DT)** : Ajout automatique du montant forfaitaire du timbre fiscal (actuellement 1.00 DT) aux factures ne comportant pas l'exonération du droit de timbre.
*   **Intégration Comptable** : Mapping correct avec les articles comptables associés (`product_fodec` et `product_timbre_fiscal`).
*   **Impression** : Édition des factures avec les montants FODEC et Timbre Fiscal bien distincts selon le modèle tunisien.

## 🚀 Installation

1.  Placez le dossier `l10n_tn_invoice` dans votre répertoire d'addons personnalisés (custom addons).
2.  Dans Odoo, assurez-vous d'avoir activé le **Mode Développeur**.
3.  Allez dans **Applications** -> **Mise à jour de la liste des applications**.
4.  Recherchez `FODEC & Timbre Fiscal` ou `l10n_tn_invoice`.
5.  Cliquez sur **Activer**.

## ⚙️ Configuration & Utilisation

Une fois installé :
*   Les articles de service **"FODEC 1%"** et **"Timbre Fiscal"** seront créés dans votre base de données (si non existants).
*   L'application du FODEC se fait sur la base des règles de taxes liées aux articles concernés.
*   Le Timbre Fiscal (non soumis à la TVA) s'ajoute selon le paramétrage des factures.
*   Pensez à configurer vos **comptes de revenus / dépenses** pour ces articles en fonction de votre plan comptable tunisien.

## 🛠️ Dépendances

*   `account` (Module Facturation / Comptabilité standard d'Odoo)

## 📄 Licence et Auteur

*   **Auteur :** Expert Odoo Developer
*   **Version :** 19.0.1.0.0
*   **Licence :** LGPL-3
