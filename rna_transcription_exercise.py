def to_rna(dna_strand):
    dna_yes = ("A","C","G","T")
    rna_yes = ("A","C","G","U")

    new = []

    try:
        for char in dna_strand:
            if char in dna_yes:
                if char == "A":
                    new.append("U")

                elif char == "C":
                    new.append("G")

                elif char == "G":
                    new.append("C")

                elif char == "T":
                    new.append("A")       
            else:
                raise ValueError("Invalid DNA strand")

    except ValueError:
        print("sorry try again")
        
        
    return("".join(new))