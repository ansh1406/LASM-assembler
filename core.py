from gui import log_field , asmEditor, fileNameInputField

opcodes = {
"LDA": "0100",
"LDB": "0200",
"LDC": "0300",
"LDD": "0400",
"LDT": "0500",
"LRA": "0600",
"LRB": "0700",
"LRC": "0800",
"LRD": "0900",
"LRT": "0A00",
"LSA": "0B00",
"LSB": "0C00",
"LSC": "0D00",
"LSD": "0E00",
"LST": "0F00",
"SRA": "1000",
"SRB": "1100",
"SRC": "1200",
"SRD": "1300",
"SRK": "1400",
"SSA": "1500",
"SSB": "1600",
"SSC": "1700",
"SSD": "1800",
"SSK": "1900",
"MAB": "1A00",
"MAC": "1B00",
"MAD": "1C00",
"MBA": "1D00",
"MBC": "1E00",
"MBD": "1F00",
"MCA": "2000",
"MCB": "2100",
"MCD": "2200",
"MDA": "2300",
"MDB": "2400",
"MDC": "2500",
"MAK": "2600",
"MBK": "2700",
"MCK": "2800",
"MDK": "2900",
"MTA": "2A00",
"MTB": "2B00",
"MTC": "2C00",
"MTD": "2D00",
"SUM": "2E00",
"SUB": "2F00",
"MUL": "3000",
"DIV": "3100",
"MOD": "3200",
"NOT": "3300",
"AND": "3400",
"ORR": "3500",
"XOR": "3600",
"NND": "3700",
"NOR": "3800",
"CMP": "3900",
"SAV": "3A00",
"RET": "3B00",
"JMP": "3C00",
"JPA": "3D00",
"JPB": "3E00",
"JPC": "3F00",
"JPD": "4000",
"CPC": "4100",
"RBA": "4200",
"RCA": "4300",
"RDA": "4400",
"STU": "4500",
"STD": "4600",
"KBP": "4700",
"SBA": "4800",
"SCA": "4900",
"SDA": "4A00",
"CSP": "4B00",
"SUD": "4C00",
"SDD": "4D00",
"JPG": "FB00",
"JPE": "FC00",
"JPL": "FD00",
"JPZ": "FE00",
"HLT": "FF00"
}
two_arg_instructions = {
"LDA":True,
"LDB":True,
"LDC":True,
"LDD":True,
"LDT":True,
"LRA":True,
"LRB":True,
"LRC":True,
"LRD":True,
"LRT":True,
"LSA":False,
"LSB":False,
"LSC":False,
"LSD":False,
"LST":False,
"SRA":True,
"SRB":True,
"SRC":True,
"SRD":True,
"SRK":True,
"SSA":False,
"SSB":False,
"SSC":False,
"SSD":False,
"SSK":False,
"MAB":False,
"MAC":False,
"MAD":False,
"MBA":False,
"MBC":False,
"MBD":False,
"MCA":False,
"MCB":False,
"MCD":False,
"MDA":False,
"MDB":False,
"MDC":False,
"MAK":False,
"MBK":False,
"MCK":False,
"MDK":False,
"MTA":False,
"MTB":False,
"MTC":False,
"MTD":False,
"SUM":False,
"SUB":False,
"MUL":False,
"DIV":False,
"MOD":False,
"NOT":False,
"AND":False,
"ORR":False,
"XOR":False,
"NND":False,
"NOR":False,
"CMP":False,
"SAV":False,
"RET":False,
"JMP":True,
"JPA":False,
"JPB":False,
"JPC":False,
"JPD":False,
"CPC":False,
"RBA":False,
"RCA":False,
"RDA":False,
"STU":False,
"STD":False,
"KBP":False,
"SBA":False,
"SCA":False,
"SDA":False,
"CSP":False,
"SUD":False,
"SDD":False,
"JPG":True,
"JPE":True,
"JPL":True,
"JPZ":True,
"HLT":False,
}
needAddressAsSecondArg = ["LRA","LRB","LRC","LRD","LRT","SRA","SRB","SRC","SRD","SRK","JMP","JPZ","JPL","JPE","JPG"]
needDataAsSecondArg = ["LDT","LDA","LDB","LDC","LDD"]

dataBlockBaseAddress = 0

instructions = {}
currentRamHead = 0
labels = {}


def assemble():
    global dataBlockBaseAddress, currentRamHead, instructions, labels
    dataBlockBaseAddress = 0
    instructions = {}
    currentRamHead = 0
    labels = {}
    program = []
    currentLine = 1
    asm_code = " "
    while asm_code:
        asm_code = asmEditor.get(f"{currentLine}.0",f"{currentLine+1}.0")
        words = asm_code.split()
        if len(words) == 0:
            currentLine += 1
            continue
        if words[0].startswith('#'):
            currentLine += 1
            continue
        words[0] = words[0].upper()
        program.append(words)
        currentLine += 1
    
    for line in program:
        if line[0] in opcodes:
            handle_instructions(line)
        elif line[0].endswith(':'):
            handle_labels(line)
    
    dataBlockBaseAddress = currentRamHead        
    for line in program:
        if line[0][0:4] == "DATA":
            handle_data_entries(line)
        
    handle_arguments()
        
    print(instructions)
    create_binary_file()
     

def log_message(message):
    log_field.configure(state="normal")
    log_field.insert("end", message + "\n")
    log_field.configure(state="disabled")


def handle_instructions(line):
    global currentRamHead, instructions
    if two_arg_instructions[line[0]]:
        if len(line) < 2:
            log_message(f"Error: Invalid number of arguments for instruction {line[0]}")
        else:
            instructions[currentRamHead] = opcodes[line[0]]
            currentRamHead += 1
            if line[0] in needAddressAsSecondArg:
                instructions[currentRamHead] = "arg:"+("ADDR-"+line[1][5:]) if line[1][0:4].upper() == "DATA" else line[1]
            if line[0] in needDataAsSecondArg:
                instructions[currentRamHead] = "arg:"+line[1]
            currentRamHead += 1
    else:
        instructions[currentRamHead] = opcodes[line[0]]
        currentRamHead += 1
                
                
def handle_labels(line):
    global currentRamHead, labels
    label_name = line[0][:-1].upper()
    if label_name in labels:
        log_message(f"Error: Label {label_name} already exists.")
    else:
        labels[label_name] = currentRamHead
        

def handle_data_entries(line):
    global dataBlockBaseAddress
    if len(line) != 2:
        log_message(f"Error: Invalid number of arguments at line {line}")
    if line[1].startswith('-'):
        instructions[dataBlockBaseAddress + int(line[0][5:])] = hex((1 << 16) + int(line[1])).replace("0x", "").zfill(4).upper()
    else:
        instructions[dataBlockBaseAddress + int(line[0][5:])] = hex(int(line[1])).replace("0x", "").zfill(4).upper() if line[1][0] != '\'' else line[1][1].encode("ascii").hex().zfill(4)
        

def handle_arguments():
    global instructions, labels, dataBlockBaseAddress
    for instruction in instructions:
        if instructions[instruction].startswith("arg:"):
            arg = instructions[instruction][4:]
            if arg.startswith('-'):
                instructions[instruction] = hex((1 << 16) + int(arg)).replace("0x", "").zfill(4).upper()
            elif arg.startswith('\''):
                if arg[1] == '\\':
                    if arg[2] == 'n': instructions[instruction] = "000A"
                    elif arg[2] == 't': instructions[instruction] = "0009"
                    elif arg[2] == 'r': instructions[instruction] = "000D"
                    elif arg[2] == 'b': instructions[instruction] = "0008"
                else:
                    instructions[instruction] = arg[1].encode("ascii").hex().zfill(4)
            elif arg.upper() in labels:
                instructions[instruction] = hex(labels[arg.upper()]).replace("0x", "").zfill(4).upper()
            elif arg.upper().startswith("ADDR-"):
                instructions[instruction] = hex(dataBlockBaseAddress+int(arg[5:])).replace("0x", "").zfill(4).upper()
            elif arg.upper().startswith("DATA-"):
                instructions[instruction] =instructions[dataBlockBaseAddress + int(arg[5:])]
            else:
                try:
                    instructions[instruction] = hex(int(arg)).replace("0x", "").zfill(4).upper()
                except ValueError:
                    log_message(f"Error: Invalid argument {arg} for instruction at address {instruction}")
            
            
def create_binary():
    global instructions
    min_address = min(instructions.keys())
    max_address = max(instructions.keys())
    binary = bytearray()
    for address in range(min_address, max_address + 1):
        if address in instructions:
            binary.extend(bytes.fromhex(to_little_endian(instructions[address])))
        else:
            binary.extend(bytes.fromhex("0000")) 
    return binary

def to_little_endian(hexStr):
    return hexStr[2:4] + hexStr[0:2]

def create_binary_file():
    binary = create_binary()
    try:
        fileName = fileNameInputField.get()
        fileName = str.strip(fileName)
        if fileName == "":
            log_message("Invalid file name.")
            return
        if not fileName.endswith(".lm1"):
            fileName += ".lm1"
        with open(fileName, "wb") as binary_file:
            binary_file.write(binary)
        log_message(f"Binary file successfully written to {fileName}.")
    except Exception as e:
        log_message(f"Error: {str(e)}")