import lxml.etree as ET

xml_filename = "f:\\SICDM_DevDocu\\Architecture\\XML_Interface_SICAM_DeviceManager.xsd"
#xsl_filename = ".\\transformer.xslt"

#xml_filename = ".\\example.xml"
#xsl_filename = ".\\example.xslt"

dom = ET.parse(xml_filename)
#xslt = ET.parse(xsl_filename)
#transform = ET.XSLT(xslt)
#newdom = transform(dom)
#print(ET.tostring(newdom, pretty_print=True))

def init():
    return dom.getroot()

def dump(e, path="", indent=""):
    tag = ET.QName(e)
    deeper=""
    if e.attrib.has_key("name"):
        path+="/"+e.attrib["name"]
        print path, tag.localname
        for k,v in e.attrib.iteritems():
            if k != "name":
                print "  %s=%s" %(k, v)
        
        deeper="  "
    #else:
    #    print indent, e
    for c in e.iterchildren(tag=ET.Element):
        dump(c, path, indent+deeper)
    
def dumpElements(root, xtype, xsdtype):
    for c in root.iterchildren(tag=xtype):
        tag = ET.QName(c)
        if type(c) == ET._Element and tag.localname == xsdtype:
            #if "Cmd_CreateProject" in c.attrib["name"]:
                print
                dump(c)

if __name__ == "__main__":
    print "main"
    root = init()
    dumpElements(root, ET.Element, "complexType")
    print
    dumpElements(root, ET.Element, "element")
else:
    print "wot"
    root = init()
