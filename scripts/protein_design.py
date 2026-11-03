import random

def get_sequence_count():
    while True:
        user_input = input("Please indicate how many random protein sequences you need (1-1000)? ")

        #Check that the input contains only digits
        if user_input.isdigit():
            count = int(user_input)

            #Make sure the number is between 1 and 1000
            if 1 <= count <= 1000:
                return count

        #Display an error message if the input is invalid
        print("Error: Please enter an integer between 1 and 1000.")

def generate_protein():
    #Define the amino acid groups according to their chemical properties
    nonpolar = list("AVLIPFMWGC") * 7 + ["A"] * 4
    polar = list("NQSTY") * 9
    positive = list("KRH") * 5
    negative = list("DE") * 7 + ["D"]

    #Combine all amino acids to create the required composition
    amino_acids = nonpolar + polar + positive + negative

    #Randomly shuffle the amino acids
    random.shuffle(amino_acids)

    #Add methionine as the first amino acid and return the sequence
    return "M" + "".join(amino_acids)

def main():
    #Get the number of sequences requested by the user
    count = get_sequence_count()

    #Create a list to store the generated sequences
    sequences = []
    #Create a set to keep track of previously generated sequences
    seen = set()

    #Generate unique protein sequences until the requested number is reached
    while len(sequences) < count:
        sequence = generate_protein()

        #Add the sequence only if it has not been generated before
        if sequence not in seen:
            sequences.append(sequence)
            seen.add(sequence)

    with open("results/Out_RandProtSeq.txt", "w") as output_file:
        for i, sequence in enumerate(sequences, start=1):
            output_file.write(f">Rand_Prot{i}\n")
            output_file.write(sequence + "\n")

    print(count, "protein sequences generated successfully!")

#Run the main function when the script is executed
if __name__ == "__main__":
    main()