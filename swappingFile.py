def swapfiledata():
    doc_1_name = input('Please enter the name of the first file: ')
    doc_2_name = input('Please enter the name of the second file: ')

    with open(doc_1_name, 'r') as a:
        doc_1 = a.read()
    with open(doc_2_name, 'r') as b:
        doc_2 = b.read()

    with open(doc_1_name, 'w') as a:
        a.write(doc_2)
    with open(doc_2_name, 'w') as b:
        b.write(doc_1)

swapfiledata()
print('The data in both the files have been swapped!')