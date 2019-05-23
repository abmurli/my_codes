resource "aws_elasticache_security_group" "redis_sg" {
  name                 = "elasticache-security-group"
  security_group_names = ["${var.sg1}"]
}

resource "aws_elasticache_subnet_group" "redis_subnet_group" {
  name       = "elasticache-subnet-group"
  subnet_ids = ["${var.subnet_id1}"]
}

resource "aws_elasticache_replication_group" "redis_cluster" {
  replication_group_id          = "redis-cluster"
  replication_group_description = "description"
  engine                        = "${var.engine}"
  engine_version                = "${var.engine_version}"
  availability_zones            = ["${var.az1}"]
  node_type                     = "${var.node_type}"
  port                          = 6379
  subnet_group_name             = "${aws_elasticache_subnet_group.redis_subnet_group.name}"
  parameter_group_name          = "${var.parameter_group_name == "" ? "default.redis5.0" : var.parameter_group_name}"
  security_group_ids            = ["${aws_elasticache_security_group.redis_sg.id}"]
  automatic_failover_enabled    = true

  cluster_mode {
    replicas_per_node_group = 3
    num_node_groups         = 1
  }
}

resource "aws_elasticache_cluster" "replica" {
  count                 = 1
  cluster_id            = "${var.cluster_name}"
  replication_group_id  = "${aws_elasticache_replication_group.redis_cluster.id}"
}
