## Dependencies

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__: 

    Using conda
	```bash
	conda create --name drlnd python=3.6
	conda activate drlnd
	```
    Using virtualenv and virtualenvwrapper
	```bash
	mkvirtualenv drld -p python3.6
    workon drld
	```
2. Install dependencies
    ```bash
    git clone https://github.com/udacity/Value-based-methods.git
    cd Value-based-methods/python
    pip3 install .
    ```
3. Install kernel for jupyter notebook
    ```bash
    python3 -m ipykernel install --user --name drlnd --display-name "drlnd"
    ```
4. Start jupyter notebook
    ```bash
    jupyter notebook --ip 0.0.0.0 --port 8.8.8.8
    ```
    After running the commandline above, a new notebook will appear then you select "drlnd" kernel

## Algorithm
- Step 1: At the starting step, I will try with a neural network with different number of hidden layers, with the number of nodes on each layer increased power of 2 with previous nodes on previous layer.

