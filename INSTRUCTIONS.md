
```bash
# Optionally create virtual environment and activate it
# python -m venv env 
# source env/bin/activate
sudo apt install python3-pip
pip3 install streamlit
python -m site # --user-base flag optional
streamlit hello # Test streamlit
streamlit run appy.py # Run actual streamlit app
```

OR

```bash
sudo apt install python3-pip
pip3 install pipenv
pipenv shell
pipenv install streamlit # Keep local $PATH intact
streamlit hello # Test streamlit
streamlit run appy.py # Run actual streamlit app
```
