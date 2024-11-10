# HEIC to PNG Converter

`heic2png.py` is a Python script that converts HEIC (High Efficiency Image Coding) files to PNG format. It supports batch processing of all HEIC files in a specified directory, with optional features to delete the original HEIC files after conversion.

## Requirements

- Python 3.x
- `pyheif` library for reading HEIC files
- `Pillow` library for image processing

You can install the required dependencies using `pip`:

```bash
pip install pyheif Pillow
```

## Usage
The script can be run from the command line with the following syntax:

```bash
python heic2png.py <input_directory> [<output_directory>] [--delete_heic]
```

### Arguments
- `input_directory`: The directory containing the HEIC files you want to convert. (Required)
- `output_directory`: The directory where the converted PNG files will be saved. If not provided, the output will be saved in the same directory as the input. (Optional)
- `--delete_heic`: A flag to delete the original HEIC files after conversion. (Optional)

## Examples
1. Convert HEIC files and save them as PNG in a specific directory:
```bash
python heic2png.py /path/to/heic_files /path/to/output_directory
```

2. Convert HEIC files and save the PNG files in the same directory:
```bash
python heic2png.py /path/to/heic_files
```

3. Convert HEIC files and delete the original HEIC files after conversion:
```bash
python heic2png.py /path/to/heic_files /path/to/output_directory --delete_heic
```

4. Convert HEIC files, save PNG files in the same directory, and delete the original HEIC files:
```bash
python heic2png.py /path/to/heic_files --delete_heic
````


## Notes
- The script will automatically create the output directory if it does not exist.
- The script will overwrite any existing PNG files with the same name in the output directory.
- If `--delete_heic` is enabled, the script will delete each HEIC file after successfully converting it to PNG.

## License
This script is released under the MIT License. See LICENSE for details.
