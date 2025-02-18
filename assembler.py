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

def read():
    lst = []
    x = input("Enter input file: ")
    with open(x,'r') as f:
        for i in f:
            lst.append(i)
    return lst



read()
