<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>
  <xsl:template match="/livres">
    <livres>
      <xsl:apply-templates select="livre"/>
    </livres>
  </xsl:template>
  <xsl:template match="livre">
    <livre annee="{annee_parution}" genre="{genre}" >
      <xsl:value-of select="titre" /> - <xsl:value-of select="auteur" /> 
    </livre>
  </xsl:template>
</xsl:stylesheet>