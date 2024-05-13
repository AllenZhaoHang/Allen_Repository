def main():
    '''Read numbers from input file, calculate the sum, and write the sum to the output file'''
   # Read numbers from the input file
    with open('input.txt', 'r') as input_file:
        numbers = [int(line.strip()) for line in input_file]

    # Calculate the sum of the numbers
    total = sum(numbers)

    # Write the sum to the output file
    with open('output.txt', 'w') as output_file:
        output_file.write(str(total))


if __name__ == '__main__':
    main()
