#!/usr/bin/env python

import sys, os
import argparse

def main(replace, show_data, file_path, name, exclude, execute, params):
    existing_file = os.path.exists(name)
    
    files = os.listdir(file_path)

    command = f'g++ -o {name} '
    
    for f in files:
        if '.cpp' in f and f not in exclude:
            command += os.path.abspath(file_path) + '/' + f + ' '
    
    # check the existence of a file with the same name 
    if existing_file and replace:
        os.remove(name)
    elif existing_file:
        print(f'Archivo existente: El archivo "{name}" ya existe en la carpeta "file_path", si desea remplazarlo pruebe con el argumento --replace')
        return
    
    # Execute command
    output = os.system(command)
    if output: return

    if show_data:
        print('\n'.join(command[6::].split()))

    if execute:
        print('\nEjecucion:')
        output = os.system(f'./{name} {' '.join(params)}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compila todos los archivos de una carpeta')
    
    parser.add_argument('-r', '--replace', action='store_true', help='Remplaza el arhivo con el mismo nombre en caso de existir')
    parser.add_argument('-s', '--show', action='store_true', help='Muestra los archivos que fueron compilados')
    parser.add_argument('-E', '--execute', action='store_true', help='Ejecuta el programa despues de compilarse')
    
    parser.add_argument('-e', '--exclude', nargs='+', help='Exluye los archivos que no van a ser compilados')
    parser.add_argument('-p', '--parameters', nargs='+', help='Manda los parametros ingresados al programa como input')    

    parser.add_argument('name', nargs=1, help='Nombre del ejecutable')
    parser.add_argument('path', nargs=1, help='Se ingresa la ruta absoluta de la carpeta')

    args = parser.parse_args()

    if not args.exclude:
        args.exclude = []
    
    main(args.replace, args.show, *args.path, *args.name, args.exclude, args.execute, args.parameters)
