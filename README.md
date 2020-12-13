# option_vol_curve

## Steup
At repository root directory, run
```
virtualenv venv
activate ./venv/bin/activate (Unix)
venv/Scripts/activate (Windows)
pip install -r requirements.txt
```

## Project layout
* /src: main source code
* /tests: unit tests
* /notebook: notebooks to visualize data and see results

## Get notebooks working
### Setup Jupyter Kernel with venv
```console
activate ./venv/bin/activate (Unix)
venv/Scripts/activate (Windows)
pip install ipykernel python=3.6
python -m ipykernel install --user --name option_vol_curve --display-name "OPTION_VOL_CURVE"

```

### Install Plotly extensions
```console
activate ./venv/bin/activate (Unix)
venv/Scripts/activate (Windows)
pip install jupyterlab "ipywidgets>=7.5"
jupyter labextension install jupyterlab-plotly@4.12.0
jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.12.0
```

### Launch jupyter lab from /notebooks
```console
cd notebooks
jupyter lab
```

## Unit Tests
At repository root directory, run
```
pytest tests
```