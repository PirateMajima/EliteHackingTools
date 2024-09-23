# script to hide secret.pdf after the EOF of input.wav

# program is invoked as follows:
# python hide_pdf.py -h <pdf_file> <wav_file>
# -h: hide the pdf file in the wav file

import sys
import os
import wave 

def hide_pdf(pdf_file, wav_file):
    
    f1 = open(wav_file, "rb")
    f1_data =  f1.read()
    f1.close()

    f2 = open(pdf_file, "rb")
    f2_data = f2.read()
    f2.close()

    path = "output"
    # Create output directory if needed
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

    with open(path + "/" + "best-intro.wav", "wb") as out_file:
        out_file.write(f1_data)
        out_file.write(f2_data)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1] == '-h':
            hide_pdf(sys.argv[2], sys.argv[3])
        else:
            print('Invalid option')
    else:
        print('Usage: python hide_pdf.py -h <pdf_file> <wav_file>')
