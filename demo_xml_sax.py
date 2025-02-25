import xml.sax


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
    # Méthode appelée lorsque le parser rencontre un nouvel élément
    def startElement(self, name, attrs):
        print("Élément trouvé :", name)
        if attrs:
            print("Attributs :")
            for attr_name, attr_value in attrs.items():
                print(f"{attr_name} = {attr_value}")
    # Méthode appelée lorsque le parser rencontre une balise de fin
    def endElement(self, name):
        print("Fin de l'élément :", name)
    # Méthode appelée lorsque le parser rencontre du texte
    def characters(self, content):
        if content not in " \n":
            print("Contenu :", content)

xml_handler = XMLHandler()

parser = xml.sax.make_parser()

parser.setContentHandler(xml_handler)

with open("example.xml") as file:
    parser.parse(file)