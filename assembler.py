r_type_instructions = {
    "add": {"funct7": "0000000", "funct3": "000", "opcode": "0110011"},
    "sub": {"funct7": "0100000", "funct3": "000", "opcode": "0110011"},
    "slt": {"funct7": "0000000", "funct3": "010", "opcode": "0110011"},
    "srl": {"funct7": "0000000", "funct3": "101", "opcode": "0110011"},
    "or": {"funct7": "0000000", "funct3": "110", "opcode": "0110011"},
    "and": {"funct7": "0000000", "funct3": "111", "opcode": "0110011"}
}

i_type_instructions = {
    "lw": {"funct3": "010", "opcode": "0000011"},
    "addi": {"funct3": "000", "opcode": "0010011"},
    "jalr": {"funct3": "000", "opcode": "1100111"}
}

s_type_instructions = {
    "sw": {"funct3": "010", "opcode": "0100011"}
}

b_type_instructions = {
    "beq": {"funct3": "000", "opcode": "1100011"},
    "bne": {"funct3": "001", "opcode": "1100011"},
    "blt": {"funct3": "100", "opcode": "1100011"}
}

j_type_instructions = {
    "jal": {"opcode": "1101111"}
}

register = {
    'zero': '00000',
    'ra':   '00001',
    'sp':   '00010',
    'gp':   '00011',
    'tp':   '00100',
    't0':   '00101',
    't1':   '00110',
    't2':   '00111',
    's0':   '01000',
    's1':   '01001',
    'a0':   '01010',
    'a1':   '01011',
    'a2':   '01100',
    'a3':   '01101',
    'a4':   '01110',
    'a5':   '01111',
    'a6':   '10000',
    'a7':   '10001',
    's2':   '10010',
    's3':   '10011',
    's4':   '10100',
    's5':   '10101',
    's6':   '10110',
    's7':   '10111',
    's8':   '11000',
    's9':   '11001',
    's10':  '11010',
    's11':  '11011',
    't3':   '11100',
    't4':   '11101',
    't5':   '11110',
    't6':   '11111',
}

def read_instructions(filename="input2.txt"):
    instructions = []
    labels = {}

    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f):
                line = line.strip()

                label = None
                if ':' in line:
                    label, line = line.split(':', 1)
                    label = label.strip()
                    line = line.strip()
                    labels[label] = line_num
                
                if not line:
                    continue  

                parts = line.replace(',', ' ').replace(')', " ").replace('(', " ").split()
                instructions.append(parts)

        return instructions, labels

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
        return [], {}

def to_twos_complement(value, bit_width):
    
    if value >= 0:
        binary_representation = format(value, '0{}b'.format(bit_width))
    else:
        binary_representation = format((1 << bit_width) + value, '0{}b'.format(bit_width))
    return binary_representation

def encode_r_type(instruction, rd, rs1, rs2):
    
    funct7 = r_type_instructions[instruction]["funct7"]
    funct3 = r_type_instructions[instruction]["funct3"]
    opcode = r_type_instructions[instruction]["opcode"]
    
    rd= register[rd]
    rs1= register[rs1]
    rs2= register[rs2]
    
    binary_instruction = funct7 + rs2 + rs1+ funct3 + rd+ opcode
    
    return binary_instruction

def encode_i_type(instruction, rd, rs1, imm):
        funct3 = i_type_instructions[instruction]["funct3"]
        opcode = i_type_instructions[instruction]["opcode"]
        
        rd = register[rd]
        rs1= register[rs1]
        imm=to_twos_complement(int(imm), 12)
        
        binary_instruction = imm[0:12]+ rs1+ funct3 + rd + opcode
        
        return binary_instruction




def encode_s_type(instruction, rs1, rs2, imm):
    
    funct3 = s_type_instructions[instruction]["funct3"]
    opcode = s_type_instructions[instruction]["opcode"]

    rs1= register[rs1]
    rs2= register[rs2]
    imm=to_twos_complement(int(imm), 12)


    binary_instruction = imm[0:7] + rs2+ rs1+ funct3 + imm[7:11] + opcode

    return binary_instruction


def encode_j_type(instruction, rd, imm):

    
    opcode = j_type_instructions[instruction]["opcode"]
    rd = register[rd]
    imm = to_twos_complement(int(imm), 21)
    binary_instruction = imm[0:20] + rd + opcode
    return binary_instruction

def encode_b_type(instruction, rd, rs1, val, label, counter):
    funct3 = b_type_instructions[instruction]["funct3"]
    opcode = b_type_instructions[instruction]["opcode"]

    rd_bin = register[rd]
    rs1_bin = register[rs1]

    if val in label:
        imm = (to_twos_complement(int(label[val]) - int(counter), 13))
    else:
        imm = (to_twos_complement(int(val), 13))

    imm_12 = imm[0]
    imm_10_5 = imm[2:8]
    imm_4_1 = imm[8:12]
    imm_11 = imm[1]

    binary_instruction = imm_12 + imm_10_5 + rs1_bin + rd_bin + funct3 + imm_4_1 + imm_11 + opcode
    
    return binary_instruction

def main():
    instructions, labels = read_instructions()
    for counter, instr in enumerate(instructions):
        if not instr:
            continue
        
        instruction = instr[0]
        if instruction in r_type_instructions and len(instr) == 4:
            _, rd, rs1, rs2 = instr
            print(encode_r_type(instruction, rd, rs1, rs2))
        
        elif instruction in i_type_instructions and len(instr) == 4:
            _, rd, rs1, imm = instr
            print(encode_i_type(instruction, rd, rs1, imm))
        
        elif instruction in s_type_instructions and len(instr) == 4:
            _, rs2, imm, rs1 = instr
            print(encode_s_type(instruction, rs1, rs2, imm))
        
        elif instruction in b_type_instructions and len(instr) == 4:
            _, rs1, rs2, val = instr
            print(encode_b_type(instruction, rs1, rs2, val, labels, counter))
        
        elif instruction in j_type_instructions and len(instr) == 3:
            _, rd, imm = instr
            print(encode_j_type(instruction, rd, imm))
        
        else:
            print(f"Error: Unknown or incorrectly formatted instruction {instr}")

if __name__ == "__main__":
    main()

