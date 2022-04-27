#!/bin/bash -i
conda init bash

mamba env create -f environment.yml -p $HOME/envs/ligohw6

echo ello
echo $HOME
conda env list

conda activate ligohw6

conda env list


pip install pytest

python2 -m ipykernel install --user --name ligohw6 