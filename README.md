# Scripts
A collection of various Python scripts for all kinds of purposes.
- [daysbetweendates.py](#days-between-dates)
- [numberstowords.py](#numbers-to-words)
- [rappernamegenerator.py](#rapper-name-generator)
- [timeconverter.py](#time-converter)
- [unitconverter.py](#unit-converter)


## Days between dates
Calculates the number of days between two dates.

### Usage
```bash
./daysbetweendates.py <date1> <date2>
```   
### Arguments:
- date1: a date written in the format 'YYYYMMDD'
- date2: a date written in the format 'YYYYMMDD'
Alternatively, you can write 'today' if referring to the current date.   

### Example:
`./daysbetweendates.py today 20200420`


## Numbers to words
Returns the English word representation of a given number.

### Usage
```bash
./numberstowords.py <number>
```   
### Arguments:
- number: a positive integer not exceeding 15 digits

### Example:
`./numberstowords.py 420` -> *four hundred and twenty*


## Rapper name generator
Randomly generates a rap name alias.   
*Any resemblance to actual rapper names is purely coincidental.*

### Usage
```bash
./rappernamegenerator.py
```

### Example:
`./rappernamegenerator.py`


## Time converter
Converts the local time in one country to the local time in another country.

### Requirements
- The [pytz](https://pypi.org/project/pytz/) module must be installed
- The `timezones.json` file provided in this repo
[(original source)](https://github.com/moment/moment-timezone/blob/develop/data/meta/latest.json)


### Usage
```bash
./timeconverter.py <command> <...command args>
```

### Commands:
- **now <country>**   
  Returns the current local time in the specified country.   
  Example:   
  `./timeconverter.py now Norway`
- **convert <time> <origin> <target>**   
  Converts the specified time in origin country to the corresponding time in the target country.   
  If the origin country has multiple timezones, the user will be asked to choose which one to use.
  Example:   
  `./timeconverter.py convert 04:20 Norway 'United States'`
- **diff <country1> <country2>**   
  Calculates the time difference between two countries.   
  If a country has multiple timezones, the user will be asked to choose which one to use.
  Example:   
  `./timeconverter.py diff Norway 'United States'`
- **countries**   
  Show a list of all available countries.   
  Example:   
  `./timeconverter.py countries`


## Unit converter
Converts a value from one measurement unit to another.

### Usage
```bash
./unitconverter.py <value> <original unit> <target unit>
```   
### Arguments:
- value: a whole or floating point number
- original unit: a date written in the format 'YYYYMMDD'
- target unit: a date written in the format 'YYYYMMDD'

List of valid units: **mm, cm, m, km, in, ft, yd, mi**

### Example:
`./unitconverter.py 4.20 cm in` -> *1.6535 in*
