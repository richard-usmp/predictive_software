def generar_datos(num_datos):
    datos_generados = []
    ultimo_numero = int(datos[-1].split('-')[1])
    
    for i in range(num_datos):
        nuevo_numero = ultimo_numero + i + 1
        nuevo_dato = f'G-{str(nuevo_numero).zfill(8)}'
        datos_generados.append(nuevo_dato)
    
    return datos_generados

# Ejemplo de uso
datos = [
    'G-61126247',
    'G-65142934',
    'G-66997523',
    'G-06392739',
    'G-68518715',
    'G-07285941',
    'G-68471901',
    'G-62762865',
    'G-09702554',
    'G-09828994',
    'G-08429537',
    'G-08243821',
    'G-06731226',
    'G-07066597',
    'G-62041972',
    'G-09440996',
    'G-66307087',
    'G-62662662',
    'G-09973678',
    'G-08851803'
]

nuevos_datos = generar_datos(30)
print(nuevos_datos)


