import datetime, pytest
from ad_leavers.models.data_classes.user import User

class TestUser:

    testdata = [
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            "sam_account_name=eren.yeager,common_name=eren yeager,user_account_control=512,display_name=Eren Yeager,email=None,description=['10/25/2022'],member_of=['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],user_principal_name=eren.yeager@checkoutaws.local,account_expires=None,is_disabled=False,name=Eren Yeager,when_created=2022-01-15 17:25:18+00:00,distinguished_name=CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local"    
        )
    ]
    @pytest.mark.parametrize("schema,expected_result", testdata)
    def test_str_method(self, schema, expected_result):
        
        # * Arrange
        user = User(schema=schema)

        # * Act
        try:
            
            result = user.__str__()
            print(f"res: {result}")
        except Exception as e:

            result = str(e)

        # * Assert
        assert result == expected_result

    testdata = [
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'sAMAccountName': 'eren.yeager',    
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'sAMAccountName': 'eren.yeager',    
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 514,
                }
            },
            True
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2023, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 66048,
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'cn': 'eren yeager',
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 10, 23, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 66050,
                }
            },
            True
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'cn': 'eren yeager',
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 2, 23, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 2,
                }
            },
            True
        ),
    ]
    @pytest.mark.parametrize("schema,expected_result", testdata)
    def test_is_disabled(self, schema, expected_result):
        
        # * Arrange
        user = User(schema=schema)

        # * Act
        try:
            
            result = user.is_disabled

        except Exception as e:

            result = str(e)

        # * Assert
        assert result == expected_result

    testdata = [
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'sAMAccountName': 'eren.yeager',    
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'sAMAccountName': 'eren.yeager',    
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 514,
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2023, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'cn': 'eren yeager',
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 10, 23, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 514,
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'cn': 'eren yeager',
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 2, 23, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            True
        ),
    ]
    @pytest.mark.parametrize("schema,expected_result", testdata)
    def test_is_eligible_to_disable(self, schema, expected_result):
        
        # * Arrange
        user = User(schema=schema)

        # * Act
        try:
            
            result = user.is_eligible_to_disable()

        except Exception as e:

            result = str(e)

        # * Assert
        assert result == expected_result

    testdata = [
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            # * Account doesn't have an expiration and account is active
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 514,
                }
            },
            # * Account doesn't have an expiration and account is enabled
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2023, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            # * Account has an expiration date that has not been reached yet and account is enabled
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 512,
                }
            },
            # * Account has an expiration date that has been reached and account is enabled
            True
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'cn': 'eren yeager',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                    'userAccountControl': 514,
                }
            },
            # * Account has an expiration date that has been reached and account is disabled
            True
        ),
    ]
    @pytest.mark.parametrize("schema,expected_result", testdata)
    def test_is_eligible_for_deletion(self, schema, expected_result):
        
        # * Arrange
        user = User(schema=schema)

        # * Act
        try:
            
            result = user.is_eligible_for_deletion(days_limit=90)

        except Exception as e:

            result = str(e)

        # * Assert
        assert result == expected_result