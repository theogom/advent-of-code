output "dial" {
  value = length(var.list) == 0 ? var.dial : module.next[0].dial
}