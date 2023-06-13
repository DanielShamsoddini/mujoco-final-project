import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class BODY_GENERATOR:
    def __init__(self):
        self.root = ET.Element("mujoco")
        self.option = ET.SubElement(self.root, "option")
        self.option.set("gravity", "0 0 -9.81")
        self.worldbody = ET.SubElement(self.root, "worldbody")

        # Create the light element
        self.light = ET.SubElement(self.worldbody, "light")
        self.light.set("diffuse", ".5 .5 .5")
        self.light.set("pos", "0 0 3")
        self.light.set("dir", "0 0 -1")
def generate_xml_code():

    # Create the worldbody element
    

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
    make_sensors(root)

    # Create and return the XML tree


    def make_sensors(root):
        sensor = ET.SubElement(root, "sensor")
        for a in range(1,num_sensors+1):
            touch1 = ET.SubElement(sensor, "touch")
            touch1.set("name", "test"+str(a))
            touch1.set("site", "site"+str(a))

# Test the program
    def createFile(self):
        generated_tree = ET.ElementTree(self.root)
        generated_code = ET.tostring(generated_tree.getroot(), encoding="unicode")
        dom = minidom.parseString(generated_code)

        # Output the pretty XML to a file
        output_file = "output.xml"
        with open(output_file, "w") as file:
            file.write(dom.toprettyxml())