from lxml import etree
# Charger le document XML source
source_doc = etree.parse("source.xml")
# Charger la feuille de style XSLT
xslt_doc = etree.parse("style.xsl")
# Créer un transformateur XSLT
transformer = etree.XSLT(xslt_doc)
# Appliquer la transformation
result = transformer(source_doc)
# Afficher le résultat 
print(result)