# SKC_unit_converter

CLI temperature and fuel consumption converter developed with unit testing

Sub 0K temperatures are not flagged as erronous or corrected

# Help

-h<br />
displays this message = '-h' ;

-t<br />
temperature conversion = '-t' 'c'|'f'|'k','c'|'f'|'k' value ; 

-fc<br />
fuel consumption conversion = '-fc' 'uk_mpg'|'us_mpg'|'l100km','uk_mpg'|'us_mpg'|'l100km' value ; 

example: python unit_converter.py -t cc -40
