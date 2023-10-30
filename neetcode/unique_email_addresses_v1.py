from typing import List
class Solution:
    def canonicalize(self, address):
        local, domain = address.split('@')
        local = local.split('+')[0]
        local = local.replace('.', '')
        
        return "@".join([local, domain])

    def numUniqueEmailsFunc(self, emails: List[str]) -> int:
        # Without local or uniques

        return len(set([self.canonicalize(address) for address in emails]))


    def numUniqueEmails(self, emails: List[str]) -> int:
        # Create of set of unique address
        uniques = set()

        # Iterate over each string
        for address in emails:
            local, domain = address.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            
            joined = "@".join([local, domain])

            uniques.add(joined)

        

        return len(uniques)
    

        
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
local = "test.e.mail+bob.cathy" 
domain = "@leetcode.com"

local.split