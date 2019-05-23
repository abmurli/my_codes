variable "cluster_name" {
  description = "The name of the redis cluster"
  default     = ""
}

variable "engine" {
  description = "Engine type"
  default     = "redis"
}

variable "engine_version" {
  description = "Engine version compatibility"
  default     = "5.0.4"
}

variable "node_type" {
  description = "Type of the node"
  default     = "cache.r5.large"
}

variable "parameter_group_name" {
  description = "Parameter group name"
  default     = ""
}

variable "subnet_id1" {
  description = "Subnet id to be associated with the redis cluster"
  default     = ""
}

variable "sg1" {
  description = "Security group id"
  default     = ""
}
