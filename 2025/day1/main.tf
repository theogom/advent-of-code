locals {
    input = file("../inputs/input1.txt")
    lines = split("\n", local.input)
    absolute_rotations = [
        for line in local.lines : [
            substr(line, 0, 1) == "L" ? -1 : 1,
            tonumber(substr(line, 1, length(line) - 1))
        ]
    ]
    rotations = [
        for rotation in local.absolute_rotations : (
            rotation[0] * rotation[1]
        )
    ]
}

locals {
    iteration_count = length(local.rotations)

    init = <<EOT
    {
        password = 0,
        dial = 50
    }
    EOT
    math = <<EOT
    {
        password = local.dial == 0 ? local.password + 1 : local.password,
        dial = local.dial + x < 0 ? 99 + local.dial + x : local.dial + x > 99 ? local.dial + x - 99 : local.dial + x
    }
    EOT
    code = join("", flatten([
        "$${jsonencode(",
        "{ for local in {\"\"= ${local.init} } : \"output\" => ",
        [ for index in range(0, local.iteration_count) : "{ for local in {\"\"= merge(local, { x = 4 } )} : \"output\" => "],
        "local",
        [for index in range(0, local.iteration_count) : "}.output"],
        "}.output",
        ")}",
    ]))
}



# output "output" {
#     # value = jsondecode(templatestring(local.code, {}))
#     value = local.rotations
# }

output "code" {
    value = local.code
}