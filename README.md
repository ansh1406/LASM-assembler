# LASM Assembler

A graphical assembler for the Lancelot M1 architecture.

## Features
- Write, assemble, and save assembly code for the Lancelot M1
- GUI built with Tkinter and CustomTkinter
- Supports labels, data blocks, and instruction argument handling
- Generates binary files for Lancelot-m1 hardware simulation and Lancelot-m1 Emulator

## Requirements
- Python 3.x
- customtkinter

Install dependencies with:
```
pip install -r requirements.txt
```

## Usage
1. Run the assembler:
   ```
   python assembler.py
   ```
2. Use the GUI to write or open assembly code.
3. Click the "Assemble" button to generate machine code.
4. Save the output as a `.lm1` binary file.

## File Structure
- `assembler.py` - Main entry point, connects GUI and core logic
- `core.py` - Assembler logic and binary generation
- `gui.py` - GUI components and event bindings
- `utils.py` - Utility functions (file dialogs, logging, etc.)
- `requirements.txt` - Python dependencies
