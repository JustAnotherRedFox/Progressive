#!/bin/zsh
echo 'digite um arquivo'
read archive;

if [ e$archive ];
    then 
        echo "o arquivo existe"
    else
        echo "o arquivo nao existe"
fi

if [ d$archive ];
    then
        echo "o arquivo e um diretorio"
    else
        echo "o arquivo nao e um diretorio"
fi

if [ f$archive ];
    then
        echo "o arquivo e um arquivo regular"
    else
        echo "o arquivo nao e um arquivo regular"
fi

