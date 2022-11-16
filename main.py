def fileWriter():
    result = 0
    with open('input.txt') as fr:
        data = fr.read().split()
        n1 = int(data[0])
        n2 = int(data[1])
        with open('output.txt','w') as fw:
            fw.write(str(n1 + n2))



def main():
    fileWriter()

if __name__ == '__main__':
    main()