# Komikcast-Rest-Api

This repo is a rest-api which is scraping to the [komikcast](https://komikcast.com) website and made up using Flask.

## Demo
[Click to show preview](https://komikcast-rest-api.herokuapp.com/)

## Installation

Use the package manager [npm](https://npmjs.com/) to install SRA's package.

* Clone the Repo
* Create the environment first
```bash
python -m venv env
```
* Activate the environment
```bash
env\Scripts\activate.bat
```
* Install all library needed to environment by using command
```bash
pip install -r requirements.txt
```


## Usage

* (For Windows) set the flask app
```bash
set FLASK_APP=app.py
```
* Start server with command:
```bash
python -m flask run
```

Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Endpoint

| Url        | Params           | Type |
| ------------- |:-------------:| :-----:| 
| /      | page | Number | 
| /daftar-komik  | page | Number | 
| /project-list  | page | Number | 
| /komik-tamat  | page | Number | 
| /jadwal-update  | - | - | 
| /komik  | id | String | 
| /chapter  | id | String | 




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2020-present, Ahmad Khamdani (rizalord)
