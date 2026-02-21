from flask import Flask, jsonify, request   

app = Flask(__name__) #Inicilaizar la aplicación tipo Flask

#url = 'http://localhost:8080/api/' #URL de mi microservicio

@app.route('/')
def home(): #Ruta principal
    #return "Bienvenido a mi microservicio"
    return jsonify({'message': 'Bienvenido a la API de Microservicio Base - Tratamiento de Datos Paralelo A'}) #Retorna un mensaje en formato JSON

#Endpoint 1 (para sumar dos números)
@app.route('/api/sumar', methods=['POST']) 
def sumar(): #Ruta para sumar dos números
    data = request.get_json() #Obtener los datos enviados en formato JSON
    a = data.get('a') #Obtener el valor de 'a' del JSON
    b = data.get('b') 
    if a is None or b is None: #Validar que ambos valores existan
        return jsonify({"error": "Parámetros 'a' y 'b' son requeridos"}), 400 #Retornar un error si falta algún parámetro
    return jsonify({"resultado": a+b}) #Retornar el resultado en formato JSON

#Endpoint 2
@app.route('/api/info', methods=['GET']) 
def info():
    return jsonify({
        'nombre': 'Microservicio Base - Tratamiento de Datos Paralelo A',
        'version': '1.0.0',
        'descripcion': 'Este microservicio realiza operaciones básicas de suma y proporciona información del servicio.',
        'autor': 'Carlos Vintimilla',
    })

#Endpoint 3 (para multiplicar dos números)
@app.route('/api/multiplicar', methods=['POST']) # Endpoint para multiplicar dos números
def multiplicar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a * b})


if __name__ == '__main__': #Ejecuta mi aplicacion cuando yo llame a mi script
    app.run(debug=True, host='0.0.0.0', port=8080)  # Permite que la aplicación sea accesible desde cualquier IP en el puerto 8080


