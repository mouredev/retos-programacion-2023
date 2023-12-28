#!/usr/bin/env sh +x
set -u
usage(){
    echo "Uso: $0 [-t TAM] [-m] [-M] [-n] [-s]"
}

declare -A conf
conf[TAM]=8
conf[MIN]='0'
conf[MAY]='0'
conf[NUM]='0'
conf[SIM]='0'
letras='abcdefghijklmnopqrstuvwxyz'
mayusculas='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros='0123456789'
simbolos="!\"#$%&\'()*+,-./:;<=>?@_"

while getopts ":t:mMns" options; do
    case "${options}" in
        t)
            conf[TAM]=${OPTARG};;
        m)
            conf[MIN]="1";;
        M)
            conf[MAY]="1";;
        n)
            conf[NUM]="1";;
        s)
            conf[SIM]="1";;
        :)
            echo "Error: -${OPTARG} requiere un argumento"
            exit 1;;
        *) usage
    esac
done
finished=0;
val=0;
tam=${conf[TAM]}
until [ $finished -eq 1 ]
do
    case $(shuf -i 0-3 -n1) in
        0)
            if [ ${conf[MIN]} = '1' ]; then
                let idx=$(shuf -i 0-26 -n1)
                echo -n "${letras:idx:1}"
                let val=$val+1
            fi
            ;;
        1)
            if [ ${conf[MAY]} = '1' ];then
                let idx=$(shuf -i 0-26 -n1)
                echo -n "${mayusculas:idx:1}"
                let val=$val+1
            fi
            ;;
        2)
            if [ ${conf[NUM]} = '1' ];then
                let idx=$(shuf -i 0-10 -n1)
                echo -n "${numeros:idx:1}"
                let val=$val+1
            fi
            ;;
        3)
            if [ ${conf[SIM]} = '1' ];then
                let idx=$(shuf -i 0-22 -n1)
                echo -n "${simbolos:idx:1}"
                let val=$val+1
            fi
            ;;
        *)
            echo "HOLA"
    esac

    if [[ ${conf[TAM]} -eq $val ]]; then let finished=1; fi
done
exit 0
