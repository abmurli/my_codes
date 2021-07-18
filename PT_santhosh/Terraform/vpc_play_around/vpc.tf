data "aws_vpcs" "vpc" {
}

data "aws_vpc" "vpc1" {
  count = length(data.aws_vpcs.vpc.ids)
  id    = tolist(data.aws_vpcs.vpc.ids)[count.index]
}

data "aws_vpc" "vpc2" {
  for_each = data.aws_vpcs.vpc.ids
  # id    = tolist(data.aws_vpcs.vpc.ids)[count.index]
}

data "aws_subnet_ids" "subnet" {
  vpc_id = data.aws_vpc.vpc1[0].id
}

data "aws_subnet" "subnet1" {
  for_each = data.aws_subnet_ids.subnet.ids
  id       = each.value
}


output "vpc" {
  value = data.aws_vpc.vpc1[0].id
}

output "vpc1" {
  value = data.aws_vpc.vpc2
}

output "subnet" {
  value = tolist(data.aws_subnet_ids.subnet.ids)
}

output "subnet1" {
  value = data.aws_subnet.subnet1
}

# resource "aws_route53_record" "www-live" {
#   zone_id = aws_route53_zone.primary.zone_id
#   name    = ""
#   type    = "CNAME"
#   ttl     = "5"
#   records        = [""]
# }
