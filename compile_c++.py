#!/usr/bin/env python

import sys, os
import argparse

args = sys.argv

def main(replace, show_data, file_path, exe, exclude, exlusive):
    existing_file = os.path.exists(exe)
    
    if existing_file and replace:
        os.remove(exe)
    elif existing_file:
        print(f'Archivo existente: El archivo "{exe}" ya existe en la carpeta "file_path", si desea remplazarlo pruebe con el argumento --replace')
        return

    files = os.listdir(file_path)

    command = f'g++ -o {exe} '

    for f in files:
        if '.cpp' in f and f not in exclude:
            command += os.path.abspath(file_path) + '/' + f + ' '

    output = os.system(command)
    
    if output: return

    if show_data:
        print('\n'.join(command[6::].split()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compila todos los archivos de una carpeta')
    
    parser.add_argument('-r', '--replace', action='store_true', help='Remplaza el arhivo con el mismo nombre en caso de existir')
    parser.add_argument('-s', '--show', action='store_true', help='Muestra los archivos que fueron compilados')
    
    parser.add_argument('-e', '--exclude', nargs='+', help='Exluye los archivos que no van a ser compilados')
    parser.add_argument('-E', '--exclusive', nargs='+', help='Elije los archivos que se van a compilar')
    
    parser.add_argument('path', nargs=1, help='Se ingresa la ruta absoluta de la carpeta')
    parser.add_argument('name', nargs=1, help='Nombre del ejecutable')
    
    args = parser.parse_args()

    if not args.exclude:
        args.exclude = []
    if not args.exclusive:
        args.exclusive = []
    
    main(args.replace, args.show, *args.path, *args.name, args.exclude, args.exclusive)
