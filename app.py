#!/usr/bin/env python3

from aws_cdk import core

from stacks.iam_stack import IAMSTACK


app = core.App()
IAMSTACK(app, "IAM")

app.synth()
