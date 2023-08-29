persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
if "skills" in persona:
    print(persona["skills"][2])
if "skills" in persona:
    if "Python" in persona["skills"]:
        print("Python")
if "skills" in persona:
    if "Javascript" and 'react' in persona["skills"]:
        print("El es un desarrollador fronted")
    elif "Node" and "Python" and "MongoDB" in persona["skills"]:
        print("El es un desarrollador backend")
    elif "React" and "Node"  and "MongoDB" in persona["skills"]:
        print("Desarrollador full stack")
    else:
        print("Titulo desconocido")