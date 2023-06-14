import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class BODY_GENERATOR:
    def __init__(self):
        self.root = ET.Element("mujoco")
        option = ET.SubElement(self.root, "option")
        option.set("gravity", "0 0 -9.81")
        self.worldbody = ET.SubElement(self.root, "worldbody")

        # Create the light element
        light = ET.SubElement(self.worldbody, "light")
        light.set("diffuse", ".5 .5 .5")
        light.set("pos", "0 0 3")
        light.set("dir", "0 0 -1")
        plane_geom = ET.SubElement(self.worldbody, "geom")
        plane_geom.set("type", "plane")
        plane_geom.set("size", "10 10 0.1")
        plane_geom.set("rgba", ".9 0 0 1")

    def generate_xml(start_pos, body_count):
        def create_element(parent, tag, attributes=None):
            element = ET.SubElement(parent, tag)
            if attributes:
                element.attrib.update(attributes)
            return element

        worldbody = ET.Element("worldbody")

        current_body = create_element(worldbody, "body", {"pos": start_pos})

        for i in range(1, body_count + 1):
            body = create_element(current_body, "body", {"pos": f"{0.2 * i} 0 0"})
            joint = create_element(body, "joint", {"name": f"joint{i}", "type": "ball", "limited": "true", "range": "0 60"})
            geom = create_element(body, "geom", {"size": "0.1", "rgba": "0 0 1 1", "pos": "0.1 0 0"})
            site = create_element(body, "site", {"name": f"site{i}", "pos": "0.1 0 0", "size": "0.1", "rgba": "1 0 0 1"})

            current_body = body

        return ET.tostring(worldbody).decode()

    # Example usage
    xml_code = generate_xml("0 0 0.5", 5)
    print(xml_code)


    # Create the sensor element
    make_sensors()
    make_motors()

    # Create and return the XML tree


    def geom_site_write(parentelem, position):
        <geom size="0.1" rgba="0 0 1 1" pos="0 -0.1 0"/>
		<site name="site6" pos="0 -0.1 0" size="0.1" rgba="1 0 0 1"/>
        geom = ET.SubElement(parentelem, "geom")
        geom.set("size", self.spheresize)
        geom.set("rgba", "0 0 1 1")
        geom.set("pos", position)
        site = ET.SubElement(parentelem, "site")
        site.set("name", )
        site.set("size", self.spheresize)
        site.set("rgba", "0 0 1 1")
        site.set("pos", position)


    def make_motors():
        actuator = ET.SubElement(self.root, "actuator")
        for a in range(1,self.num_motors+1):
            motor = ET.SubElement(actuator, "motor")
            motor.set("name", "motor"+str(a))
            motor.set("joint", str(a)+"joint")
            motor.set("gear", "1")


    def make_sensors():
        sensor = ET.SubElement(self.root, "sensor")
        for a in range(1,self.num_sensors+1):
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