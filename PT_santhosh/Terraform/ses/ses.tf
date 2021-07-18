resource "aws_iam_user" "user" {
  name = var.user_name
  path = "/"
}

resource "aws_iam_user_policy" "policy" {
  name = "ses_user_policy"
  user = aws_iam_user.user.name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ses:SendRawEmail",
      "Resource":"*"
    }
  ]
}
EOF
}

resource "aws_iam_access_key" "access_key" {
  user = aws_iam_user.user.name
}

output "secret" {
  value = aws_iam_access_key.access_key.encrypted_secret
}

output "aws_iam_smtp_password_v4" {
  value = aws_iam_access_key.access_key.ses_smtp_password_v4
}
output "aws_iam_smtp_user_v4" {
  value = aws_iam_access_key.access_key.id
}
