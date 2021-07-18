resource "aws_security_group" "vpc_endpoint" {
  name        = "ses_vpc_endpoint"
  description = "Allow TLS inbound traffic for VPC ses_endpoint"
  vpc_id      = var.vpc_id

  ingress {
    description = "TLS from VPC"
    from_port   = 25
    to_port     = 25
    protocol    = "tcp"
    cidr_blocks = [var.cidr_blocks]
  }

  ingress {
    description = "TLS from VPC"
    from_port   = 465
    to_port     = 465
    protocol    = "tcp"
    cidr_blocks = [var.cidr_blocks]
  }

  ingress {
    description = "TLS from VPC"
    from_port   = 587
    to_port     = 587
    protocol    = "tcp"
    cidr_blocks = [var.cidr_blocks]
  }

  ingress {
    description = "TLS from VPC"
    from_port   = 2465
    to_port     = 2465
    protocol    = "tcp"
    cidr_blocks = [var.cidr_blocks]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ses_vpc_endpoint"
  }
}

resource "aws_vpc_endpoint" "ses_endpoint" {
  vpc_id            = var.vpc_id
  service_name      = var.smtp_service_name
  vpc_endpoint_type = "Interface"

  security_group_ids = [
    aws_security_group.vpc_endpoint.id,
  ]

  subnet_ids          = [var.subnet_id1, var.subnet_id2]
  private_dns_enabled = true
}
