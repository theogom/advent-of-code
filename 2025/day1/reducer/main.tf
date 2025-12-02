locals {
    is_empty = length(var.list) == 0
}

locals {
    current = local.is_empty ? 0 : var.list[0]
    next_dial = var.dial + local.current
}

module "next" {
    source = "../reducer"
    list = local.is_empty ? [] : slice(var.list, 1, length(var.list))
    dial = local.next_dial
    password = 0

    count = local.is_empty ? 0 : 1
}