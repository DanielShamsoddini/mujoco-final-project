import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def generate_xml_code():
    # Create the root element
    root = ET.Element("mujoco")

    # Create the option element
    option = ET.SubElement(root, "option")
    option.set("gravity", "0 0 -9.81")

    # Create the worldbody element
    worldbody = ET.SubElement(root, "worldbody")

    # Create the light element
    light = ET.SubElement(worldbody, "light")
    light.set("diffuse", ".5 .5 .5")
    light.set("pos", "0 0 3")
    light.set("dir", "0 0 -1")

    # Create the plane geom element
    plane_geom = ET.SubElement(worldbody, "geom")
    plane_geom.set("type", "plane")
    plane_geom.set("size", "10 10 0.1")
    plane_geom.set("rgba", ".9 0 0 1")

    # Create the nested body elements
    body = ET.SubElement(worldbody, "body")
    body.set("pos", "0 0 0.5")

    geom1 = ET.SubElement(body, "geom")
    geom1.set("size", "0.1")
    geom1.set("rgba", "0 0 1 1")

    joint1 = ET.SubElement(body, "joint")
    joint1.set("type", "free")

    site1 = ET.SubElement(body, "site")
    site1.set("name", "site1")
    site1.set("size", "0.1")
    site1.set("rgba", "1 0 0 1")

    body2 = ET.SubElement(body, "body")
    body2.set("pos", "0.2 0 0")

    joint2 = ET.SubElement(body2, "joint")
    joint2.set("name", "onejoint")
    joint2.set("pos", "-0.1 0 0")
    joint2.set("type", "ball")
    joint2.set("limited", "true")
    joint2.set("range", "0 60")

    geom2 = ET.SubElement(body2, "geom")
    geom2.set("size", "0.1")
    geom2.set("rgba", "0 0 1 1")

    site2 = ET.SubElement(body2, "site")
    site2.set("name", "site2")
    site2.set("pos", "0 0 0")
    site2.set("size", "0.1")
    site2.set("rgba", "1 0 0 1")

    body3 = ET.SubElement(body2, "body")
    body3.set("pos", "0.1 0 0")

    joint3 = ET.SubElement(body3, "joint")
    joint3.set("name", "threejoint")
    joint3.set("type", "ball")
    joint3.set("limited", "true")
    joint3.set("range", "0 60")

    geom3 = ET.SubElement(body3, "geom")
    geom3.set("size", "0.1")
    geom3.set("rgba", "0 0 1 1")
    geom3.set("pos", "0.1 0 0")

    site3 = ET.SubElement(body3, "site")
    site3.set("name", "site3")
    site3.set("pos", "0.1 0 0")
    site3.set("size", "0.1")
    site3.set("rgba", "1 0 0 1")

    body4 = ET.SubElement(body3, "body")
    body4.set("pos", "0.2 0 0")

    joint4 = ET.SubElement(body4, "joint")
    joint4.set("name", "fourjoint")
    joint4.set("type", "ball")
    joint4.set("limited", "true")
    joint4.set("range", "0 60")

    geom4 = ET.SubElement(body4, "geom")
    geom4.set("size", "0.1")
    geom4.set("rgba", "0 0 1 1")
    geom4.set("pos", "0.1 0 0")

    site4 = ET.SubElement(body4, "site")
    site4.set("name", "site4")
    site4.set("pos", "0.1 0 0")
    site4.set("size", "0.1")
    site4.set("rgba", "1 0 0 1")

    body5 = ET.SubElement(body4, "body")
    body5.set("pos", "0.2 0 0")

    joint5 = ET.SubElement(body5, "joint")
    joint5.set("name", "fivejoint")
    joint5.set("type", "ball")
    joint5.set("limited", "true")
    joint5.set("range", "0 60")

    geom5 = ET.SubElement(body5, "geom")
    geom5.set("size", "0.1")
    geom5.set("rgba", "0 0 1 1")
    geom5.set("pos", "0.1 0 0")

    site5 = ET.SubElement(body5, "site")
    site5.set("name", "site5")
    site5.set("size", "0.1")
    site5.set("pos", "0.1 0 0")
    site5.set("rgba", "1 0 0 1")

    # Create the actuator element
    actuator = ET.SubElement(root, "actuator")

    motor1 = ET.SubElement(actuator, "motor")
    motor1.set("name", "motor1")
    motor1.set("joint", "onejoint")
    motor1.set("gear", "1")

    motor3 = ET.SubElement(actuator, "motor")
    motor3.set("name", "motor3")
    motor3.set("joint", "threejoint")
    motor3.set("gear", "1")

    motor4 = ET.SubElement(actuator, "motor")
    motor4.set("name", "motor4")
    motor4.set("joint", "fourjoint")
    motor4.set("gear", "1")

    motor5 = ET.SubElement(actuator, "motor")
    motor5.set("name", "motor5")
    motor5.set("joint", "fivejoint")
    motor5.set("gear", "1")

    # Create the sensor element
    sensor = ET.SubElement(root, "sensor")

    touch1 = ET.SubElement(sensor, "touch")
    touch1.set("name", "test1")
    touch1.set("site", "site1")

    touch2 = ET.SubElement(sensor, "touch")
    touch2.set("name", "test2")
    touch2.set("site", "site2")

    touch3 = ET.SubElement(sensor, "touch")
    touch3.set("name", "test3")
    touch3.set("site", "site3")

    touch4 = ET.SubElement(sensor, "touch")
    touch4.set("name", "test4")
    touch4.set("site", "site4")

    touch5 = ET.SubElement(sensor, "touch")
    touch5.set("name", "test5")
    touch5.set("site", "site5")

    # Create and return the XML tree
    tree = ET.ElementTree(root)
    return tree


# Test the program
generated_tree = generate_xml_code()
generated_code = ET.tostring(generated_tree.getroot(), encoding="unicode")
dom = minidom.parseString(generated_code)

# Output the pretty XML to a file
output_file = "output.xml"
with open(output_file, "w") as file:
    file.write(dom.toprettyxml())