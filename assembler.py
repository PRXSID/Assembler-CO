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

def to_twos_complement(value, bit_width):
    
    if value >= 0:
        binary_representation = format(value, '0{}b'.format(bit_width))
    else:
        binary_representation = format((1 << bit_width) + value, '0{}b'.format(bit_width))
    return binary_representation

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

def encode_r_type(instruction, rd, rs1, rs2):
    
    funct7 = r_type_instructions[instruction]["funct7"]
    funct3 = r_type_instructions[instruction]["funct3"]
    opcode = r_type_instructions[instruction]["opcode"]
    
    rd_bin = register[rd]
    rs1_bin = register[rs1]
    rs2_bin = register[rs2]
    
    binary_instruction = funct7 + rs2_bin + rs1_bin + funct3 + rd_bin + opcode
    
    return binary_instruction


