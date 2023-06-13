import xml.etree.ElementTree as ET
import random
import xml.dom.minidom as minidom

# Function to generate a random position in Mujoco format
def generate_random_position(spheres, radius):
    if not spheres:
        return "0 0 0"  # First sphere at the origin

    while True:
        pos = f"{random.uniform(-1, 1)} {random.uniform(-1, 1)} {random.uniform(-1, 1)}"
        collision = False
        for sphere in spheres:
            sphere_pos = sphere.find("body").get("pos")
            sphere_radius = float(sphere.find("body/geom").get("size")) / 2
            dist = sum((float(a) - float(b)) ** 2 for a, b in zip(sphere_pos.split(), pos.split())) ** 0.5
            if dist < 2 * radius + sphere_radius:  # Adjusted collision check
                collision = True
                break
        if not collision:
            return pos

# Function to generate a random sphere element
def generate_sphere(index, pos):
    sphere = ET.Element("body")
    sphere.set("name", f"sphere{index}")
    geom = ET.SubElement(sphere, "geom")
    geom.set("name", f"geom{index}")
    geom.set("type", "sphere")
    geom.set("size", "0.1")
    geom.set("rgba", "1 0 0 1")
    sphere.set("pos", pos)
    return sphere

# Create the root element
root = ET.Element("mujoco")

# Create the worldbody element
worldbody = ET.SubElement(root, "worldbody")

# Add a plane
plane = ET.SubElement(worldbody, "geom")
plane.set("name", "plane")
plane.set("type", "plane")
plane.set("size", "1 1 0.02")
plane.set("rgba", "0.9 0.9 0.9 1")

# Generate the spheres
num_spheres = 2
spheres = []
radius = 0.1  # Sphere radius
parent = worldbody  # Parent element to which sub-bodies will be appended

for i in range(num_spheres):
    pos = generate_random_position(spheres, radius)
    sphere = generate_sphere(i, pos)

    # Create a sub-body for the sphere
    sub_body = ET.Element("body")
    sub_body.set("name", f"subbody{i}")
    sub_body.append(sphere)

    if i > 0:
        # Generate a ball joint between the current and previous sub-bodies
        ball_joint = ET.SubElement(sub_body, "joint")
        ball_joint.set("name", f"joint_{sub_body.get('name')}_{spheres[i-1].get('name')}")
        ball_joint.set("type", "ball")
        ball_joint.set("limited", "false")


    # Append the sub-body to the parent
    parent.append(sub_body)

    spheres.append(sub_body)

    # Set the current sub-body as the parent for the next iteration
    parent = sub_body

# Create an ElementTree object with the root element
tree = ET.ElementTree(root)

# Write the XML to a string
xml_string = ET.tostring(root, encoding="utf-8")

# Prettify the XML string
dom = minidom.parseString(xml_string)
pretty_xml_string = dom.toprettyxml(indent="  ")

# Remove the default XML declaration added by minidom
pretty_xml_string = "\n".join(line for line in pretty_xml_string.split("\n") if line.strip())

# Write the prettified XML to a file
with open("output.xml", "w") as file:
    file.write(pretty_xml_string)
