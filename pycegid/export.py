# -*- coding: utf-8 -*-
##############################################################################
#
#    PyCEGID is a library to export datas in TRA format
#    Copyright (C) 2013 SYLEAM (<http://syleam.fr>) Christophe CHAUVET
#
#    This file is a part of PyCEGID
#
#    PyCEGID is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyCEGID is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time


class CegidException(Exception):

    def __init__(self, msg='Empty Message'):
        self.message = msg

    def __str__(self):
        return repr(self.message)

class VersionNotFound(CegidException):
    pass


class HeaderNotFound(CegidException):
    """When no header found in the streamout"""
    pass


class MandatoryException(CegidException):
    """Raise when mandatory data is required"""
    pass


class NotValidValue(CegidException):
    """Indicate check value is not in permit value"""
    pass


class ExportTra(object):
    """
    Generate format for Cegid
    """

    _default_version = '007'
    _default_date = '01011900'
    _current_date = time.strftime('%Y%m%d%H%M')
    _zone_fixe = '***'

    _available_version = ['007']
    _generate_date = ''

    _debug_header = 0

    _content = {
        'header': '',
        'lines': [],
    }

    def __init__(self):
        """
        Instanciate the class, and initialise the amount to Zero
        """
        self._total = 0.0
        self._generate_date = time.strftime('%d%m%Y%H%M')
        self._content = {
            'header': '',
            'lines': [],
        }

    def changeFormat(self, version='007'):
        if version not in self._available_version:
            raise VersionNotFound()
        self._default_version = version

    def setDebug(self, length=100):
        """
        Generate header for Debug
        """
        self._debug_header = length

    def setHeader(self, identifiant='S5', origine='CLI', type_fic='JRL',
                        format_fic='STD', code_ex_clos='', date_bascule=None,
                        date_arrete=None, num_dossier_cab='00001', utilisateur=None,
                        raison_sociale='', reprise='', num_dossier='',
                        frequence='', date_purge=None, sous_version=''):
        if utilisateur is None:
            utilisateur = 'pycegid'

        if date_bascule is None:
            date_bascule = self._default_date

        if date_arrete is None:
            date_arrete = self._default_date

        if date_purge is None:
            date_purge = self._default_date

        self._content['header'] = self._header(identifiant, origine, type_fic,
                                               format_fic, code_ex_clos, date_bascule,
                                               date_arrete, num_dossier_cab, utilisateur,
                                               raison_sociale, reprise, num_dossier,
                                               frequence, date_purge, sous_version)

    def addSAT(self, code='', libelle='', axe='', table1='', table2='',
                     table3='', table4='', table5='', table6='', table7='',
                     table8='', table9='', table10='', abrege='', sens='M'):
        """
        See documentation version 7 page 23/60 which describe "Section Analytique"
        """
        self._content['lines'].append(''.join([
            self._zone_fixe,                   # Prefix (***)
            'SAT',                             # Identifiant
            self._mandatory(code, 17),         # Code
            self._mandatory(libelle, 35),      # Libelle
            self._mandatory(axe, 3),           # Axe
            self._format(table1, 17),          # Table 1
            self._format(table2, 17),          # Table 2
            self._format(table3, 17),          # Table 3
            self._format(table4, 17),          # Table 4
            self._format(table5, 17),          # Table 5
            self._format(table6, 17),          # Table 6
            self._format(table7, 17),          # Table 7
            self._format(table8, 17),          # Table 8
            self._format(table9, 17),          # Table 9
            self._format(table10, 17),         # Table 10
            self._format(abrege, 17),          # Abrege
            self._format(sens, 3),             # Sens
        ]))

    def addCGN(self, code='', libelle='', nature='', lettrable='', pointable='',
                     ventil_axe1='', ventil_axe2='', ventil_axe3='', ventil_axe4='', ventil_axe5='',
                     table1='', table2='', table3='', table4='', table5='',
                     table6='', table7='', table8='', table9='', table10=''):
        """
        See documentation version 7 page 30/60 which describe "Compte General"
        """
        if nature not in ('BQE', 'CAI', 'CHA', 'COC', 'COD', 'COF', 'COS',
                          'DIV', 'EXT', 'IMO', 'PRO', 'TIC', 'TID'):
            raise NotValidValue('"%s" value is not valid for "nature" field' % nature)

        self._content['lines'].append(''.join([
            self._zone_fixe,                   # Prefix (***)
            'CGN',                             # Identifiant
            self._mandatory(code, 17),         # Code
            self._mandatory(libelle, 35),      # Libelle
            self._mandatory(nature, 3),        # Nature
            self._mandatory(lettrable, 1),     # Lettrable
            self._mandatory(pointable, 1),     # Pointable
            self._mandatory(ventil_axe1, 1),   # Ventilable axe 1
            self._mandatory(ventil_axe2, 1),   # Ventilable axe 2
            self._mandatory(ventil_axe3, 1),   # Ventilable axe 3
            self._mandatory(ventil_axe4, 1),   # Ventilable axe 4
            self._mandatory(ventil_axe5, 1),   # Ventilable axe 5
            self._format(table1, 17),          # Table 1
            self._format(table2, 17),          # Table 2
            self._format(table3, 17),          # Table 3
            self._format(table4, 17),          # Table 4
            self._format(table5, 17),          # Table 5
            self._format(table6, 17),          # Table 6
            self._format(table7, 17),          # Table 7
            self._format(table8, 17),          # Table 8
            self._format(table9, 17),          # Table 9
            self._format(table10, 17),         # Table 10
        ]))

    def addCAE(self, code='', libelle='', nature='', lettrable='', collectif='',
                     ean='', table1='', table2='', table3='', table4='', table5='',
                     table6='', table7='', table8='', table9='', table10='',
                     adresse1='', adresse2='', adresse3='', code_postal='', ville='',
                     domiciliation='', etablissement='', guichet='', cle='', pays='',
                     libelle_abrege='', langue='', multidevise='', devise_tiers='-',
                     telephone='', fax='', regime_tva='', mrg='', comment='', nif='',
                     siret='', ape='', prenom='', ctc_service='', ctc_fonction='',
                     ctc_telephone='', ctc_fax='', ctc_telex='', ctc_rva='',
                     ctc_civilite='', ctc_principal='', forme_juridique='', rib_principal='',
                     tva_encaissement='', payeur='', ispayeur='', avoir_rbt='', relance_rgt='',
                     relance_traite='', confidentiel=''):
        """
        See documentation version 7 page 32/60 whick describe "Compte de tiers"
        """
        if nature not in ('AUC', 'AUD', 'CLI', 'DIV', 'FOU', 'SAL'):
            raise NotValidValue('"%s" value is not valid for "nature" field' % nature)

        if ispayeur and ispayeur not in ('X', '-'):
            raise NotValidValue('"%s" value is not valid for "ispayeur" field' % ispayeur)

        self._content['lines'].append(''.join([
            self._zone_fixe,                   # Prefix (***)
            'CAE',                             # Identifiant
            self._mandatory(code, 17),         # Code
            self._mandatory(libelle, 35),      # Libelle
            self._mandatory(nature, 3),        # Nature
            self._mandatory(lettrable, 1),     # Lettrable
            self._mandatory(collectif, 17),    # Collectif
            self._format(ean, 17),             # EAN
            self._format(table1, 17),          # Table 1
            self._format(table2, 17),          # Table 2
            self._format(table3, 17),          # Table 3
            self._format(table4, 17),          # Table 4
            self._format(table5, 17),          # Table 5
            self._format(table6, 17),          # Table 6
            self._format(table7, 17),          # Table 7
            self._format(table8, 17),          # Table 8
            self._format(table9, 17),          # Table 9
            self._format(table10, 17),         # Table 10
            self._mandatory(adresse1, 17),     # Adresse 1
            self._mandatory(adresse2, 17),     # Adresse 2
            self._format(adresse3, 17),        # Adresse 3
            self._format(code_postal, 9),      # Code postal
            self._format(ville, 35),           # Ville
            self._format(domiciliation, 24),   # Domiciliation (TODO: mandatory ?)
            self._format(etablissement, 5),    # Etablissement (TODO: mandatory ?)
            self._format(guichet, 5),          # Guichet (TODO: mandatory ?)
            self._format(cle, 2),              # Cle (TODO: mandatory ?)
            self._format(pays, 3),             # Pays (TODO: Pays ?)
            self._format(libelle_abrege, 17),  # Libelle abrege
            self._format(langue, 3),           # Langue
            self._format(multidevise, 1),      # Multi devise
            self._format(devise_tiers, 3),     # Devise Tiers
            self._format(telephone, 25),       # Telephone
            self._format(fax, 25),             # Fax
            self._format(regime_tva, 3),       # regime TVA (TODO: mandatory ?)
            self._format(mrg, 3),              # Mode de reglement (TODO: mandatory ?)
            self._format(comment, 35),         # Commentaire
            self._format(nif, 17),             # Nif
            self._format(siret, 17),           # Siret
            self._format(ape, 5),              # Ape
            self._format(prenom, 35),          # Prenom
            self._format(ctc_service, 35),     # Contact service
            self._format(ctc_fonction, 35),    # Contact fonction
            self._format(ctc_telephone, 25),   # Contact telephone
            self._format(ctc_fax, 25),         # Contact fax
            self._format(ctc_telex, 25),       # Contact Telex
            self._format(ctc_rva, 50),         # Contact RVA
            self._format(ctc_civilite, 3),     # Contact civilite
            self._format(ctc_principal, 1),    # Contact principal
            self._format(forme_juridique, 3),  # Forme juridique
            self._format(rib_principal, 1),    # RIB principale
            self._format(tva_encaissement, 3), # TVA Encaissement
            self._format(payeur, 17),          # Payeur
            self._format(ispayeur, 1),         # Tiers payeur
            self._format(avoir_rbt, 1),        # Avoir remboursement
            self._format(relance_rgt, 3),      # Relance reglement
            self._format(relance_traite, 3),   # Relance traite
            self._format(confidentiel, 1),     # Confidentiel
        ]))

    def addEcriture(self, journal='', date_mouvement=None, type_piece='', compte='', type_compte='',
                          num_compte='', ref_interne='', libelle='', modepaie='', echeance='',
                          sens='', montant1=0.0, type_ecriture='', numero_piece='', devise='',
                          taux_dev=1, code_montant='', montant2=0.0, montant3=0.0, etablissement='',
                          axe='', numeche=''):
        """Add move"""

        if type_piece not in ('FC', 'AC', 'RC', 'FF', 'AF', 'RF', 'OD', 'OC', 'OF'):
            raise NotValidValue('"%" value is not valid for "type_piece" field' % type_piece)

        if date_mouvement is None:
            date_mouvement = self._generate_date[:8]

        if not echeance:
            echeance = self._default_date

        if type_compte not in ('X', 'A', 'H', '0'):
            raise NotValidValue('"%s" value is not valid for "type de compte" field' % type_compte)

        if type_ecriture not in ('N', 'S', 'U', 'R'):
            raise NotValidValue('"%s" value is not valid for "type_ecriture" field' % type_ecriture)

        if sens not in ('C', 'D'):
            raise NotValidValue('"%s" value is not valid for "sens" field')

        if type_compte == 'A' and not axe:
            raise MandatoryException('When "type_compte" = A, "axe" field is mandatory!')

        self._content['lines'].append(''.join([
            self._mandatory(journal, 3),         # Code Journal
            self._mandatory(date_mouvement, 8),  # Date du mouvement
            self._mandatory(type_piece, 2),      # Type de piece
            self._mandatory(compte, 17),         # Compte general
            self._format(type_piece, 1),         # Type de compte
            self._format(num_compte, 17),        # numero compte ou section ana
            self._format(ref_interne, 35),       # Reference interne
            self._format(libelle, 35),           # Libelle
            self._format(modepaie, 3),           # Mode paie
            self._format(echeance, 8),           # Date echeance
            self._format(sens, 1),               # Sens
            self._number(montant1, 20, 2),       # Montant1
            self._mandatory(type_ecriture, 1),   # Type ecriture
            self._format(numero_piece, 8),       # Numero de piece
            self._format(devise, 3),             # Devise
            self._number(taux_dev, 10),          # Taux devise
            self._mandatory(code_montant, 3),    # Code montant
            self._number(montant2, 20, 2),       # Montant 2
            self._number(montant3, 20, 2),       # Montant 3
            self._format(etablissement, 3),      # Etablissement
            self._format(axe, 2),                # Axe si type compte = 'A'
            self._format(numeche, 2),            # Multi echeance
        ]))

    def render(self, filename=''):
        """
        Generate the content, and store it in a file if specified
        """
        if not self._content['header']:
            raise HeaderNotFound()

        content = ''
        if self._debug_header:
            content = self._debug_toolbar()

        content += self._content['header'] + '\r\n'
        for c in self._content['lines']:
            content += c + '\r\n'
        return content

    def _debug_toolbar(self):
        """
        Generate a toolbar to debug position of datas
        """
        header = ''
        for x in range(1, self._debug_header):
            if not x % 10:
                header += '|'
            elif not x % 5:
                header += '.'
            else:
                header += ' '

        header += '\n' + ((self._debug_header - 1) * '-') + '\n'
        return header

    @staticmethod
    def _format(value, length, rpad=False, caract=' '):
        value = str(value)
        if rpad:
            return value.rjust(length, caract)[:length]
        return value.ljust(length, caract)[:length]

    def _number(self, value, length, dec=2):
        if value and isinstance(value, (int, str)):
            value = float(value)
        #else:
        #    return self._format(value, length)
        return (('%.' + str(dec) + 'f') % value).replace('.', ',').rjust(length, '0')

    def _mandatory(self, value, length, rpad=False, caract=' '):
        """Check mandary field, if missing raise an error"""
        if not value:
            raise MandatoryException()

        return self._format(value, length, rpad, caract)

    def _header(self, identifiant, origine, type_fic, format_fic, code_ex_clos,
                      date_bascule, date_arrete, num_dossier_cab, utilisateur, raison_sociale,
                      reprise, num_dossier, frequence, date_purge, sous_version):
        """
        Generate the header of the file
        """
        return ''.join([
            self._zone_fixe,                        # Prefix (***)
            self._format(identifiant, 2),           # Identifiant
            self._format(origine, 3),               # Origine Fichier
            self._format(type_fic, 3),              # Type fichier
            self._format(format_fic, 3),            # Foramt de fichier
            self._format(code_ex_clos, 3),          # Code exercice clos
            self._format(date_bascule, 8),          # date de bascule
            self._format(date_arrete, 8),           # date d'arrete periodique
            self._default_version,                  # Version du fichier
            self._format(num_dossier_cab, 5),       # Numero dossier cabinet
            self._format(self._current_date, 12),   # Date et heure
            self._format(utilisateur, 35),          # Utilisateur
            self._format(raison_sociale, 35),       # Raison sociale
            self._format(reprise, 4),               # Reprise
            self._format(num_dossier, 6),           # Numero de dossier
            self._format(frequence, 3),             # Frequence
            self._format(date_purge, 8),            # Date de purge des écritures
            self._format(sous_version, 3),          # Sous Version
        ])


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
