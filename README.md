MJO Indices Script
==================

This Python script retrieves and parses [Madden-Julian Oscillation](https://en.wikipedia.org/wiki/Madden%E2%80%93Julian_oscillation) [Wheeler-Hendon Index](http://journals.ametsoc.org/doi/abs/10.1175/1520-0493%282004%29132%3C1917%3AAARMMI%3E2.0.CO%3B2) values from the Australian [Bureau of Meteorology (BOM)](http://www.bom.gov.au/).

Functions
---------

### `load_indices()`

This is a meta-function that runs all functions in the script: retrieving, parsing, and extracting indices from the BOM site.

The output is a two-dimensional matrix with each row containing the year, julian day, phase, and amplitude.

### `_retrieve()`

This function fetches the indices file from the BOM and returns its text.

### `_parse(data)`

This function takes the text output from `_retrieve()`, removes the header information, and parses the data.

The output is a two-dimensional matrix with each row containing the year, month, day, first EOF magnitude, second EOF magnitude, phase, amplitude, and note for each day. Missing values are set to 999.

### `_extract(data)`

This function takes the output from `_parse()` and returns only certain information.

The output is a two-dimensional matrix with each row containing the year, julian day, phase, and amplitude.
