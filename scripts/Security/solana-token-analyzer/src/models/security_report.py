class SecurityReport:
    def __init__(self, mint_authority=None, freeze_authority=None, upgradeable=False, metadata_verified=False):
        self.mint_authority = mint_authority
        self.freeze_authority = freeze_authority
        self.upgradeable = upgradeable
        self.metadata_verified = metadata_verified

    def __repr__(self):
        return (f"SecurityReport(mint_authority={self.mint_authority}, "
                f"freeze_authority={self.freeze_authority}, "
                f"upgradeable={self.upgradeable}, "
                f"metadata_verified={self.metadata_verified})")