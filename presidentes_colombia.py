##PRESIDENTES DE LA HISTORIA POLÍTICA DE COLOBMIA##


#presidentes de las Provincias Unidas de la Nueva Granada

apellidos_pre_pro = ["Pey","Lozano", "Nariño", "de Castro",
                     "de Ayala", "Arrubla", "Gamba", "de Vergara",
                     "Álvarez", "Torres", "Restrepo", "Fernández",
                     "Camacho", "Valenzuela", "de Villavicencio", "Torices",
                     "García", "Serrano", "Mejía"]

departamento_pre_pro = ["Bogotá", "Bogotá", "Bogotá", "Bogotá",
                        "Bogotá", "Antioquia", "Tolima", "Bogotá",
                        "Bogotá", "Cauca", "Antioquia", "Bolívar",
                        "Boyacá", "Santander", "Ecuador", "Bolívar",
                        "Santander", "Santander", "Antioquia"]

#presidentes de la Gran Colombia

apellidos_pre_gc = ["Bolívar", "Santander", "Vergara", "Caycedo",
                    "Mosquera", "Urdaneta", "García del Río"]

departamento_pre_gc = ["Venezuela", "Norte de Santander", "Bogotá", "Bogotá",
                       "Cauca", "Venezuela", "Bolívar"]


#presidentes la República de la Nueva Granada

apellidos_pre_ng = ["Obando", "Santander", "Márquez", "Alcántara",
                    "Mosquera", "López", "Obando", "Melo", "Herrera",
                    "de Obaldía", "Mallarino", "Ospina"]

departamento_pre_ng = ["Cauca", "Norte de Santander", "Boyacá", "Bogotá",
                       "Cauca", "Cauca", "Cauca", "Tolima",
                       "Panamá", "Panamá", "Valle del Cauca", "Cundinamarca"]

#presidentes de la Confederación de la Nueva Granada

apellidos_pre_con = ["Ospina", "Nieto", "de Mosquera", "Calvo"]

departamento_pre_con = ["Cundinamarca", "Atlántico", "Cauca", "Bolívar"]

#presidentes de los Estados Unidos de Colombia

apellidos_pre_eu = ["de Mosquera", "Largacha", "López", "Salgar", "Gutierrez",
                    "Murillo", "Rojas", "Riascos", "Acosta",
                    "Pérez", "Parra", "Trujillo", "Nuñez",
                    "Zaldúa", "Calderón", "Otálora", "Hurtado",
                    "Campo"]

departamento_pre_eu = ["Cauca", "Cauca", "Cauca", "Bogotá",
                       "Boyacá", "Tolima", "Huila", "Panamá",
                       "Boyacá", "Cundinamarca", "Santander", "Cauca",
                       "Bolívar", "Bogotá", "Boyacá", "Cundinamarca",
                       "Cauca", "Magdalena"]

#presidentes de la República de Colombia

apellidos_pre_rp = [
    "Campo", "Payán", "Nuñez", "Holguín", "Caro",
    "Sanclemente", "Reyes", "González", "Restrepo", "Concha",
    "Suarez", "Ospina", "Méndez", "Olaya", "López",
    "Santos", "López", "Ospina", "Gómez", "Urdaneta",
    "Lleras", "León", "Lleras", "Pastrana", "López",
    "Turbay", "Betancur", "Barco", "Gaviria", "Samper",
    "Pastrana", "Uribe", "Santos", "Duque", "Petro",
    "De la Espriella"
]

departamento_pre_rp = [
    "Magdalena", "Valle del Cauca", "Bolívar", "Valle del Cauca", "Bogotá",
    "Valle del Cauca", "Boyacá", "Norte de Santander", "Antioquia", "Bogotá",
    "Antioquia", "Bogotá", "Tolima", "Boyacá", "Tolima",
    "Bogotá", "Tolima", "Antioquia", "Bogotá", "Bogotá",
    "Bogotá", "Cauca", "Bogotá", "Huila", "Bogotá",
    "Bogotá", "Antioquia", "Norte de Santander", "Risaralda", "Bogotá",
    "Bogotá", "Antioquia", "Bogotá", "Bogotá", "Córdoba",
    "Bogotá"
]



###CONTAR DEPARTAMENTOS###

#NUEVA GRADANADA

print("\n" + "="*51 + "\n")

print("Provincias Unidas de la Nueva Granada (1811-1816): \n")

print(f"Total de presidentes: {len(apellidos_pre_pro)} \n")
for lugares_pro in sorted(set(departamento_pre_pro)):
    print(f"{lugares_pro}: {departamento_pre_pro.count(lugares_pro)}")   
print("\n" + "="*51 + "\n")

#GRAN COLOMBIA

print("Gran Colombia (1819-1831): \n")

print(f"Total de presidentes: {len(apellidos_pre_gc)} \n")
for lugares_gc in sorted(set(departamento_pre_gc)):
    print(f"{lugares_gc}: {departamento_pre_gc.count(lugares_gc)}")
print("\n" + "="*51 + "\n")

#REPÚBLICA DE LA NUEVA GRANADA

print("República de la Nueva Granada (1831-1858): \n")
print(f"Total de presidentes: {len(apellidos_pre_ng)} \n")
for lugares_ng in sorted(set(departamento_pre_ng)):
    print(f"{lugares_ng}: {departamento_pre_ng.count(lugares_ng)}")
print("\n" + "="*51 + "\n")

#CONFEDERACIÓN DE LA NUEVA GRANADA

print("Confederación de la Nueva Granada (1858-1863): \n")
print(f"Total de presidentes: {len(apellidos_pre_con)} \n")
for lugares_con in sorted(set(departamento_pre_con)):
    print(f"{lugares_con}: {departamento_pre_con.count(lugares_con)}")
print("\n" + "="*51 + "\n")

#ESTADOS UNIDOS DE COLOMBIA

print("Estados Unidos de Colombia (1863-1886): \n")
print(f"Total de presidentes: {len(apellidos_pre_eu)} \n")
for lugares_eu in sorted(set(departamento_pre_eu)):
    print(f"{lugares_eu}: {departamento_pre_eu.count(lugares_eu)}")
print("\n" + "="*51 + "\n")

#REPÚBLICA DE COLOMBIA

print("República de Colombia (1886-actualidad): \n")
print(f"Total de presidentes: {len(apellidos_pre_rp)} \n")
for lugares_rp in sorted(set(departamento_pre_rp)):
    print(f"{lugares_rp}: {departamento_pre_rp.count(lugares_rp)}")
print("\n" + "="*51 + "\n")

###REPRESENTACIÓN PRESIDENCIAL ACUMULADA###

todos_los_departamentos = (
    departamento_pre_pro + 
    departamento_pre_gc + 
    departamento_pre_ng + 
    departamento_pre_con + 
    departamento_pre_eu + 
    departamento_pre_rp
)


print(len(todos_los_departamentos))

# --- CONTAR Y MOSTRAR ORDENADO ---
print("\nREPRESENTACIÓN PRESIDENCIAL ACUMULADA POR DEPARTAMENTO\n")
for depto in sorted(set(todos_los_departamentos)):
    print(f"{depto}: {todos_los_departamentos.count(depto)} presidentes")




