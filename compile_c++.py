#!/usr/bin/env python

import sys, os, time
import argparse

args = sys.argv

def main(file_path, exe, replace, show_data):
    cpp_exist = False
    
    if os.path.exists(exe) and not replace:
        x = input(f'--> El archivo "{exe}" ya existe, ¿quieres remplazarlo? (S/N)\n>>> ')
        if x == 'S':
            replace = True
        else:
            return f'El archivo "{exe}" queda intacto'
            return

    if os.path.exists(exe) and replace:
        os.remove(exe)

    files = os.listdir(file_path)
    
    if not len(files) or sum(x.count('.cpp') for x in files) == 0:
        return 'No se encontro ningun archivo'

    command = f'g++ -o {exe} '

    for f in files:
        if (f.count('.cpp')):
            command += file_path + '/' + f + ' '

    os.system(command)

    print('- Se han compilado correctamente todos los archivos -\n')
    if show_data:
        return '\n'.join(command[6::].split())

    return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compila todos los archivos de una carpeta')
    
    parser.add_argument('-p', '--path', help='Se ingresa la ruta absoluta de la carpeta')
    parser.add_argument('-n', '--name', help='Nombre del ejecutable')
    parser.add_argument('-r', '--replace', action='store_true', help='Remplaza el arhivo con el mismo nombre en caso de existir')
    parser.add_argument('-s', '--show', action='store_true', help='Muestra los archivos que fueron compilados')
    
    args = parser.parse_args()
    
    if not args.path or not args.name:
        print('Hacen falta 1 o mas parametros. Consulta "compilecpp -h" para mas informacion')
        exit()

    print(main(args.path, args.name, args.replace, args.show))
