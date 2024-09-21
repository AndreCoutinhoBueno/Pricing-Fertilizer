# Comexstat
[The governmental portal](http://comexstat.mdic.gov.br/pt/geral) provides free access to Brazil's foreign trade statistics, with data used to construct the Brazilian trade balance, detailed by NCM or by municipalities of the exporter/importer.

The site indicates that the data is available in compressed files containing CSV files, using a semicolon (;) as the delimiter, with column names in the first row.

The import and export tables by NCM have the following structure:

* Ordinal Columns:
    * CO_ANO: year of the record
    * CO_MES: month of the record

* Categorical Columns:
    * CO_ANO and CO_MES: in addition to their ordinal value, these columns also represent categorical values, related to the climate of the indicated period.
    * CO_NCM: NCM (Mercosur Common Nomenclature), which identifies the product based on the International System (HS) of the World Trade Organization, with two additional digits that further specify the characteristics of the imported goods.
    * CO_UNID: monetary unit of value used in the record, textually identified in an auxiliary table.
    * CO_PAIS: country of origin, textually identified in an auxiliary table.
    * CO_VIA: physical transportation route, textually identified in an auxiliary table.
    * CO_URF: Federal Revenue Unit, linked to a disembarkation port, textually identified in an auxiliary table.
    * SG_UF_NCM: contains the acronym of the federative unit of the import destination, textually identified in an auxiliary table.

* Quantitative Columns:
    * QT_ESTAT: contains the quantity of the imported product in the unit typically used in the country of origin, which may differ from the main standard, the kilogram.
    * KG_LIQUIDO: contains the weight of the import in kilograms.
    * VL_FOB: quantifies the monetary value of the goods in the [FOB](https://en.wikipedia.org/wiki/Free_on_Board) modality.
    * VL_FRETE: quantifies the transportation cost of the imported quantity from the country of origin to Brazil.
    * VL_SEGURO: quantifies the insurance cost of the goods during transportation from the country of origin to Brazil.

To fully utilize the data files, it is necessary to download and use the Auxiliary Tables containing the "Code and Classification Correlations".