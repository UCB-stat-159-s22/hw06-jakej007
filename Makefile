# Make environment 
.PHONY : env
env :
	#chmod a+x make_scripts/envsetup.sh
	#bash -ic make_scripts/envsetup.sh
	
	mamba env create -f environment.yml -p ~/envs/ligo
	
	bash -ic 'conda activate ligo;mamba env update --file environment.yml --prune'
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython - ligo"'

# Build JupyterBook locally
.PHONY : html
html :
	chmod a+x make_scripts/bookgen.sh
	bash -ic make_scripts/bookgen.sh


# Build JupyterBook via URL Hub proxy
.PHONY : html-hub
html-hub :
	pip install ghp-import
	ghp-import -n -p -f _build/html


# Clean 
.PHONY : clean
clean :
	rm -r figures/*
	rm -r audio/*
	rm -rf _build