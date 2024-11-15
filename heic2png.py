import os
import argparse
from PIL import Image
import pyheif

def convert_heic_to_png(heic_file, output_folder):
    try:
        # Open HEIC file using pyheif
        heif_file = pyheif.read(heic_file)
        
        # Convert to a Pillow Image object
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # Create a PNG file name
        base_name = os.path.basename(heic_file)
        png_file = os.path.join(output_folder, f"{os.path.splitext(base_name)[0]}.png")
        
        # Save as PNG (overwrites the existing file)
        image.save(png_file, "PNG")
        
        return png_file
    except Exception as e:
        print(f"Error converting {heic_file}: {e}")
        return None

def convert_all_heic_in_directory(input_directory, output_directory, delete_heic=False):
    # Check if the input directory exists
    if not os.path.isdir(input_directory):
        print(f"Error: The directory {input_directory} does not exist.")
        return
    
    # List all HEIC files in the input directory
    heic_files = [f for f in os.listdir(input_directory) if f.lower().endswith(".heic")]
    
    if not heic_files:
        print("No HEIC files found in the specified directory.")
        return

    # Total number of HEIC files
    total_files = len(heic_files)

    # Create output folder for PNG files if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Iterate over the HEIC files and convert them
    for idx, heic_file in enumerate(heic_files, start=1):
        heic_file_path = os.path.join(input_directory, heic_file)
        
        # Convert the HEIC file and overwrite existing PNG
        output_file = convert_heic_to_png(heic_file_path, output_directory)
        
        if output_file:
            # Print the progress (x/total - %done)
            print(f"\rConverting {heic_file} to {output_file} ({idx}/{total_files})", end='')

            # If delete_heic is True, delete the original HEIC file
            if delete_heic:
                try:
                    os.remove(heic_file_path)
                    # print(f" - Deleted {heic_file}", end='')
                except Exception as e:
                    print(f" - Error deleting {heic_file}: {e}", end='')

    # Show a message when conversion is completed
    print(f"\nConversion completed!")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Convert HEIC files to PNG format with overall progress.")

    # Add command-line arguments for input and output directories
    parser.add_argument("input_directory", help="Directory containing HEIC files to convert.")
    parser.add_argument("output_directory", nargs="?", help="Directory where PNG files will be saved.")
    
    # Add the --delete_heic flag (optional)
    parser.add_argument("--delete_heic", action="store_true", help="Delete the original HEIC files after conversion.")
    
    # Parse the arguments
    args = parser.parse_args()

    # If no output directory is provided, use the input directory as the output directory
    if not args.output_directory:
        args.output_directory = args.input_directory

    # Convert HEIC files to PNG in the specified directories, and delete HEIC files if the flag is set
    convert_all_heic_in_directory(args.input_directory, args.output_directory, delete_heic=args.delete_heic)

if __name__ == "__main__":
    main()
