<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xmile="http://docs.oasis-open.org/xmile/ns/XMILE/v1.0"
    xmlns:isee="http://iseesystems.com/XMILE">

    <xsl:output method="text"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="/">
        <xsl:apply-templates select="//xmile:model" />
    </xsl:template>

    <xsl:template match="xmile:model">
        <xsl:text>{</xsl:text>
        <xsl:value-of select="concat('&quot;model&quot;: &quot;',./@name,'&quot;, ')" />
        <xsl:text>&quot;variables&quot;: [</xsl:text>
        <xsl:apply-templates select="xmile:variables"/>
        <xsl:text>]</xsl:text>
        <xsl:text>}</xsl:text>
    </xsl:template>

    <xsl:template match="xmile:variables">
        <xsl:apply-templates select="xmile:aux[xmile:gf]"/>
    </xsl:template>

    <xsl:template match="xmile:aux">
        <xsl:if test="position() &gt; 1">
            <xsl:text>, </xsl:text>
        </xsl:if>
        <xsl:text>{ &quot;name&quot;: &quot;</xsl:text>
        <xsl:value-of select="@name" />
        <xsl:text>&quot;,</xsl:text>
        <xsl:apply-templates select="xmile:gf"/>
        <xsl:text>}</xsl:text>
    </xsl:template>

    <xsl:template match="xmile:gf">
        <xsl:text>&quot;gf&quot;: { </xsl:text>
        <xsl:text>&quot;type&quot;: &quot;</xsl:text>
        <xsl:value-of select="@type" />
        <xsl:text>&quot;, </xsl:text>
        <xsl:text>&quot;xmin&quot;: &quot;</xsl:text>
        <xsl:value-of select="xmile:xscale/@min" />
        <xsl:text>&quot;, </xsl:text>
        <xsl:text>&quot;xmax&quot;: &quot;</xsl:text>
        <xsl:value-of select="xmile:xscale/@max" />
        <xsl:text>&quot;, </xsl:text>
        <xsl:text>&quot;ymin&quot;: &quot;</xsl:text>
        <xsl:value-of select="xmile:yscale/@min" />
        <xsl:text>&quot;, </xsl:text>
        <xsl:text>&quot;ymax&quot;: &quot;</xsl:text>
        <xsl:value-of select="xmile:yscale/@max" />
        <xsl:text>&quot;, </xsl:text>
        <xsl:text>&quot;ypts&quot;: &quot;</xsl:text>
        <xsl:value-of select="xmile:ypts" />
        <xsl:text>&quot;</xsl:text>
        <xsl:text> }</xsl:text>
    </xsl:template>

</xsl:stylesheet>