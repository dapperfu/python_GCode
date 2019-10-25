import datetime
import re
import uuid
from typing import List

import numpy as np


class GCode:
    """GCode class for programatically generating a GCode"""

    # NewLine to use

    def __init__(
        self,
        file: str = None,
        machine=None,
        name: str = None,
        buffer: List[str] = list(),
    ):
        self.buffer: List[str] = list()
        if file is not None:
            self.load(file)
        # Extend the existing buffer with the given buffer.
        self.buffer.extend(buffer)
        # Set the machine.
        self.machine = machine
        # Program Name
        self.name = name

    @property
    def code(self):
        # If a child class has a generate gcode function
        if hasattr(self, "generate_gcode"):
            # Execute it.
            getattr(self, "generate_gcode")()
        # Return just the code.
        return "\n".join(self.buffer)

    def load(self, filename: str):
        """Load a given filename to the GCode program buffer."""
        with open(filename, "r") as fid:
            data = fid.read()
        # For a line in each line in the given file
        for line in data.splitlines():
            # Split the file by comments:
            # Mach3: ()
            # Siemens: ;
            line = line.split("(")[0].split(";")[0].strip()
            # If the line is empty
            if len(line) == 0:
                # Skip it.
                continue
            # Otherwise add it to the buffer.
            self.buffer.append(line)

    def save(self, filename):
        """ Save the

        """
        with open(filename, "w") as fid:
            if self.name is not None:
                print(f"; Program Name: {self.name}")
            print(f"; Program UUID: {uuid.uuid4()}")
            print(f"; Save Date: {datetime.datetime.utcnow().isoformat()}")
            print(str(self), file=fid)

    def __str__(self):
        return self.code

    def __repr__(self):
        if hasattr(self, "generate_gcode"):
            getattr(self, "generate_gcode")()
        return "<GCode>[cmds={}]".format(len(self.buffer))

    def _repr_html_(self):
        if hasattr(self, "generate_gcode"):
            getattr(self, "generate_gcode")()
        html = list()
        for cmd_line in self.buffer:
            html_line = ""
            for match in re.compile(r"([\w])([\d.]+)").findall(str(cmd_line)):
                html_line += f"<b>{match[0]}</b>{match[1]}"
            html.append(html_line)
        return "<br>\n".join(html)

    def __add__(self, other):
        """Add GCode programs to:
        - Other GCode programs
        - List of GCode commands,
        - String of GCode commands"""
        # Before adding the objects
        # If either has a generate_gcode()
        if hasattr(self, "generate_gcode"):
            getattr(self, "generate_gcode")()
        if hasattr(other, "generate_gcode"):
            getattr(other, "generate_gcode")()

        if isinstance(other, list):
            buffer2 = other
        elif isinstance(other, str):
            buffer2 = other.splitlines()
        elif hasattr(other, "buffer"):
            buffer2 = other.buffer
        else:
            raise Exception(f"{type(other)}:\n{other}")
        return self.buffer.extend(buffer2)

    def __iter__(self):
        """ __iter__ function """
        for i in range(len(self.buffer)):
            yield (self.buffer[i])

    def run(self):
        """ run the program on the given machine """
        if self.machine is None:
            raise Exception("No machine to run on")
        self.machine.run(self)

    def optimise(self):
        """ Create the best GCode possible. """
        raise (NotImplementedError("TODO:"))


numeric_types = (
    int,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.float,
    np.float16,
    np.float32,
    np.float64,
    np.float128,
)


def cmd_factory(cmd, doc=None):
    """ Factory to create GCode Command Functions. """

    def cmd_fcn(self, **kwargs):
        f""" {cmd}:"""
        args = list()

        # Loop through each of the given arguments
        for key, value in kwargs.items():
            # If the value is a known numeric type
            if isinstance(value, numeric_types):
                # Cast to a float
                value = np.float(value)
                # Round the value
                value = np.round(value, decimals=4)
            # Add the args to the command line.
            args.append(f"{key}{value}")
        # Join the list of arguments into a string.
        arg_str = "".join(args)
        # Join the command with the command arguments.
        cmd_str = f"{cmd}{arg_str}"
        # For commands with no arguments.
        cmd_str = cmd_str.strip()
        # Append the command string to the buffer.
        self.buffer.append(cmd_str)

    return cmd_fcn


# Good core to start with.
commands = list()
# GCodes
for code in [0, 1, 2, 3, 4, 20, 21, 28, 90, 91, 92]:
    commands.append(f"G{code}")
# MCodes
for code in [0, 1, 2, 3, 4, 5, 6]:
    commands.append(f"M{code}")

for command in commands:
    setattr(GCode, command, cmd_factory(command))
