@echo off

rem Obtener la fecha y hora actual
set "fecha_hora=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%-%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%"

rem Descargar los datos de precio de Bitcoin
curl -s "https://api.coindesk.com/v1/bpi/currentprice/USD.json" > "precios_bitcoin_%fecha_hora%.txt"

rem Generar un gráfico con los datos
python generar_grafico.py "precios_bitcoin_%fecha_hora%.txt"

rem Mostrar un mensaje de éxito
echo "**Los datos de Bitcoin se han almacenado correctamente.**"
