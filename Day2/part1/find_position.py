import commands


def parse_command_string(command):
    parsed_command = command.split(" ")
    parsed_command[1] = int(parsed_command[1])
    return parsed_command


def forward(position, coordinate):
    position["x"] += coordinate


def up(position, coordinate):
    position["z"] += coordinate


def down(position, coordinate):
    position["z"] -= coordinate


operations = {
    "forward": forward,
    "up": up,
    "down": down
}


def crawler(commands):
    position = {"x": 0, "z": 0}
    for command in commands:
        [movement, coordinate] = parse_command_string(command)
        operations[movement](position, coordinate)
    return position["x"] * position["z"] * -1


print(crawler(commands.commands))
