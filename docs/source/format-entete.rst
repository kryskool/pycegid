.. _page_5_60:

Entête
======

:version: Version 7 du 04-08-2005 - Page 5 / 60


Descriptif
----------

+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| Type      |                                                                            |                  | Obligatoire |     |
+===========+============================================================================+==================+=============+=====+
| a3        | Zone fixe                                                                  | FIXE             |     Oui     |  1  |
|           | \*\*\*                                                                     |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a2        | Produit générant le fichier                                                | IDENTIFIANT      |     Oui     |  4  |
|           | S1 ; S3 ; S5 ; S7 ; SI;QU                                                  |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a3        | Origine du fichier                                                         | ORIGINE FICHIER  |     Oui     |  6  |
|           | CLI pour PME ; EXP pour cabinet d expertise comptable                      |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a3        | Contenu du fichier                                                         | TYPE FICHIER     |     Oui     |  9  |
|           | JRL=journal ; DOS=dossier complet ; BAL=balance ;                          |                  |             |     |
|           | SYN=Synchronisation S1                                                     |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a3        | Format du fichier                                                          | FORMAT           |     Oui     |  12 |
|           | STD=standard ; ETE= tendu                                                  |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a3        | Code de l exercice qui doit tre cl turer chez le client.                   | CODE EXO CLOS    |    Non      |  15 |
|           | Information n cessaire dans le cadre d une synchronisation S1              |                  |             |     |
|           | Si aucune information, la zone est blanc                                   |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| d8        | Date de la bascule Euro à faire chez le client sous la forme JJMMAAAA      | DATE BASCULE     |    Non      |  18 |
|           | Information nécessaire dans le cadre d une synchronisation S1              |                  |             |     |
|           | Pour ne rien faire, mettre 01011900                                        |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| d8        | Nouvelle date d'arr t p riodique, sous la forme JJMMAAAA . Pour ne         | DATE ARRETE      |    Non      |  26 |
|           | rien faire, mettre 01011900                                                | PERIODIQUE       |             |     |
|           | Information n cessaire dans le cadre d une synchronisation S1              |                  |             |     |
|           | Pour ne rien faire, mettre 01011900                                        |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| n3        | Version de fichier                                                         | VERSION          |     Oui     |  34 |
|           | Version 007                                                                |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a5        | numéro du dossier au cabinet                                               | N DOSSIER CAB    |     Oui     |  37 |
|           | Information n cessaire dans le cadre d une synchronisation S1              |                  |             |     |
|           | Si aucune information, la zone est blanc                                   |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| d12       | Date et heure de génération de fichier sous la forme JJMMAAAAHHMM          | DATE/HEURE       |    Non      |  42 |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a35       | Nom de l'utilisateur qui a généré le fichier                               | UTILISATEUR      |    Non      |  54 |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a35       | Raison sociale du cabinet                                                  | RAISON SOCIALE   |    Non      |  89 |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a4        | Indicateur de Reprise                                                      | Reprise          |    Non      | 124 |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a6        | numéro dossier                                                             | N Dossier        |    Non      | 128 |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| a3        | Informations d'échanges Fréquence                                          |                  |    Non      | 134 |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| d8        | Date début du premier exercice en ligne de purge des écritures, sous la    | SO_CPDATEREFPUR  |    Non      | 137 |
|           | forme JJMMAAAA .                                                           | GE               |             |     |
|           | Information nécessaire dans le cadre d une synchronisation Sx              |                  |             |     |
|           | Pour ne rien faire, mettre 01011900                                        |                  |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+
| n3        | Sous Version de fichier                                                    | SOUSVERSION      |     Oui     | 146 |
|           | Version 001                                                                                   |             |     |
+-----------+----------------------------------------------------------------------------+------------------+-------------+-----+

.. warning::

    Si TYPEFICHIER est la valeur **BAL** , il est impératif que FORMAT soit égal à STD.





