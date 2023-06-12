from xml.dom import minidom

doc = minidom.Document()

doc.appendChild(doc.createElement('mujoco'))



xml_str = doc.toprettyxml(indent ="\t") 
  
save_path_file = "gfg.xml"
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 