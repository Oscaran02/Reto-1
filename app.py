def cdt(usuario: str, capital: int, tiempo_cdt: int) -> str:
    if tiempo_cdt > 2:
        valor_interes = capital * (0.03 * tiempo_cdt) / 12
        valor_cdt = capital + valor_interes
        return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo_cdt} meses es: {valor_cdt}")
    else:
        cantidad_perder = capital * 0.02
        valor_cdt = capital - cantidad_perder
        return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo_cdt} meses es: {valor_cdt}")

print(cdt("Juan", 100000, 24))