import os

def split_file_into_chunks(file, num_chunks=3):
    # Read the file content
    with open(file, 'r', encoding='ascii') as f:
        content = f.read()
    
    # Calculate the size of each chunk
    chunk_size = len(content) // num_chunks
    chunks = [content[i*chunk_size:(i+1)*chunk_size] for i in range(num_chunks)]
    
    # Add the remainder to the last chunk, if any
    if len(content) % num_chunks != 0:
        chunks[-1] += content[num_chunks*chunk_size:]
    
    return chunks

def save_chunks_to_files(chunks):
    # Create 'chunks' directory if it doesn't exist
    if not os.path.exists('chunks'):
        os.makedirs('chunks')
    
    # Output file names with directory
    file_names = [os.path.join('chunks', f"chunk_{i+1}.txt") for i in range(len(chunks))]
    
    # Save each chunk to its respective file
    for i, chunk in enumerate(chunks):
        with open(file_names[i], 'w', encoding='ascii') as f:
            f.write(chunk)
        print(f"Chunk {i+1} saved to {file_names[i]}.")

def main(input_file):
    # Split the content of the file into 3 chunks
    chunks = split_file_into_chunks(input_file, num_chunks=3)
    
    # Save the chunks to files inside the 'chunks' directory
    save_chunks_to_files(chunks)

# Example usage:
input_file = "FileNotFound.txt"
main(input_file)
