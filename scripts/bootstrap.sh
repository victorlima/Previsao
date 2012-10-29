#!/bin/sh
if [ ! -n "${VIRTUAL_ENV_DIR}" ]; then 
    VIRTUAL_ENV_DIR="./ve"
else
    VIRTUAL_ENV_DIR="${VIRTUAL_ENV_DIR}"
fi

if [ -z ${VIRTUAL_ENV} ]; then # há um virtualenv está ativo?
  echo "### - Nenhum virtualenv identificado"
  if [ ! -d $VIRTUAL_ENV_DIR ]; then
    virtualenv $VIRTUAL_ENV_DIR
  fi
else
  echo "### - Usando virtualenv em ${VIRTUAL_ENV}"
fi

echo "### - Executando virtualenv..."
source $VIRTUAL_ENV_DIR/bin/activate

echo "### - Instalando requirements do projeto"
pip install -q -r ./requirements.txt
