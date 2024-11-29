def process_srt(input_file, output_file):
    try:
        print(f"Opening input file: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        print("File read successfully. Processing subtitles...")

        subtitles = []
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.isdigit() or '-->' in line or not line:
                continue
            subtitles.append(line)

        result_text = ' '.join(subtitles)

        print(f"Writing processed subtitles to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(result_text)

        print(f"Subtitle processing complete! Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
input_srt = 'input.srt'  # Ensure this file exists
output_txt = 'output.txt'  # Specify the output file
process_srt(input_srt, output_txt)
