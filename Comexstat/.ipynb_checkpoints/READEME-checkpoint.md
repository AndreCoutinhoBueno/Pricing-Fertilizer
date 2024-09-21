# [Comex Stat](http://comexstat.mdic.gov.br/pt/home)

> Portal para acesso gratuito às estatísticas de comércio exterior do Brasil. Cria consultas detalhadas das exportações e importações brasileiras com as diversas variáveis da base de dados estatísticos.

Estrutura das tabelas de importação e exportação por NCM:  

* Colunas ordinais:
    * CO_ANO: ano do registro
    * CO_MES: mês do registro

* Colunas categóricas:
    * CO_ANO e CO_MES: além do valor ordinal, essas colunas representam também valor categórico, ligados ao clima do momento indicado.
    * CO_NCM: NCM-Nomenclatura Comum do Mercosul, que identifica o produto com base no Sistema Internacional (SH) da Organização Mundial do Comércio, acrescido de mais dois dígitos extras, que especificam ainda mais as características das mercadorias importadas.
    * CO_UNID: unidade monetária de valor utilizada no registro, que é identificada textualmente em tabela auxiliar.
    * CO_PAIS: país de origem, identificado textualmente em tabela auxiliar.
    * CO_VIA:  via física de transporte, identificada textualmente em tabela auxiliar.
    * CO_URF:  Unidade da Receita Federal, ligada ao um porto de desembarque, identificada textualmente em tabela auxiliar.
    * SG_UF_NCM: contém a sigla unidade federativa de destino da importação, identificada textualmente em tabela auxiliar.

  
* Colunas quantitativas:
    * QT_ESTAT: contém a quantidade de produto importado em unidade tipicamente utilizada no país de origem, que pode ser diferente do padrão principal, o quilograma.
    * KG_LIQUIDO contém o peso da importação em quilograma
    * VL_FOB quantifica o valor monetário da mercadoria na modalidade [FOB](https://pt.wikipedia.org/wiki/Free_on_Board#:~:text=Na%20modalidade%20FOB%2C%20o%20remetente,do%20seguro%20a%20partir%20da%C3%AD.)
    * VL_FRETE quantifica o valor do transporte da quantidade importada, do país de origem até o Brasil.
    * VL_SEGURO quantifica o valor do seguro sobre a mercadoria durante o transporte do país de origem até o Brasil.