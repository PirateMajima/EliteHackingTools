from argparse import ArgumentParser

def hide(input):
    try:
        # Lê o arquivo em modo binário
        with open(input, 'rb') as f:
            content = f.read()

        # Converte o conteúdo para binário
        binary = ''.join(format(byte, '08b') for byte in content)

        # Substitui 0s por espaços e 1s por tabs
        converted = binary.replace('0', ' ').replace('1', '\t')
        
        return converted

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"
    
def solve(input):
    try:
        # Lê o arquivo contendo espaços e tabs
        with open(input, 'r', encoding="ascii") as f:
            content = f.read()

        # Substitui espaços por 0s e tabs por 1s
        binary = content.replace(' ', '0').replace('\t', '1')

        # Converte a string binária em bytes
        resulting_bytes = bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))

        return resulting_bytes

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"

def save_file(output, content):
    try:
        # Verifica se o conteúdo é em bytes ou string e escolhe o modo apropriado
        mode = 'wb' if isinstance(content, bytes) else 'w'
        
        with open(output, mode) as f:
            f.write(content)
        print(f"Successful save in {output}")
    except Exception as e:
        print(f"Error saving file: {str(e)}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", "--mode", type=str, help="Mode to use (Default: hide)", choices=["hide", "solve"], default="hide")
    parser.add_argument("-i", "--input", type=str, help="Input file path", required=True)
    parser.add_argument("-o", "--output", type=str, help="Output file path", required=True)
    args = parser.parse_args()

    if args.mode == "hide":
        result = hide(args.input)
        try:
            with open(args.output, "w", encoding="ascii") as f:
                f.write(result)
            print(f"Successful save in {args.output}")
        except Exception as e:
            print(f"Error saving file: {str(e)}")
    else:
        result = solve(args.input)
        try:
            with open(args.output, "wb") as f:
                if isinstance(result, bytes):
                    f.write(result)
                elif isinstance(result, str):
                    f.write(result.encode("ascii"))
            print(f"Successful save in {args.output}")
        except Exception as e:
            print(f"Error saving file: {str(e)}")