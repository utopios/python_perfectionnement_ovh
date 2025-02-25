import xml.dom.minidom
# Parse le fichier XML
dom_tree = xml.dom.minidom.parse("example.xml")
# Obtient le document root
root_element = dom_tree.documentElement
print("Element racine :", root_element.tagName)
# Parcours les éléments enfants du root
for node in root_element.childNodes:
    if node.nodeType == node.ELEMENT_NODE:
        print("\nÉlément :", node.tagName)
        # Parcours les attributs de l'élément
        if node.hasAttributes():
            print("Attributs :")
            for attr_name, attr_value in node.attributes.items():
                print(f"{attr_name} = {attr_value}")
        # Parcours les nœuds enfants
        for child_node in node.childNodes:
            if child_node.nodeType == child_node.TEXT_NODE:
                print("Contenu :", child_node.data)
# Exemple de modification du contenu
first_child = root_element.firstChild
first_child.data = "Nouveau contenu"
# Enregistrer les modifications dans un nouveau fichier XML
with open("nouveau_exemple.xml", "w") as new_xml_file:
    dom_tree.writexml(new_xml_file)