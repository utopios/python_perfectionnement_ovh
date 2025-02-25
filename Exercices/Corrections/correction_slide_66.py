from lxml import etree

with open("livres.xml", "r", encoding="utf-8") as reader:
    content = reader.read()
    source = etree.fromstring(content)
    transform = etree.parse("transform.xsl")
    transformer = etree.XSLT(transform)
    result = transformer(source)

with open("new_result.xml", 'w') as file:
    file.write(str(result))

print(result)