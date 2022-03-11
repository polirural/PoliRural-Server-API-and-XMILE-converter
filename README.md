# Pysd Polirural Server

## Server application for SD-models in the Polirural Project

```bash
conda activate pysd2
python app.py

```

## Cleaner application for XMILE-files exported from Stella Architect / iSee

```bash
conda activate pysd2
```

Original files are stored in the folder xmile/originals

Place files to be converted directly in the folder xmile

Do conversions like this

```bash
python converter.py "xmile\Galilee_v2.xmile"
```

This will clean the file and place a copy in "xmile/cleaned"

It will also create the final version in a folder called "xmile/processed"

Copy generated model files from here to /models

Add to model configuration client app to make available for end users

## Update Pysd version

This assumes the same setup as on the development environment, i.e. pysd being hosted in a parallel folder

```cmd
install-pysd.bat
```