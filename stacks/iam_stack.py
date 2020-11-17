from aws_cdk import aws_iam as iam, core


class IAMSTACK(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        user_password = core.SecretValue.plain_text("Newuser123")
        
        # different approach to assigning policy

        # # Approach 1 = defining the PolicyStatement and assigning it directly to user
        # policy_statement = iam.PolicyStatement(effect=iam.Effect.ALLOW)
        # policy_statement.add_actions("*")
        # policy_statement.add_all_resources()

        # # Apporach 2 = creating a policy and adding policy statements then attach this policy to a user
        # NewAdminAccess = iam.Policy(self, 'newpolicy', policy_name="NewAdminAccessForUsers")
        # NewAdminAccess.add_statements(policy_statement)

        # # Apporach 3 = create a group and define the policies/policyStatements
        # AdminGroupOfNewGen = iam.Group(self, "newgengroup", group_name="AdminGroupOfLambdas")
        # AdminGroupOfNewGen.attach_inline_policy(NewAdminAccess)

        # # Creating the iam user
        # iam_user = iam.User(self, 'newuser',
        #     user_name="newuser123", 
        #     password=user_password
        # )

        # iam_user2 = iam.User(self, 'newuser2', 
        #     user_name="jalanie123",
        #     password=user_password
        # )

        # # Approach 1 = assigning to user the policy statement
        # iam_user.add_to_policy(policy_statement)

        # # Approach 2 = assigning the created policy from approach 2 above
        # NewAdminAccess.attach_to_user(iam_user)

        # # Approach 3 = assign user to group created from approach 3 above
        # iam_user.add_to_group(AdminGroupOfNewGen)
        # iam_user2.add_to_group(AdminGroupOfNewGen)


        # # Approach 4 = assign user a permission directly from an aws managed policy
        # iam_user.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess"))


